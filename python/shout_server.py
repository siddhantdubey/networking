import socket

our_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
PORT = 12345
our_socket.bind(('', PORT))
print('Listening on port', PORT)
while True:
    data, add = our_socket.recvfrom(1024)
    shout = data.decode().upper()
    our_socket.sendto(shout.encode(), add)
