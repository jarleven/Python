import rpyc

# Remote Python Call   RPyC (pronounced are-pie-see)

conn = rpyc.classic.connect('192.168.137.3')    # host name or IP address of the EV3
ev3 = conn.modules['ev3dev.ev3']                # import ev3dev.ev3 remotely

ev3.Sound.speak('Luke Im your father').wait()

