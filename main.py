import time
import signal

from primitive_server import PrimServer
from primitive_request_handler import PrimRequestHandler

# Define host and port
SERVER_ADDRESS = (SERVER_HOST, SERVER_PORT) = ('', 8888)

server = PrimServer()
client_handler = PrimRequestHandler()

# Start web server: set up signal handler for SIGINT, SIGTERM signals
def start():
    signal.signal(signal.SIGINT, stop)      # interrupt signal
    signal.signal(signal.SIGTERM, stop)     # terminate signal

# Stop web server: signal handler to shutdown server
def stop(signum: int, _):
    signame = signal.Signals(signum).name
    print("\n" + time.asctime(), f"- Received signal {signame}. Shutting down...")
    client_handler.shutdown()
    server.shutdown()
    exit(0)

if __name__ == '__main__':
    start()
    server_socket = server.setup(SERVER_ADDRESS)
    client_handler.run(server_socket)

