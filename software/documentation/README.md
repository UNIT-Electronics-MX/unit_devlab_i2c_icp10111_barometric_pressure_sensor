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

# Template Development Board

![product](./images/top.png) <!-- FILL HERE: replace image if needed -->

## Introduction

<!-- FILL HERE -->
The **ICP-10111 Barometric Pressure Sensor Module** is a compact and efficient sensor designed for high-accuracy atmospheric pressure measurements with low power consumption. Based on MEMS capacitive technology, this module offers ultra-low noise performance, exceptional relative accuracy, and stable sensor throughput. Ideal for weather monitoring, altitude measurement, and environmental sensing, it delivers industry-leading precision in demanding applications.

## Functional Description

<!-- FILL HERE -->
- **High Accuracy**  
  - Differential: ±1 Pa (10 hPa span at 25 °C)  
  - Absolute: ±1 hPa (950 hPa–1050 hPa over –40 °C to +85 °C)
- **Ultra-Low Power Modes**  
  - Ultra-Low Noise: 10 Hz sample, 10.4 µA  
  - Low Noise: 10 Hz sample, 5.2 µA  
  - Low Power: 10 Hz sample, 1.3 µA
- **Wide Pressure Range**  
  - 30 kPa to 110 kPa (300 mbar–1100 mbar)
- **Built-In Temperature Sensor**  
  - ±0.4 °C accuracy, used for real-time compensation
- **I²C Interface**  
  - Supports up to 400 kHz clock  
  - Standard 7-bit address: 0x63 (GNDBIAS pin floating)
- **Qwiic / STEMMA QT Connector**  
  - Plug-and-play I²C connectivity, no soldering required
- **Operating Voltage**  
  - Module: 3.3 V–5.5 V  
  - On-chip sensor core: 1.8 V
- **Operating Temperature**  
  - –40 °C to +85 °C
- **Compact Footprint**  
  - 20.32 × 17.78 mm PCB with four mounting holes

## Electrical Characteristics & Signal Overview

<!-- FILL HERE -->
| Parameter                   | Value                                  |
|-----------------------------|----------------------------------------|
| Pressure Range              | 30 kPa – 110 kPa                       |
| Differential Accuracy       | ±1 Pa (10 hPa span @ 25 °C)            |
| Absolute Accuracy           | ±1 hPa (950–1050 hPa, –40 °C to +85 °C) |
| Temperature Accuracy        | ±0.4 °C                                |
| Pressure Noise (RMS)        | 0.4 Pa (ULN mode), 0.8 Pa (LN), 3.2 Pa (LP) |
| Supply Current              | 1.3 µA – 10.4 µA (depends on mode)     |
| I²C Speed                   | Up to 400 kHz                          |
| I²C Address                 | 0x63 (default)                         |
| Supply Voltage              | 3.3 V – 5.5 V                          |
| Sensor Core Voltage         | 1.8 V internal                        |
| Operating Temperature Range | –40 °C to +85 °C                       |


## Applications

<!-- FILL HERE -->
- Weather Stations & Barographs
  - Track atmospheric pressure trends.

- Altimeters & UAVs
  - Estimate real-time altitude changes.

- Indoor/Outdoor Navigation
  - Enhance GPS accuracy with pressure-based elevation.

- Wearables & IoT
  - Monitor environmental conditions in low-power devices.

- Climatology & Research
  - High-resolution pressure mapping for science projects.
- Weather Forecasting

## Features

| Parameter                   | Value                                  |
|-----------------------------|----------------------------------------|
| Board Dimensions            | 20.32 mm × 17.78 mm                    |
| Mounting Holes              | 4 × Ø 2.2 mm                           |

  

## Pin & Connector Layout
| Pin   | Type    | Voltage Level | Function                                                  |
|-------|---------|---------------|-----------------------------------------------------------|
| VCC   | Power   | 3.3 V – 5.5 V  | Provides power to the on-board regulator and sensor core. |
| GND   | Ground  | 0 V           | Common reference for power and signals.                   |
| SDA   | I²C Data| 1.8 V to VCC  | Serial data line for I²C communications.                  |
| SCL   | I²C Clock| 1.8 V to VCC | Serial clock line for I²C communications.                 |

> **Note:** The module also includes a Qwiic/STEMMA QT connector carrying the same four signals (VCC, GND, SDA, SCL) for effortless daisy-chaining.

## Settings

### Interface Overview

| Interface  | Signals / Pins         | Typical Use                              |
|------------|------------------------|------------------------------------------|
| UART       | <!-- FILL -->          | <!-- FILL -->                             |
| I2C        | <!-- FILL -->          | <!-- FILL -->                             |
| SPI        | <!-- FILL -->          | <!-- FILL -->                             |
| USB        | <!-- FILL -->          | <!-- FILL -->                             |

### Supports

| Symbol | I/O         | Description                        |
|--------|-------------|------------------------------------|
| VCC    | Input       | <!-- FILL -->                      |
| GND    | GND         | <!-- FILL -->                      |
| IO     | Bidirectional | <!-- FILL -->                   |

## Block Diagram

![Function Diagram](images/pinout.png) <!-- FILL HERE: replace image if needed -->

## Dimensions

![Dimensions](images/dimension.png) <!-- FILL HERE: replace image if needed -->

## Usage

<!-- FILL HERE -->
Mention supported development platforms and toolchains 

- (e.g., Arduino IDE, ESP-IDF, PlatformIO, etc.)

## Downloads

<!-- FILL HERE -->
- [Schematic PDF](docs/schematic.pdf)
- [Board Dimensions DXF](docs/dimensions.dxf)
- [Pinout Diagram PNG](docs/pinout.png)

## Purchase

<!-- FILL HERE -->
- [Buy from vendor](https://example.com)
- [Product page](https://example.com/product/template-board)
