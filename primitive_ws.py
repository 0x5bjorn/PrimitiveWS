import socket

# Define host and port
SERVER_ADDRESS = (SERVER_HOST, SERVER_PORT) = ('', 8888)
# Define connection number of unaccepted connections
# that the system will allow before refusing new connections
# and maximum amount of data to be received at once
CONN_NUMBER, RECV_BUFFER = 3, 1024

def init_server():
    # Create and set up listening socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(SERVER_ADDRESS)
    server_socket.listen(CONN_NUMBER)

def handle_request():
    # Get the client request
    request = client_connection.recv(RECV_BUFFER).decode('utf-8')
    print(request)

    # Send HTTP response
    response = "Hello, World!\n"
    client_connection.sendall(response.encode())

def serve():
    init_server()

    print(f'Serving/listening on port {SERVER_PORT} ...')
    while True:
        # Wait for client connections
        client_connection, client_addr = server_socket.accept()
        handle_request()
        client_connection.close()

if __name__ == '__main__':
    serve()
    # Close socket
    server_socket.close()
