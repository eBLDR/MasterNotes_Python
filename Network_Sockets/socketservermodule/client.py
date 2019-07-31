import socket
import sys

usage_msg = 'Usage: client.py <port> <msg> <msg> ...'

try:
    HOST, PORT = 'localhost', int(sys.argv[1])
except (IndexError, ValueError):
    print(usage_msg)
    sys.exit()

data = ' '.join(sys.argv[2:])

if not data:
    print(usage_msg)
    sys.exit()

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + '\n', 'utf-8'))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), 'utf-8')

print('Sent:     {}'.format(data))
print('Received: {}'.format(received))
