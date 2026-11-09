# First power-on and calibration

Do [CAN setup](can-setup.md) first, then fill in both `canbus_uuid` values.

## 1. Before anything moves

1. Run `STEPPER_BUZZ STEPPER=stepper_x` (repeat for `stepper_y`, `stepper_z`, `stepper_z1`, `extruder`). Each one should move back and forth +1 mm / −1 mm. For the two Z motors, check they **lift the gantry in the same direction**. If `stepper_z1` fights `stepper_z`, flip its `dir_pin` before you do anything else.
2. Check the endstops with `QUERY_ENDSTOPS`, pressing each switch by hand.
3. Heat to 50 °C and check the hotend fan spins (FAN2, 5 V). Run `PID_CALIBRATE HEATER=extruder TARGET=250`, then `PID_CALIBRATE HEATER=heater_bed TARGET=60`, then `SAVE_CONFIG`. Check the hotend reading against a thermocouple, since the X1 thermistor type isn't published.

## 2. X/Y limits

1. Home X and Y. Jog to the left/front bed edge and set `position_endstop` / `position_min` so the nozzle can reach X0/Y0. The Mini Stealth and the front rail both move the nozzle relative to stock.
2. Jog to the far edges and set `position_max`.

## 3. Eddy Coil

Z can't home on the Eddy until it's calibrated. The `EDDY_FIRST_CALIBRATION` macro covers the unhomed start.

1. Manually raise the nozzle to about 20 mm above the bed centre, then run `EDDY_FIRST_CALIBRATION`.
2. Run `LDC_CALIBRATE_DRIVE_CURRENT CHIP=btt_eddy`, then `SAVE_CONFIG`.
3. Heat the bed to your normal printing temperature. The Coil has no temperature compensation.
4. Run `G28 X Y` and `SET_KINEMATIC_POSITION Z=25`. Then run `PROBE_EDDY_CURRENT_CALIBRATE CHIP=btt_eddy`, do the paper test, `ACCEPT`, then `SAVE_CONFIG`.
5. Run `G28` and check the probe offsets with Klipper's `PROBE_CALIBRATE` procedure. If you change `x_offset` / `y_offset`, repeat step 4.

## 4. Gantry and mesh

1. Measure where the two Z belts lift the gantry, and set `[z_tilt] z_positions`.
2. Run `LEVEL_GANTRY` (home → `Z_TILT_ADJUST` → re-home Z). It should converge within the retries.
3. Run `BED_MESH_CALIBRATE METHOD=rapid_scan` with the bed at printing temperature, then `SAVE_CONFIG`.
4. Command a 10 mm Z move and measure it, to check `rotation_distance: 8` on both Z steppers.

## 5. Extruder and motion tuning

1. `rotation_distance`: mark 120 mm of filament, extrude 100 mm, then adjust.
2. `SHAPER_CALIBRATE AXIS=X` uses the EBB36's built-in accelerometer. On an Ender 3 the bed carries Y, so Y needs a separate accelerometer on the bed (or skip it and set `[input_shaper]` for X only).
3. Tune pressure advance, then raise `max_accel` to what the input shaper report recommends.

## Notes

- The Eddy needs metal under the print surface. A spring-steel PEI sheet works, but a plain glass bed won't.
- BTT says the mesh is invalid if the Eddy is more than about 4 mm above the bed, so keep `horizontal_move_z` around 2.
- `PRINT_START` heats the bed fully before Z_TILT_ADJUST and the mesh, so probing happens at the same temperature as calibration.
