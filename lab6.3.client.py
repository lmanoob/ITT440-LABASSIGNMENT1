import socket

ClientSocket = socket.socket()
host = '192.168.50.164'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
while True:
    Input2 = input('Function(sqrt/cos/log): ')
    ClientSocket.send(str.encode(Input2))
    Input1 = input('Number 1: ')
    ClientSocket.send(str.encode(Input1))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()
