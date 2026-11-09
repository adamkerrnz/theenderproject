# EBB36 Gen2 wiring

Pin names come from BTT's EBB36 Gen2 pin diagram and sample config ([bigtreetech/EBB](https://github.com/bigtreetech/EBB)).

## Jumpers (set before powering on)

BTT warns that the FAN1 and FAN2 power jumpers must be set correctly.

| Jumper | Setting | Why |
| --- | --- | --- |
| USB/CAN | CAN | Communicates over the umbilical |
| CAN-120R | On | Terminates the toolhead end of the bus |
| VFAN0 | VIN (24 V) | FAN0 drives the two 24 V 4010 blowers |
| VFAN2 | 5 V | FAN2 drives the 5 V X1 hotend fan |
| VPROBE | default | Unused; the Eddy runs from the I2C header's 5 V |

## Connections

| Device | EBB36 Gen2 port | Pins |
| --- | --- | --- |
| Umbilical | Power/CAN input | VIN, GND, CAN-H, CAN-L |
| Sherpa Micro motor | Motor | A1 A2 B1 B2 |
| X1 heater | HE | VIN / PB4 |
| X1 thermistor | TH | PA3 / GND |
| 4010 blowers (both) | FAN0 | VFAN0 / FAN0− (PD3) |
| X1 hotend fan | FAN2 | + → VFAN2, − → FAN2− (PD2), tach → DET (PA4). Leave PWM unconnected |
| Eddy Coil | I2C | 5 V, GND, SCL (PA7), SDA (PA6). Re-pin the supplied lead to this order |
| Neopixels (optional) | RGB | PC7 |

Check every fan and sensor lead with a meter before cutting connectors off.
