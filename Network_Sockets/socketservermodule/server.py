"""
socketserver module uses sockets module to simplify the task of
writing network servers.

Types of servers:
    - TCP Server
    - UDP Server
    - Unix Stream Server
    - Unix Datagram Server
"""
import socketserver
import sys


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print('{} wrote:'.format(self.client_address))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


if __name__ == '__main__':
    try:
        HOST, PORT = 'localhost', int(sys.argv[1])
    except (IndexError, ValueError):
        print('Usage: server.py <port>')
        sys.exit()

    # Create the server, binding to localhost on specific port
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        print('Server is active.')
        # Activate the server; this will keep it running until you
        # interrupt the program with Ctrl+C
        server.serve_forever()
