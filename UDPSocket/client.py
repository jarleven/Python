import socket

UDP_IP = "192.168.1.240"
UDP_PORT = 6789
MESSAGE = "Hello World"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT )
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))
