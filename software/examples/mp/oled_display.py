"""
ICP-10111 OLED Display Example - MicroPython
============================================

This example shows how to display ICP-10111 sensor readings
on an OLED screen using MicroPython.

Hardware Requirements:
- ESP32 or similar MicroPython board
- ICP-10111 barometric pressure sensor
- SSD1306 OLED display (128x64)

Connections:
ICP-10111:
- VCC: 3.3V
- GND: Ground  
- SCL: GPIO 22
- SDA: GPIO 21

OLED Display:
- VCC: 3.3V
- GND: Ground
- SCL: GPIO 22 (shared with sensor)
- SDA: GPIO 21 (shared with sensor)

Author: UNIT Electronics
"""

import time
from machine import Pin, I2C
import ssd1306
from icp10111_basic import ICP10111  # Import our sensor class

def format_display_text(temp, pressure, altitude):
    """Format sensor data for OLED display"""
    lines = [
        "ICP-10111 Sensor",
        "",
        f"Temp: {temp:.1f}C",
        f"Press: {pressure:.0f}hPa", 
        f"Alt: {altitude:.1f}m",
        "",
        "UNIT Electronics"
    ]
    return lines

def main():
    """Main OLED display example"""
    print("ICP-10111 OLED Display Example")
    print("=" * 32)
    
    # Initialize I2C
    i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
    
    # Scan for I2C devices
    devices = i2c.scan()
    print(f"I2C devices: {[hex(d) for d in devices]}")
    
    try:
        # Initialize OLED display (128x64)
        oled = ssd1306.SSD1306_I2C(128, 64, i2c)
        oled.fill(0)
        oled.text("Initializing...", 0, 0)
        oled.show()
        
        # Initialize pressure sensor
        sensor = ICP10111(i2c)
        
        # Set reference pressure
        temp, press = sensor.read_sensor_data()
        sensor.set_reference_pressure(press * 100)
        
        print("Display and sensor ready!")
        
        # Main display loop
        while True:
            try:
                # Read sensor
                temperature, pressure = sensor.read_sensor_data()
                altitude = sensor.calculate_altitude(pressure * 100, sensor.reference_pressure)
                
                # Clear display
                oled.fill(0)
                
                # Format and display text
                lines = format_display_text(temperature, pressure, altitude)
                for i, line in enumerate(lines):
                    oled.text(line, 0, i * 8)
                
                # Update display
                oled.show()
                
                # Console output
                print(f"T:{temperature:.1f}C P:{pressure:.0f}hPa A:{altitude:.1f}m")
                
                time.sleep(2)
                
            except KeyboardInterrupt:
                print("\nDisplay stopped")
                oled.fill(0)
                oled.text("Stopped", 0, 0)
                oled.show()
                break
            except Exception as e:
                print(f"Display error: {e}")
                oled.fill(0)
                oled.text("Error!", 0, 0)
                oled.show()
                time.sleep(3)
    
    except Exception as e:
        print(f"Setup failed: {e}")

if __name__ == "__main__":
    main()
