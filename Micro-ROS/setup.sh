
# wget https://raw.githubusercontent.com/jarleven/Python/master/Micro-ROS/setup.sh && chmod +x setup.sh

# Thanks to https://robofoundry.medium.com/raspberry-pi-pico-ros2-via-micro-ros-actually-working-in-1-hr-9f7a3782d3e3


sudo apt update && sudo apt upgrade -y

sudo apt install -y build-essential cmake gcc-arm-none-eabi libnewlib-arm-none-eabi doxygen git python3

# Configure environment variables
echo "export PICO_TOOLCHAIN_PATH=..." >> ~/.bashrc
echo "export PICO_SDK_PATH=$HOME/micro_ros_ws/src/pico-sdk" >> ~/.bashrc
source ~/.bashrc


mkdir -p ~/micro_ros_ws/src
cd ~/micro_ros_ws/src
### clone the pico-sdk
git clone --recurse-submodules https://github.com/raspberrypi/pico-sdk.git
### clone the micro-ros example repo. This example simply publishes an incrementing integer value every second
git clone https://github.com/micro-ROS/micro_ros_raspberrypi_pico_sdk.git



