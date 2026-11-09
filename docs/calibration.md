# CAN setup and calibration

## Flash the EBB36 Gen2

1. In `make menuconfig`, choose STM32G0B1, an 8 MHz crystal, and **CAN bus on PB12/PB13**. Set the bitrate to match your `can0` interface (1000000 is common).
2. Flash over USB in DFU mode, then set the USB/CAN jumper back to CAN.
3. Find the UUID with `~/klippy-env/bin/python ~/klipper/scripts/canbus_query.py can0` and put it in [`../klipper/ebb36-gen2-toolhead.cfg`](../klipper/ebb36-gen2-toolhead.cfg).

## Bring-up order

1. Heat to 50 °C and check the hotend fan spins. Run `PID_CALIBRATE HEATER=extruder TARGET=250`, then check the temperature reading against a thermocouple.
2. Calibrate `rotation_distance` by extruding 100 mm.
3. **First Eddy calibration.** Z can't home on the Eddy until it's calibrated. Follow Klipper's "Performing initial calibration when homing with probe" steps: home X and Y, set the nozzle about 20 mm above the bed centre, and run `SET_KINEMATIC_POSITION Z=25`.
4. With the coil about 20 mm above the bed, run `LDC_CALIBRATE_DRIVE_CURRENT CHIP=btt_eddy` and then `SAVE_CONFIG`.
5. Heat the bed to your normal printing temperature. The Coil has no temperature compensation. Run `PROBE_EDDY_CURRENT_CALIBRATE CHIP=btt_eddy`, do the paper test, `ACCEPT`, then `SAVE_CONFIG`.
6. Home normally and check the X/Y probe offsets. If you change either one, repeat step 5.
7. Run `BED_MESH_CALIBRATE METHOD=rapid_scan` with the bed at printing temperature.
8. Run `SHAPER_CALIBRATE AXIS=X`. On an Ender 3 the bed carries Y, so Y needs an accelerometer on the bed.

## Notes

- The Eddy needs metal under the print surface. A spring-steel PEI sheet works, but a plain glass bed won't.
- BTT says the bed mesh is invalid if the Eddy is more than about 4 mm above the bed, so keep `horizontal_move_z` around 2.
