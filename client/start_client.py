import socket
import json
import os
import sys
from enum import Enum


class Commands(Enum):
    EMPTY = 0
    CHANGE_STATE = 1
    NO_CHANGE = 2
    UPDATE = 3


cmd_dict = { Commands.EMPTY: 'EMPTY'.encode(), Commands.CHANGE_STATE: 'CHANGE_STATE'.encode(), Commands.NO_CHANGE: 'NO_CHANGE'.encode(), Commands. UPDATE: 'UPDATE'.encode() }


def cmd_encode(cmd):
    return cmd_dict[cmd]


def cmd_decode(cmd_str):
    for k, v in cmd_dict.items():
        if v == cmd_str:
            return k


sock = socket.socket()
print('start')
sock.connect(('localhost', 9090))
print('connect')
# sock.send('hello world!'.encode())
sock.send(cmd_encode(Commands.EMPTY))
data = sock.recv(1024)
print(cmd_decode(data))
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
