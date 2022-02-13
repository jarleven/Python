### Minimal description


* https://github.com/studioimaginaire/phue

```

pip3 install phue



```

```Python

from phue import Bridge
import time

b = Bridge('192.168.1.192')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

# Prints if light 1 is on or not
b.get_light(1, 'on')

# Set brightness of lamp 1 to max
b.set_light(1, 'bri', 254)

time.sleep(4)

# Set brightness of lamp 1 to 50%
b.set_light(1, 'bri', 127)



```

