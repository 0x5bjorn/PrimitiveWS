from primitive_server import PrimServer

# Define host and port
SERVER_ADDRESS = (SERVER_HOST, SERVER_PORT) = ('', 8888)

if __name__ == '__main__':
    web_server = PrimServer(SERVER_ADDRESS)
    try:
        web_server.serve()
    except KeyboardInterrupt:
        pass
