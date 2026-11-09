# CAN bus setup – Manta E3EZ + CB1 + EBB36 Gen2

The Manta's own STM32G0B1 runs Klipper in **USB-to-CAN bridge** mode. The CB1 talks to it over the Manta's internal USB hub and sees a `can0` interface. The EBB36 then hangs off the Manta's CAN port, so **no U2C adapter is needed**.

```
CB1 ──USB (on-board)──► Manta E3EZ MCU (bridge) ──CAN port──► umbilical ──► EBB36 Gen2
```

Both MCUs end up with a `canbus_uuid`. The UUIDs are left blank in `klipper/printer.cfg` and `klipper/ebb36-gen2-toolhead.cfg`.

## 1. can0 on the CB1

Create `/etc/network/interfaces.d/can0`:

```
allow-hotplug can0
iface can0 can static
    bitrate 1000000
    up ip link set $IFACE txqueuelen 1024
```

The bitrate must match both firmware builds below. Klipper's docs recommend `txqueuelen 1024`.

## 2. Manta E3EZ firmware (bridge)

`cd ~/klipper && make menuconfig`:

| Option | Value |
| --- | --- |
| Enable extra low-level configuration options | yes |
| Micro-controller architecture | STMicroelectronics STM32 |
| Processor model | STM32G0B1 |
| Bootloader offset | 8KiB bootloader |
| Clock reference | 8 MHz crystal |
| Communication interface | **USB to CAN bus bridge (USB on PA11/PA12)** |
| CAN bus interface | **CAN bus (on PB12/PB13)** |
| CAN bus speed | 1000000 |

Then run `make`, copy `out/klipper.bin` to a microSD card as `firmware.bin`, put it in the Manta's card slot and power-cycle. (While the Manta still shows up as a USB serial device, `make flash FLASH_DEVICE=/dev/serial/by-id/...` also works.)

After a reboot, `ip -details link show can0` should show the interface. `~/klippy-env/bin/python ~/klipper/scripts/canbus_query.py can0` should list the Manta's UUID. Put it in `[mcu] canbus_uuid`.

## 3. EBB36 Gen2 firmware

| Option | Value |
| --- | --- |
| Processor model | STM32G0B1 |
| Bootloader offset | No bootloader (flashing via DFU) – or 8KiB if you install Katapult |
| Clock reference | 8 MHz crystal |
| Communication interface | **CAN bus (on PB12/PB13)** |
| CAN bus speed | 1000000 |

Set the EBB36's USB/CAN jumper to USB, then hold BOOT, tap RST, and flash over USB with `make flash FLASH_DEVICE=0483:df11`. Afterwards set the jumper back to **CAN**, fit the **120R** jumper, and wire the umbilical: 24 V, GND, CAN-H, CAN-L to the Manta's CAN port. The Manta end of the bus needs 120 Ω termination too. Check the Manta E3EZ manual for its 120R jumper.

Run `canbus_query.py can0` again. A second UUID appears, which goes in `[mcu EBB] canbus_uuid`.

Optional: installing [Katapult](https://github.com/Arksine/katapult) on the EBB36 lets you update its firmware over CAN later without opening the toolhead.

## Troubleshooting

- `canbus_query.py` only lists UUIDs for boards that aren't currently connected to Klipper. Stop Klipper first (`sudo service klipper stop`), or read the UUIDs from `klippy.log`.
- No `can0` at all: the Manta build probably used plain "CAN bus" instead of "USB to CAN bus bridge" as the communication interface.
- Random disconnects: check termination (exactly two 120 Ω, one at each end), the twisted pair, and that both builds use the same bitrate.
