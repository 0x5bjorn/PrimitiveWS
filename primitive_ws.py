import socket
import time

class PrimitiveWS:

    # Type of addresses (IPv4 addresses)
    address_family = socket.AF_INET
    # TCP connection
    socket_type = socket.SOCK_STREAM

    # Connection number of unaccepted connections
    # that the system will allow before refusing new connections
    conn_number = 3
    # Maximum amount of data to be received at once
    recv_buffer = 1024

    def __init__(self, server_address):
        # Create and set up listening socket
        self.server_socket = socket.socket(
            self.address_family,
            self.socket_type
        )
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(server_address)
        self.server_socket.listen(self.conn_number)

    def __del__(self):
        # Close socket after finishing using webserver
        self.server_socket.close()
        print("\n", time.asctime(), f"- Server Stops - {SERVER_HOST}:{SERVER_PORT}")

    def serve(self):
        print(time.asctime(), f"- Serving/listening on port {SERVER_PORT} ...")
        while True:
            # Wait for client connections
            self.client_connection, client_addr = self.server_socket.accept()
            self.handle_request()
            self.client_connection.close()

    def shut(self):
        # Close socket after finishing using webserver
        self.server_socket.close()
        print(time.asctime(), f"Server stops - {SERVER_HOST}:{SERVER_PORT}")

    def handle_request(self):
        # Get the client request
        request = self.client_connection.recv(self.recv_buffer).decode('utf-8')
        print(request)

        # Send HTTP response
        response = "Hello, World!\n"
        self.client_connection.sendall(response.encode())


# Define host and port
SERVER_ADDRESS = (SERVER_HOST, SERVER_PORT) = ('', 8888)

if __name__ == '__main__':
    web_server = PrimitiveWS(SERVER_ADDRESS)
    try:
        web_server.serve()
    except KeyboardInterrupt:
        pass
