import socket
from enum import Enum

class Commands(Enum):
    EMPTY = 0
    CHANGE_STATE = 1
    NO_CHANGE = 2
    UPDATE = 3

sock = socket.socket()
print('start')
sock.bind(('', 9090))
print('connect')
sock.listen(1)
conn, addr = sock.accept()

print('connected:' + str(addr))

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()