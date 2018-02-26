"""
    https://devhub.io/repos/UniPiTechnology-evok
"""

from jsonrpclib import Server

s=Server("http://192.168.1.233:8080/rpc")

for state in range(0,2):

    for i in range(1,9):
        s.relay_set(i,state)
        print(s.relay_get(i))

