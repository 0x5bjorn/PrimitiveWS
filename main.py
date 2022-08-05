import time
import signal

from primitive_server import PrimServer

# Define host and port
SERVER_ADDRESS = (SERVER_HOST, SERVER_PORT) = ('', 8888)

web_server = PrimServer(SERVER_ADDRESS)

# Start web server: set up signal handler for SIGINT, SIGTERM signals
def start():
    signal.signal(signal.SIGINT, stop)      # interrupt signal
    signal.signal(signal.SIGTERM, stop)     # terminate signal

# Stop web server: signal handler to shutdown server
def stop(signum, _):
    signame = signal.Signals(signum).name
    print("\n" + time.asctime(), f"- Received signal {signame}. Shutting down...")
    web_server.shutdown()
    exit(0)

if __name__ == '__main__':
    start()
    web_server.run()
