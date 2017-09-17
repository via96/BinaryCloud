import socket

sock = socket.socket()
print('start')
sock.connect(('localhost', 9090))
print('connect')
sock.send('hello world!'.encode())

data = sock.recv(1024)
print(str(data))
sock.close()

print(data)