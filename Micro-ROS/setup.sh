
# wget https://raw.githubusercontent.com/jarleven/Python/master/Micro-ROS/setup.sh && chmod +x setup.sh

sudo apt install cmake g++ gcc-arm-none-eabi doxygen libnewlib-arm-none-eabi git python3


# which arm-none-eabi-gcc

echo "export PICO_TOOLCHAIN_PATH=/usr/bin/arm-none-eabi-gcc" >> ~/.bashrc
echo "export PICO_SDK_PATH=$HOME/pico-sdk" >> ~/.bashrc

# Install Pico SDK
git clone --recurse-submodules https://github.com/raspberrypi/pico-sdk.git $HOME/pico-sdk

git clone https://github.com/micro-ROS/micro_ros_raspberrypi_pico_sdk.git

source ~/.bashrc

# Once the Pico SDK is ready compile the example:

cd micro_ros_raspberrypi_pico_sdk
mkdir build
cd build
cmake ..
make

# Copy the uf2 file over to the RPi Pico (Remember to puch the BOOTSEL button)
# cp ~/micro_ros_raspberrypi_pico_sdk/build/pico_micro_ros_example.uf2 /media/$USER/RPI-RP2


