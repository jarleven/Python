#### Not really Python but general Linux stuff



## Framebuffer / remote display images
```bash

chvt 1

# parameters
#  -a Auto zoom
#  -t slideshow time


sudo  fbi -a -d /dev/fb0 -T 1 myPicture.png

# slideshow
sudo fbi -a -t 10 *.png -d /dev/fb0 -T 1

```

## Framebuffer video player
```bash


```

## 
```bash

sudo openvt -s -- cmatrix

sudo openvt -s -- ls -al



cowsay "Hei"

cowsay "Hei" > kuseier.txt

cat kuseier.txt

sudo openvt -s -- cat kuseier.txt


cowsay "Hei" > kuseier.txt && sudo openvt -s -- cat kuseier.txt


date

date | cowsay



```




```bash

```
