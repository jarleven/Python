## A collection of what I have done on the Lego Ev3 using Ev3dev 
This is a simplified colection of things to try using Linux on an Ev3 in the classroom

* http://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/rpyc.html
* https://sites.google.com/site/ev3python/learn_ev3_python
* https://sites.google.com/site/ev3python/learn_ev3_python/rpyc
* http://www.ev3dev.org/docs/tutorials/setting-up-wifi-using-the-command-line/




```
Login : robot
Passord : maker
```

To start RPyC server on Ev3 Brick just run the "pyc_classic.py"

To enable wifi on the Ev3 run the following commands
```
robot@ev3dev:~$ connmanctl
connmanctl> enable wifi
connmanctl> scan wifi
connmanctl> services
connmanctl> agent on
connmanctl> connect wifi_*****
Passphrase? *************
connmanctl> quit
```


### ABC
* Download image file snapshot-ev3dev-buster-ev3-generic-2019-09-08.img.xz
* Brurn the image directly to an SD-Card using Balena Etcher  https://www.balena.io/etcher/
* Plug the SD-Card in your Ev3 brick
* Magic :-)
