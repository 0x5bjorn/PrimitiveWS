import queue
import socket
import time
import threading

class PrimRequestHandler:

    is_stopped = False

    # Maximum amount of data to be received at once
    recv_buffer = 1024

    # Number of threads
    thread_number = 5
    # Send a signal to threads to exit
    # Use thread safe solution for signaling like threading.Event()
    thread_exit_signal = threading.Event()

    # Request queue size
    queue_size = 5
    
    def __init__(self):
        self.request_queue = queue.Queue(maxsize=self.queue_size)
        threads = [threading.Thread(target=self.handle_request) for t in range(self.thread_number)]
        for t in threads:
            t.start()
                
    def shutdown(self):
        self.is_stopped = True
        self.thread_exit_signal.set()

    def run(self, server_socket: socket.socket):
        print(time.asctime(), f"- Accepting connections...")
        while not self.is_stopped:
            # Wait for client connections
            client_socket, _ = server_socket.accept()
            try:
                self.request_queue.put(client_socket)
            except queue.Full:
                # TODO: handle excpetion
                pass

    def handle_request(self):
        while not self.thread_exit_signal.is_set():
            try:
                # Get the client request
                client_socket = self.request_queue.get(block=True, timeout=1)
                request = client_socket.recv(self.recv_buffer).decode()
                print(request)

                # Send HTTP response
                response = f'''HTTP/1.1 200 OK
                                Date: {time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.localtime())}
                                Server: Primitive server v1.0

                                Hello, World!
                            '''

                client_socket.sendall(response.encode())
                client_socket.close()
            except queue.Empty:
                continue