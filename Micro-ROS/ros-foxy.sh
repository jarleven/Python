# wget https://raw.githubusercontent.com/jarleven/Python/master/Micro-ROS/ros-foxy.sh && chmod +x ros-foxy.sh

# https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html

sudo apt update && sudo apt install curl gnupg2 lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

sudo apt update
sudo apt upgrade -y

sudo apt install -y ros-foxy-desktop



