##  Ubuntu 18.04.3 LTS
* Trying to make a simple description for some students
* Date 11. Des 2019

```
Download : http://releases.ubuntu.com/18.04/ubuntu-18.04.3-desktop-amd64.iso
Tensorflow versions are here : https://www.tensorflow.org/versions/

# Norwegian keyboard map
setxkbmap no

# Set path and update
echo "export PATH=$PATH:~/.local/bin" >> ~/.bash_profile
source ~/.bash_profile

# Install 
sudo apt install -y git
sudo apt install -y python3-pip

python3 -m pip install --upgrade --user pip 


python3 -m pip install --upgrade --force-reinstall tensorflow==1.15 --user
# Edit At the time 1.15 is the lastest / final 1.x version.

# Get the "Models and examples built with TensorFlow"
cd ~
git clone https://github.com/tensorflow/models.git
cd ~/models/tutorials/image/imagenet

# Test if everything works
python3 classify_image.py



# Download some random image
wget https://i.dailymail.co.uk/1s/2019/11/23/09/21370544-7717313-image-a-1_1574501083030.jpg -O ~/test.jpg

# Calssify this image
python3 classify_image.py --image_file ~/test.jpg

```

Resource
```
https://www.tensorflow.org/install/pip
```



Info about Python and PIP versions
```
python3 --version
Python 3.6.9

python3 -m pip --version
pip 19.3.1 from /home/jarleven/.local/lib/python3.6/site-packages/pip (python 3.6)


```

Output is 
```
>> Downloading inception-2015-12-05.tgz 100.0%
Successfully downloaded inception-2015-12-05.tgz 88931400 bytes.
2019-10-25 12:51:16.934624: W tensorflow/core/framework/op_def_util.cc:346] Op BatchNormWithGlobalNormalization is deprecated. It will cease to work in GraphDef version 9. Use tf.nn.batch_normalization().
2019-10-25 12:51:17.098627: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2019-10-25 12:51:17.271974: W tensorflow/core/framework/allocator.cc:108] Allocation of 8257536 exceeds 10% of system memory.
giant panda, panda, panda bear, coon bear, Ailuropoda melanoleuca (score = 0.89107)
indri, indris, Indri indri, Indri brevicaudatus (score = 0.00779)
lesser panda, red panda, panda, bear cat, cat bear, Ailurus fulgens (score = 0.00296)
custard apple (score = 0.00147)
earthstar (score = 0.00117)
```


 Version 2 not supported. If you don't specify a version as above you get v2 of Tensorflow!
```
python3 -m pip install --upgrade --force-reinstall tensorflow --user
```



## Docker

run -it -p 8888:8888 tensorflow/tensorflow


Inspiration from here : https://www.youtube.com/watch?v=QfNvhPx5Px8


https://www.reddit.com/r/MachineLearning/comments/4f1gjk/how_do_i_run_the_tensorflow_docker_image_without/
How do I run the tensorflow docker image without jupyter notebook?!?!
If you want, for example, to run a bash shell just put /bin/bash at the end of your docker run command, e.g.:

docker run -it gcr.io/tensorflow/tensorflow /bin/bash
