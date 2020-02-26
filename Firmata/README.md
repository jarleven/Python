

python3 -m pip install --upgrade --force-reinstall --user pyfirmata


```Python
# Pyton script in it's simplest form
# Tested on Examples->Firmata->StandardFirmata

from pyfirmata import Arduino, util
import time
board = Arduino('/dev/ttyUSB0')

while True:
  time.sleep(1)
  print("High")
  board.digital[13].write(1)
  time.sleep(1)
  print("Low")
  board.digital[13].write(0)
```
