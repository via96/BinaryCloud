import socket
import json
import os

sock = socket.socket()
print('start')
sock.connect(('localhost', 9090))
print('connect')
sock.send('hello world!'.encode())

data = sock.recv(1024)
print(str(data))
sock.close()

print(data)

dirPath = ''
fileMap = {}


def InitDir():
    file = open('.sets', 'w+')
    info = file.readlines()
    if len(info) > 0:
        dirPath = info[0]
        if len(info) > 1:
            fileMap = json.dumps(info[1])
    file.close()


