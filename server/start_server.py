import socket
from enum import Enum
from server.directory import Directory

FILEPATH = '/home/developer/develop/Projects/libs(backup)/'


client_dict = {}
dir = Directory(FILEPATH)
dir.update()


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



while True:
    conn, addr = sock.accept()
    client_dict[addr] = conn
    print('connected:' + str(addr))

    for cl_addr, cl_conn in client_dict.items():
        data = cl_conn.recv(1024)
        print(str(data))
    conn.close()

    # if not data:
    #     print('not data')
    #     break
    # conn.send(data.upper())

# conn.close()