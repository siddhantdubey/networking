import socket
import json

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8080)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)

        # Receive the data in small chunks
        data = ''
        while True:
            chunk = connection.recv(16)
            data += chunk.decode()
            if '\r\n\r\n' in data or not chunk:
                break

        print('received {!r}'.format(data))

        # Prepare a response with the received data in json format
        response = json.dumps({"received_request": data})

        http_response = f"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: {len(response)}\r\n\r\n{response}"
        connection.sendall(http_response.encode())

    finally:
        # Clean up the connection
        connection.close()
