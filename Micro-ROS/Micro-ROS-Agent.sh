# wget https://raw.githubusercontent.com/jarleven/Python/master/Micro-ROS/Micro-ROS-Agent.sh && chmod +x Micro-ROS-Agent.sh

# https://artivis.github.io/post/2021/pi-pico-uros-getting-started/



sudo snap install micro-ros-agent
# After installing it, and because we are using a serial connection, we need to configure a couple things. First we need to enable the 'hotplug' feature,

sudo snap set core experimental.hotplug=true
# and restart the snap demon so that it takes effect,

sudo systemctl restart snapd
# After making sure the Pi Pico is plugged, execute,

snap interface serial-port
# name:    serial-port
# summary: allows accessing a specific serial port
# plugs:
#  - micro-ros-agent
# slots:
#  - snapd:pico (allows accessing a specific serial port)

# What we see here is that the micro-ros-agent snap has a serial ‘plug’ while a ‘pico’ 'slot' magically appeared. 
# As per the semantic, we probably should connect them together. To do so run,

snap connect micro-ros-agent:serial-port snapd:pico
# We are now all set to finally run our example.

# Actually running the example
# With the Pi Pico plugged through USB, we will start the micro-ros-agent as follows,

micro-ros-agent serial --dev /dev/ttyACM0 baudrate=115200
# and wait a couple seconds for the Pi Pico’s LED to light up indicating that the main loop is running.
# In case it does not light up after a few long seconds (count up to 10 mississippi), you may want to unplug/replug the board in order to reboot it.
# The initialization procedure of the example lacks a few error checking. Hey, could fixing that be your first project?
