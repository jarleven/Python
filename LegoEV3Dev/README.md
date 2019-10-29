
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

