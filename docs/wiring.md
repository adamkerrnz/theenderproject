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

# Manta E3EZ wiring

Pins come from Klipper's `generic-bigtreetech-manta-e3ez.cfg` and BTT's Manta-E3EZ `printer-ender3.cfg`.

| Device | Manta port | Klipper section | Pins |
| --- | --- | --- | --- |
| X motor | X | `[stepper_x]` | step PA14, dir PA10, en PA13; UART PB8 |
| Y motor | Y | `[stepper_y]` | step PC8, dir PA15, en PC14; UART PC9 |
| Z motor, left | Z | `[stepper_z]` | step PD2, dir PD4, en PD3; UART PD0 |
| Z motor, right | E0 | `[stepper_z1]` | step PD5, dir PD6, en PB3; UART PD1 |
| X endstop | X-STOP | `[stepper_x]` | PC4 |
| Y endstop | Y-STOP | `[stepper_y]` | PB0 |
| Z endstop | — | Eddy virtual endstop | stock Z switch (PC6) not used |
| Bed heater / thermistor | HB / TB | `[heater_bed]` | PB2 / PA3 |
| Electronics fan (optional) | FAN0 | `[controller_fan]` | PA8 |
| EBB36 umbilical | CAN | — | 24 V, GND, CAN-H, CAN-L |

Spare: E1 slot (PB7/PB6/PB4, UART PB5), FAN1/FAN2 (PB15/PB14), RGB (PC7), PS_ON (PA9).
