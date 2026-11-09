# Hardware / BOM

Where no length is given, measure during the dry fit. The Mini Stealth designer's advice is to dry-run before final assembly.

## Electronics

| Item | Qty | Notes |
| --- | --- | --- |
| BTT EBB36 Gen2 (CAN) | 1 | Mounted on the umbilical PCB mount behind the extruder motor |
| USB-to-CAN adapter (e.g. BTT U2C) | 1 | Creality Ender 3 boards have no CAN port. Not needed if your mainboard has CAN |
| Klipper host (Raspberry Pi or similar) | 1 | The EBB36 runs only Klipper |
| Umbilical cable | 1 | 24 V + GND (about 18 AWG) and a twisted CAN-H/CAN-L pair. 120 Ω termination at both ends |
| BTT Eddy Coil | 1 | I2C to the EBB36. No temperature compensation |
| 4010 blower fans, 24 V | 2 | Part cooling, on EBB36 FAN0 |
| Bambu X1 hotend fan (2510, 5 V) | 1 | Stock fan, on EBB36 FAN2 with VFAN2 set to 5 V |
| Connectors | — | Re-terminate the X1 heater and thermistor (Bambu-specific plugs) for the EBB36's HE and TH ports. Re-pin the Eddy Coil's DuPont lead to the Gen2 I2C pin order |

## Fasteners and consumables

| Item | Qty | Where it goes |
| --- | --- | --- |
| M3 heat-set inserts | ~5–7 | Bambu hotend into the core (required), Sherpa Micro to the core, two in the motor bridge for the PCB mount, cable door |
| M3 screws, hotend | 2 | Bambu X1 hotend into the core's inserts |
| M3 BHCS, 25 mm spacing | 2 | Core to x-frame. The designer uses M3 × 40 on the DAB carriage |
| M3 DIN 988 shim washers | a few | Under the core screws if tightening starts to crush the linear carriage |
| M3 screws | 4 | X-frame to the MGN9H carriage block |
| M2.5 × 6 flat-head | 2 | Eddy bracket to the shroud (self-tapping) |
| M3 screws, Eddy | 2 | Eddy to bracket (the Eddy kit includes some) |
| M3 standoffs/screws | 2 | EBB36 to the PCB mount |
| 3 × 6 mm magnets | optional | Core-to-shroud pockets. They must sit flush |
| M3 × 20 | 1 | Temporarily holds the gluing jig |
| Gel superglue | — | Air guides. The designer says it is usable to about 250 °C |

The heat-set insert locations are shown in [`img/Heatsets1.png`](img/Heatsets1.png) and [`img/Heatsets2.png`](img/Heatsets2.png), both from the Mini Stealth repo.
