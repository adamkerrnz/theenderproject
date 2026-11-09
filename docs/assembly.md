# Assembly

Build the core as one unit, mount it on the x-frame, then slide the shroud on. The shroud, fans and probe can later come off without removing the hotend.

1. **Check rail spacing.** The Front MGN9H x-frames assume 4.5 mm between the 2020 extrusion and the back of the rail. If yours differs, the nozzle height and belt line will be off.
2. **Check the extruder fit.** Print the core first, and confirm the Mellow Sherpa Micro's mounting holes line up with it.
3. **Glue the air guides.** Dry-fit each guide and check that the impeller spins freely. Screw the jig onto the guide (M3 × 20) so it sits flush with the blower bottom. Glue the two sides and the back face, hold for about a minute, then remove the jig. Repeat for the second blower.
4. **Set the heat-set inserts** in the core, the motor bridge (two) and the cable door.
5. **Build the core.** Screw the X1 hotend into the Bambu core with two M3 screws, then mount the Sherpa Micro. Feed the heater and thermistor leads through the core.
6. **Mount the EBB36.** Fit the motor bridge, then screw the PCB mount onto it and the EBB36 onto the mount. Route the motor, heater, thermistor, fan and Eddy leads to the board.
7. **Mount the x-frame.** Bolt both halves to the MGN9H carriage. Lock each belt end with a toothed wedge from below, then tension the belt.
8. **Fit the core** to the x-frame with two M3 BHCS. If tightening binds the carriage, add DIN 988 shims. Push X by hand along its full length to check it moves freely.
9. **Fit the fans and Eddy.** Mount the blowers and the X1 fan in the shroud, and seat the magnets flush. Attach the Eddy bracket (M2.5 × 6 flat-heads) and the Eddy Coil. The coil bottom should be 2–3 mm above the nozzle tip. Swap bracket heights if needed. Keep the coil cable away from the heater block, and fold any slack in a figure 8 rather than coiling it.
10. **Close up.** Slide the shroud on, fit the cable door, and strain-relieve the umbilical at both ends.
11. **Check clearances.** Jog to all four corners and to X-min. Make sure the EBB36 behind the motor clears the Z uprights.

## Known issues

- Front-mounted rail: the nozzle sits further forward than stock. Re-measure the Y home position, and expect to lose a little bed depth.
- Self-tapping M2.5 holes in the side brackets sometimes don't grip. Open them slightly, or use M2.5 heat-set inserts.
- The Mini Stealth designer hasn't published v2 assembly instructions yet. The `.blend` files in the Mini Stealth repo are the reference model.
