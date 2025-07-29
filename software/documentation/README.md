---
title: "ICP-10111 Barometric Pressure Sensor"
version: "1.0"
modified: "2025-04-30"
output: "icp_10111_barometric_pressure_sensor"
subtitle: "Compact and efficient sensor designed for high-accuracy atmospheric pressure measurements"
---

<!--
# README_TEMPLATE.md
This file serves as an input to generate a datasheet-style technical PDF.
Fill in each section without deleting or modifying the existing headings.
-->

# ICP-10111 Barometric Pressure Sensor

![product](../../hardware/resources/unit_top_v_1_0_0_icp10111_barometric_pressure_sensor.png)


## Functional Description

The ICP-10111 is a high-precision barometric pressure sensor module based on capacitive MEMS technology.  
- Measures absolute pressure over 30 kPa–110 kPa and integrates a temperature sensor for real-time thermal compensation.  
- Delivers ±1 Pa differential accuracy (≈5 cm altitude resolution) and ±1 hPa absolute accuracy across –40 °C…+85 °C.  
- Built-in 24-bit ΔΣ ADC and I²C interface allow direct digital readout without external amplification.  
- Three programmable power/noise modes (Ultra-Low Noise, Low Noise, Low Power) optimize trade-off between current draw and resolution.  
- Breakout board includes onboard 1.8 V regulator, level-shifting I/O and four mounting holes for easy integration.

## Key Specifications

| Parameter | Value | Notes |
|-----------|--------|-------|
| Pressure Range | 30 kPa to 110 kPa | Absolute pressure measurement |
| Absolute Accuracy | ±1 hPa | Across full temperature range |
| Relative Accuracy | ±1 Pa | ≈5 cm altitude resolution |
| Supply Voltage | 3.3V - 5.5V | On-board regulator |
| Current Consumption | 1.3 - 10.4 µA | Depends on mode selection |
| Interface | I²C | 400 kHz max, address 0x63 |
| Operating Temperature | -40°C to +85°C | Industrial grade |
| Board Dimensions | 20.32 × 17.78 mm | Compact form factor |

## Electrical Characteristics & Signal Overview

- Supply Voltage: 3.3 V–5.5 V (module), 1.8 V (sensor core)  
- Supply Current:  
  - Ultra-Low Noise (10 Hz): 10.4 µA  
  - Low Noise (10 Hz): 5.2 µA  
  - Low Power (10 Hz): 1.3 µA  
- Pressure Resolution: 24-bit ΔΣ ADC (sub-Pa level)  
- Temperature Resolution: 0.01 °C (±0.4 °C accuracy)  
- I²C Interface: up to 400 kHz, 7-bit address 0x63  
- Logic Levels: VCC-referenced (1.8 V – 5.5 V tolerant)  
- Measurement Rates: 1 Hz to 100 Hz selectable
- Operating Temperature: -40°C to +85°C
- Pressure Range: 30 kPa to 110 kPa
- Absolute Accuracy: ±1 hPa
- Relative Accuracy: ±1 Pa (≈5 cm altitude resolution)
- Package: 20.32 mm × 17.78 mm breakout board
- Mounting: 4 × Ø 2.2 mm holes 


## Applications

<!-- FILL HERE -->
- Weather Stations & Barographs

- Altimeters & UAVs

- Indoor/Outdoor Navigation

- Wearables & IoT

- Climatology & Research

- Weather Forecasting

## Features

- Board Dimensions 20.32 mm × 17.78 mm
- Mounting Holes 4 × Ø 2.2 mm
- High-stability MEMS capacitive pressure sensor with low drift  
- Integrated temperature sensor for on-board compensation  
- Ultra-low-noise ΔΣ ADC with 24-bit resolution  
- Three user-selectable power/noise modes for optimized current usage  
- Qwiic/STEMMA QT connector for solder-free I²C daisy-chaining  
- On-board level shifting and 1.8 V core regulator    
- Wide operating range: –40 °C to +85 °C, 30 kPa to 110 kPa

## Pin & Connector Layout
| Pin   | Voltage Level | Function                                                  |
|-------|---------------|-----------------------------------------------------------|
| VCC   | 3.3 V – 5.5 V | Provides power to the on-board regulator and sensor core. |
| GND   | 0 V           | Common reference for power and signals.                   |
| SDA   | 1.8 V to VCC  | Serial data line for I²C communications.                  |
| SCL   | 1.8 V to VCC  | Serial clock line for I²C communications.                 |

> **Note:** The module also includes a Qwiic/STEMMA QT connector carrying the same four signals (VCC, GND, SDA, SCL) for effortless daisy-chaining.

## Settings

### Interface Overview

| Interface | Signals / Pins                            | Typical Use                                      |
|-----------|-------------------------------------------|-------------------------------------------------|
| I²C       | SDA, SCL, VCC, GND (via Qwiic/STEMMA QT™) | Main digital interface for pressure & temperature |


### Supports

| Symbol | I/O Type      | Description                                |
|--------|---------------|--------------------------------------------|
| VCC    | Power Input   | 3.3 V–5.5 V supply for on-board regulator  |
| GND    | Ground        | Common system ground                       |
| SDA    | Bidirectional | I²C data line (7-bit address 0x63 default) |
| SCL    | Bidirectional | I²C clock line                             |

## Circuit Schematic

![Circuit Schematic](../../hardware/resources/Schematics_icon.jpg)

Complete circuit schematic showing all component connections

[View Complete Schematic PDF](../../hardware/unit_sch_V_0_0_1_ue0094_ICP-10111.pdf)

## Block Diagram

![Function Diagram](../../hardware/resources/unit_pinout_v_0_0_1_ue0094_icp10111_barometric_pressure_sensor_en.png)

## Dimensions

![Dimensions](../../hardware/resources/unit_dimension_v_1_0_0_icp10111_barometric_pressure_sensor.png)

## Usage

- Arduino IDE  
  - Install SparkFun_ICP10111 library via Library Manager  
  - Include <Wire.h> and <SparkFun_ICP10111.h> in your sketch  
- PlatformIO  
  - Add sparkfun/sparkfun-icp10111@^1.0.0 to lib_deps in platformio.ini  
- Raspberry Pi (Linux/C or Python)  
  - Use the I²C-1 bus (/dev/i2c-1) with smbus2 (Python) or i2c-dev (C)  
- CircuitPython / MicroPython  
  - Install adafruit_icp10111 from the Adafruit bundle  
  - Use busio.I2C or I2C() to communicate over SDA/SCL  
