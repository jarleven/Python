
### Hummingboard2
``` 
https://wiki.solid-run.com/lib/exe/fetch.php?media=imx6:hummingboard:docs:sr-imx6-hummingboard-edge-datasheet.pdf

https://developer.solid-run.com/knowledge-base/hummingboard-gate-edge-getting-started/




    link/ether da:91:08:24:4f:f5 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.119/24 brd 192.168.1.255 scope global eth0

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


