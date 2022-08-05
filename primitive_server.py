import socket
import time

class PrimServer:

    is_stopped = False

    # Type of addresses (IPv4 addresses)
    address_family = socket.AF_INET
    # TCP connection
    socket_type = socket.SOCK_STREAM

    # Number of unaccepted connections
    # that the system will allow before refusing new connections
    conn_number = 3
    # Maximum amount of data to be received at once
    recv_buffer = 1024

    def __init__(self, server_address=None):
        # Create and set up listening socket
        self.server_socket = socket.socket(
            self.address_family,
            self.socket_type
        )
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if server_address:
            self.server_socket.bind(server_address)
            self.server_socket.listen(self.conn_number)

    def setup(self, server_address):
        # Set up listening socket
        self.server_socket.bind(server_address)
        self.server_socket.listen(self.conn_number)

    def __del__(self):
        # Close socket after finishing using webserver
        if self.server_socket.fileno() != -1:
            self.is_stopped = True
            print("\n" + time.asctime(), f"- Server stops on {self.server_socket.getsockname()}")
            self.server_socket.close()

    def shutdown(self):
        # Close socket after finishing using webserver
        if self.server_socket.fileno() != -1:
            self.is_stopped = True
            print("\n" + time.asctime(), f"- Server stops on {self.server_socket.getsockname()}")
            self.server_socket.close()

    def run(self):
        print(time.asctime(), f"- Serving/listening on {self.server_socket.getsockname()}...")
        while not self.is_stopped:
            # Wait for client connections
            print(self.server_socket.fileno())
            self.client_connection, client_addr = self.server_socket.accept()
            self.handle_request()
            self.client_connection.close()

    def handle_request(self):
        # Get the client request
        request = self.client_connection.recv(self.recv_buffer).decode('utf-8')
        print(request)

        # Send HTTP response
        response = "Hello, World!\n"
        self.client_connection.sendall(response.encode())