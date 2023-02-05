# https://www.freecodecamp.org/news/text-box-in-html-the-input-field-html-tag/
# https://microcontrollerslab.com/raspberry-pi-pico-w-web-server-control-led/

# For more details and step by step guide visit: Microcontrollerslab.com
try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import gc
gc.collect()


ssid = '3DATA'
password = 'Vinter2022'


station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin('LED', Pin.OUT)
led_state = "OFF"

def web_page():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web form</title>
</head>
<body>
    <form action="/url" method="GET">
        <label>
            Please enter your username
            <input type="text" name="username" minlength="3" maxlength="20" required>
        </label>
        <button type="submit">Submit</button>  
    </form>
</body>
</html>"""
    
    
    
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    try:
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Received HTTP GET connection request from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        print("")
        print('GET Rquest Content = %s' % request)
        led_on = request.find('/url?username=')
        endpos = request.find(' HTTP/1.1')

        print("")
        print("USERNAME CONTAIN : %s " % led_on)
        
        a=len("/url?username=")
        print(request[led_on+a:endpos])
        
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')