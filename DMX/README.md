### Some DMX notes

```

https://www.tomshardware.com/how-to/control-dmx-lights-raspberry-pi

pi@raspberrypi:/etc/ola $ ola_dev_info | grep FT232R
Device 11: FT232R USB UART with serial number : AB0PUZ6U
  port 1, OUT FT232R USB UART with serial number : AB0PUZ6U

pi@raspberrypi:/etc/ola $ ola_patch -d 11 -p 1 -u 0


```
