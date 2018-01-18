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
    CONNECT = 4
    DISCONNECT = 5


cmd_dict = { Commands.EMPTY: 'EMPTY'.encode(), Commands.CHANGE_STATE: 'CHANGE_STATE'.encode(), Commands.NO_CHANGE: 'NO_CHANGE'.encode(),
             Commands. UPDATE: 'UPDATE'.encode(), Commands.CONNECT: 'CONNECT'.encode(), Commands.DISCONNECT: 'DISCONNECT'.encode() }


def cmd_encode(cmd):
    return cmd_dict[cmd]


def cmd_decode(cmd_str):
    for k, v in cmd_dict.items():
        if v == cmd_str:
            return k


def connect(addr, port):
    sock.connect((addr, port))
    print('connect')


sock = socket.socket()
print('start')
# connect('localhost', 9090)
# sock.send('hello world!'.encode())
while True:
    dial = input()
    if dial == 'e':
        connect('localhost', 9090)
        sock.send(cmd_encode(Commands.EMPTY))
        sock.close()
    if dial == 'u':
        connect('localhost', 9090)
        sock.send(cmd_encode(Commands.UPDATE))
        sock.close()
    if dial == 'd':
        connect('localhost', 9090)
        sock.send(cmd_encode(Commands.DISCONNECT))
        sock.close()
        break
    data = sock.recv(1024)
    print(cmd_decode(data))
