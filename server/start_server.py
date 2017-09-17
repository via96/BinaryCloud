import socket

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