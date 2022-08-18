import socket
import time

class PrimServer:

    # Type of addresses (IPv4 addresses)
    address_family = socket.AF_INET
    # TCP connection
    socket_type = socket.SOCK_STREAM

    # Number of connection requests hold in a queue 
    # which is used by the operating system to store connections 
    # that have been accepted by the TCP stack but not, yet, by server
    conn_number = 3

    def __init__(self, server_address: tuple=None):
        # Create and set up listening socket
        self.server_socket = socket.socket(
            self.address_family,
            self.socket_type
        )
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if server_address:
            self.server_socket.bind(server_address)
            self.server_socket.listen(self.conn_number)
            print(time.asctime(), f"- Serving/listening on {self.server_socket.getsockname()}...")

    def setup(self, server_address):
        # Set up listening socket
        self.server_socket.bind(server_address)
        self.server_socket.listen(self.conn_number)
        print(time.asctime(), f"- Serving/listening on {self.server_socket.getsockname()}...")
        
        return self.server_socket

    def __del__(self):
        # Close socket after finishing using webserver
        if self.server_socket.fileno() != -1:
            print("\n" + time.asctime(), f"- Server stops on {self.server_socket.getsockname()}")
            self.server_socket.close()

    def shutdown(self):
        # Close socket after finishing using webserver
        if self.server_socket.fileno() != -1:
            print("\n" + time.asctime(), f"- Server stops on {self.server_socket.getsockname()}")
            self.server_socket.close()
