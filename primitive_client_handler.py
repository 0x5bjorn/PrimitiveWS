import socket
import time

class PrimClientHandler:

    is_stopped = False

    # Maximum amount of data to be received at once
    recv_buffer = 1024

    # def __init__(self, server_socket):

    def shutdown(self):
        self.is_stopped = True

    def run(self, server_socket: socket.socket):
        print(time.asctime(), f"- Accepting connections...")
        while not self.is_stopped:
            # Wait for client connections
            self.client_connection, client_addr = server_socket.accept()
            self.handle_request()
            self.client_connection.close()

    def handle_request(self):
        # Get the client request
        request = self.client_connection.recv(self.recv_buffer).decode()
        print(request)

        # Send HTTP response
        response = f'''HTTP/1.1 200 OK
                        Date: {time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.localtime())}
                        Server: Primitive server v1.0

                        Hello, World!
                    '''

        self.client_connection.sendall(response.encode())