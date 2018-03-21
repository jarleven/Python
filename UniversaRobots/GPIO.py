import socket
import time

TCP_IP = '192.168.1.114'
TCP_PORT = 30002
BUFFER_SIZE = 1024


while True:
    
    for i in range(0,100):
    
        MESSAGE = "set_analog_out(0,%.2f)\r\n" % (i/100)
                
        print(MESSAGE)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE.encode('utf-8'))
        data = s.recv(BUFFER_SIZE)
        s.close()

        print("received data:", data)
    
        time.sleep(2)
        
