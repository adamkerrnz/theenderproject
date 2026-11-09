# Print list

Print in ABS or ASA, since the core and shroud sit next to the heater block. Files with `[a]` in the name are accent-colour parts.
Files are in [`../stl/`](../stl/). The source paths are in the original [Mini Stealth repo](https://github.com/atrushing/Mini_Stealth).

| Part | File | Qty | Source path / notes |
| --- | --- | --- | --- |
| X-frame, left | `Ender3_MGN9H_Front_x-frame_Left.stl` | 1 | `Ender_3_parts/Switchwire Style Mount/` |
| X-frame, right | `Ender3_MGN9H_Front_x-frame_Right.stl` | 1 | same folder |
| Belt wedge | `Belt_Clamping_Wedge.stl` | 2 | same folder (`Belt Clamping Wedge.stl`). Locks each belt end from below |
| MGN9H spacer | `1mm_thick_MGN9H_Spacer.stl` | 0–1 | same folder. 30 × 20 × 1 mm shim. Its use isn't documented, so print it only if the dry fit needs it |
| Core | `MiniStealth_Core_SherpaMicro_Bambu.stl` | 1 | `Extruders/Sherpa_Micro/Cores/`. Standard core, not `Alternate_Rigid` |
| Shroud | `[a]_MiniStealth_Shroud_SherpaMicro_ProbeRight_2510.stl` | 1 | `Extruders/Sherpa_Micro/Shrouds/2510 Hotend Fan/ProbeRight/`. Standard length, not `_UHF` |
| Eddy bracket | `Side_Mount_V0_BTT_Eddy_bracket.stl` | 1 | `Ender_3_parts/`. If the coil sits too high, print `_1mm_Lower` or `_1.5mm_Lower` instead |
| Motor bridge | `SherpaMicro_Motor_Bridge_UmbilicalPCB_Mount.stl` | 1 | `Extruders/Sherpa_Micro/`. Two inserts for the PCB mount |
| EBB36 mount | `SherpaMicro_UmbilicalPCB_Mount.stl` | 1 | `Extruders/Sherpa_Micro/`. Holds the board upright behind the motor. Its two screw points are 43.8 mm apart, matching the EBB36's mounting holes |
| Cable door | `SherpaMicro_Cable_Door.stl` | 1 | `Extruders/Sherpa_Micro/` |
| Blower air guides | `Blower_guide_x2.stl` | 2 | `Common_Parts/`. Glued into the 4010 blowers |
| Air-guide gluing jig | `Blower_guide_gluing_tool_M3x20.stl` | 1 | `Common_Parts/`. Assembly tool |

Don't use the Mini Stealth repo's `Sherpa_Micro_Mirrored` folder. It's the designer's own modified extruder and won't fit a stock or Mellow CNC Sherpa Micro.

**About the Bambu core.** The Mini Stealth readme says the Bambu and Dragonfly BMS cores are the only ones that need heat-set inserts to hold the hotend. The designer suggests fixing the hotend with two screws rather than one.
