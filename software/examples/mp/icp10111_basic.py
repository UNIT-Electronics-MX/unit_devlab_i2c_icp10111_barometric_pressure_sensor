"""
ICP-10111 Barometric Pressure Sensor - MicroPython Example
==========================================================

This example demonstrates how to read temperature, pressure, and altitude
from the ICP-10111 sensor using MicroPython on ESP32 or similar boards.

Hardware Connections:
- VCC: 3.3V or 5V
- GND: Ground
- SCL: GPIO 22 (or your preferred I2C clock pin)
- SDA: GPIO 21 (or your preferred I2C data pin)

Author: UNIT Electronics
License: MIT
"""

import time
from machine import Pin, I2C
import struct
import math

class ICP10111:
    """Driver class for ICP-10111 barometric pressure sensor"""
    
    # I2C address (7-bit address)
    ADDRESS = 0x63
    
    # Command codes
    CMD_READ_ID = 0xEFC8
    CMD_SET_MODE = 0x6825
    CMD_READ_DATA = 0x48A3
    
    def __init__(self, i2c, address=ADDRESS):
        """Initialize the sensor"""
        self.i2c = i2c
        self.address = address
        self.reference_pressure = None
        
        # Initialize sensor
        self._init_sensor()
    
    def _init_sensor(self):
        """Initialize sensor settings"""
        # Set measurement mode (normal mode, high accuracy)
        mode_cmd = struct.pack('>H', self.CMD_SET_MODE)
        self.i2c.writeto(self.address, mode_cmd)
        time.sleep_ms(100)
    
    def read_sensor_data(self):
        """Read temperature and pressure from sensor"""
        # Send read command
        read_cmd = struct.pack('>H', self.CMD_READ_DATA)
        self.i2c.writeto(self.address, read_cmd)
        time.sleep_ms(50)
        
        # Read 6 bytes of data (3 bytes temp + 3 bytes pressure)
        data = self.i2c.readfrom(self.address, 6)
        
        # Parse temperature (first 3 bytes)
        temp_raw = (data[0] << 16) | (data[1] << 8) | data[2]
        
        # Parse pressure (last 3 bytes)  
        press_raw = (data[3] << 16) | (data[4] << 8) | data[5]
        
        # Convert to actual values (simplified conversion)
        temperature = (temp_raw - 32768) / 256.0  # Approximate conversion
        pressure = press_raw / 100.0  # Convert to hPa
        
        return temperature, pressure
    
    def calculate_altitude(self, pressure, reference_pressure=101325):
        """Calculate altitude using barometric formula"""
        if reference_pressure is None:
            reference_pressure = 101325  # Standard sea level pressure in Pa
        
        # Barometric formula
        altitude = 44330 * (1 - pow(pressure / reference_pressure, 0.1903))
        return altitude
    
    def set_reference_pressure(self, pressure):
        """Set reference pressure for altitude calculation"""
        self.reference_pressure = pressure

def main():
    """Main example function"""
    print("ICP-10111 Barometric Pressure Sensor Example")
    print("=" * 45)
    
    # Initialize I2C (adjust pins for your board)
    i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
    
    # Scan for devices
    devices = i2c.scan()
    print(f"I2C devices found: {[hex(d) for d in devices]}")
    
    try:
        # Initialize sensor
        sensor = ICP10111(i2c)
        print("Sensor initialized successfully!")
        
        # Take reference pressure reading
        temp, press = sensor.read_sensor_data()
        sensor.set_reference_pressure(press * 100)  # Convert hPa to Pa
        print(f"Reference pressure set to: {press:.2f} hPa")
        
        print("\nStarting measurements...")
        print("Temp(°C) | Press(hPa) | Altitude(m)")
        print("-" * 35)
        
        # Main measurement loop
        while True:
            try:
                # Read sensor data
                temperature, pressure = sensor.read_sensor_data()
                
                # Calculate altitude
                altitude = sensor.calculate_altitude(pressure * 100, sensor.reference_pressure)
                
                # Display results
                print(f"{temperature:7.2f} | {pressure:9.2f} | {altitude:9.2f}")
                
                time.sleep(1)  # Wait 1 second between readings
                
            except KeyboardInterrupt:
                print("\nMeasurement stopped by user")
                break
            except Exception as e:
                print(f"Error reading sensor: {e}")
                time.sleep(2)
    
    except Exception as e:
        print(f"Failed to initialize sensor: {e}")

if __name__ == "__main__":
    main()
