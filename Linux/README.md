#### Not really Python but general Linux stuff


## Download on the commandline
```bash

sudo useradd -m username


```

## Download on the commandline
```bash

wget "https://www.digi.no/?module=TekComics&service=image&id=dilbert&key=2022-10-26" -O dilbert.png

curl -JLO "https://www.digi.no/?module=TekComics&service=image&id=dilbert&key=2022-10-26" -o dilbert.png

```

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



### Crontab
```bash

@reboot (. ~/.profile; /usr/bin/screen -dmS YouTube ~/stream_file.sh)

# Note this must be in the root crontab (sudo crontab -e)
0 7 * * * /sbin/shutdown -r now



```



