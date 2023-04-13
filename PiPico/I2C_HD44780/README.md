## HD44780 LCD with I2C interface



* https://peppe8o.com/using-i2c-lcd-display-with-raspberry-pi-pico-and-micropython/



```python

import machine
sdaPIN=machine.Pin(0)
sclPIN=machine.Pin(1)
i2c=machine.I2C(0,sda=sdaPIN, scl=sclPIN, freq=400000)
devices = i2c.scan()
if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))
for device in devices:
  print("Hexa address: ",hex(device))

```

```
i2c devices found: 1
Hexa address:  0x27
```
