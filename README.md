
# ICP-10111 Barometric Pressure Sensor Module

<div align="center">
  <img src="hardware/resources/unit_top_v_1_0_0_icp10111_barometric_pressure_sensor.png" width="450px" alt="Development Board">
  <p><em></em></p>
</div>

The **UNIT ICP-10111 Barometric Pressure Sensor Module** is a compact and efficient sensor designed for measuring atmospheric pressure. It utilizes the ICP10111 sensor from Infineon, which is known for its high accuracy and low power consumption. This module is ideal for applications in weather monitoring, altitude measurement, and environmental sensing.


## 📦 Overview

<div align="center">

| Feature                                  | Specification                                                     |
|------------------------------------------|-------------------------------------------------------------------|
| Pressure operating range                 | 30 to 110 kPa                                                     |
| Noise and current consumption            | ULN mode: 0.4 Pa @ 10.4 µA<br>LN mode: 0.8 Pa @ 5.2 µA<br>LP mode: 3.2 Pa @ 1.3 µA |
| Pressure Sensor Relative Accuracy        | ±1 Pa for any 10 hPa change over 950 hPa–1050 hPa at 25°C           |
| Pressure Sensor Absolute Accuracy        | ±1 hPa over 950 hPa–1050 hPa, 0°C to 65°C                           |
| Pressure Sensor Temperature Coefficient Offset | ±0.5 Pa/°C over 25°C to 45°C at 100 kPa                           |
| Temperature Sensor Absolute Accuracy     | ±0.4°C                                                           |
| Temperature operating range              | -40 °C to 85 °C                                                   |
| Host Interface                           | I2C at up to 400 kHz                                               |
| Single Supply voltage                    | 1.8V ±5%                                                         |
| RoHS and Green compliant                 | Yes                                                              |

</div>


## 🧪 Use Cases

- Altitude Control of Drones and Flying Toys
- Mobile Phones
- Virtual Reality and Gaming Equipment
- Indoor/Outdoor Navigation (dead-reckoning, floor/elevator/step detection)
- Vertical velocity monitoring
- Leisure, Sports, and Fitness Activity Identification
- Weather Forecasting

## 🚀 Getting Started

1. **Connect** the board via USB-C to your computer.
2. **Install** the appropriate board package for:
   - Arduino IDE
   - PlatformIO
   - ESP-IDF / Pico SDK
3. **Flash** a sample project or use one from `/software/examples`
4. **Power** via USB or external battery (if supported)


## 📚 Resources

- [Schematic Diagram](hardware/schematic.pdf)
- [Board Dimensions (DXF)](docs/dimensions.dxf)
- [Pinout Diagram](docs/pinout.png)
- [Firmware Examples](firmware/)
- [Getting Started Guide](docs/getting_started.md)



## 📝 License

All hardware and documentation in this project are licensed under the **MIT License**.  
Please refer to [`LICENSE.md`](LICENSE.md) for full terms.



<div align="center">
  <sub>Template created by UNIT Electronics </sub>
</div>

