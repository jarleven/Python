
### Hummingboard2
``` 
https://wiki.solid-run.com/lib/exe/fetch.php?media=imx6:hummingboard:docs:sr-imx6-hummingboard-edge-datasheet.pdf

https://developer.solid-run.com/knowledge-base/hummingboard-gate-edge-getting-started/




    link/ether da:91:08:24:4f:f5 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.119/24 brd 192.168.1.255 scope global eth0


Jumpers for boot select
https://solidrun.atlassian.net/wiki/spaces/developer/pages/286621835/HummingBoard+Edge+Gate+Boot+Jumpers

```


### Hummingboard pulse 1

```bash
https://developer.solid-run.com/knowledge-base/hummingboard-pulse-getting-started/

https://www.solid-run.com/embedded-industrial-iot/nxp-i-mx8-family/imx8-som/

https://www.solid-run.com/wp-content/uploads/2020/09/i.MX8-SOM-front-large-960x430.png

# Software :
https://images.solid-run.com/IMX8?_ga=2.248711047.1409348554.1667298511-46829973.1667298511

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



### PICO-PI REV:B1
```bash

https://www.technexion.com/products/system-on-modules/pico/pico-imx7/


https://www.nxp.com/docs/en/user-guide/PICO-IMX7UL-USG.pdf

https://forum.digikey.com/t/debian-getting-started-with-the-pico-pi-imx7/12429

https://www.hackster.io/85787/pico-pi-and-yocto-project-7fa6ac


https://gist.github.com/liquidx/fd1002ec870a7c13f04a0b8a44744246

Disk images:
https://download.technexion.com/demo_software/PICO/IMX7/pico-imx7-emmc/

```
