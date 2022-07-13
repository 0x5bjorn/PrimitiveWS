import socket

# Define host and port
SERVER_HOST, SERVER_PORT = '', 8888

# Create and set up listening socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

print(f'Serving/listening HTTP on port {SERVER_PORT} ...')

while True:
    # Wait for client connections
    client_connection, client_addr = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode('utf-8')
    print(request)

    # Send HTTP response
    response = "Hello, World!\n"
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()
