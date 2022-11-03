
### Hummingboard2
``` 
https://wiki.solid-run.com/lib/exe/fetch.php?media=imx6:hummingboard:docs:sr-imx6-hummingboard-edge-datasheet.pdf

https://developer.solid-run.com/knowledge-base/hummingboard-gate-edge-getting-started/




    link/ether da:91:08:24:4f:f5 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.119/24 brd 192.168.1.255 scope global eth0


Jumpers for boot select
https://solidrun.atlassian.net/wiki/spaces/developer/pages/286621835/HummingBoard+Edge+Gate+Boot+Jumpers

```


#Hummingboard pulse 1

```bash
https://developer.solid-run.com/knowledge-base/hummingboard-pulse-getting-started/

https://www.solid-run.com/embedded-industrial-iot/nxp-i-mx8-family/imx8-som/

https://www.solid-run.com/wp-content/uploads/2020/09/i.MX8-SOM-front-large-960x430.png

```

```bash

apt-get update
apt-get install lightdm xfce4

sudo nano /etc/lightdm/lightdm.conf
```

Add this to the "/etc/lightdm/lightdm.conf" file
```
[SeatDefaults]
allow-guest=false
user-session=xfce
```
From : https://www.configserverfirewall.com/ubuntu-linux/install-desktop-on-ubuntu-server/


To enable x at startup time you can use:
```bash
sudo systemctl enable graphical.target --force
sudo systemctl set-default graphical.target
```

And to disable it
```bash
sudo systemctl enable multi-user.target --force
sudo systemctl set-default multi-user.target
```
From : https://unix.stackexchange.com/questions/520045/startx-not-automatically-running-on-reboot
