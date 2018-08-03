"""
A network socket is an internal endpoint for sending or receiving data within a node on a computer network.
An Internet Protocol address (IP address) is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication.

Client, a system that connects to a remote system to fetch data. Client workflow:
    1. Create a socket
    2. Connect to remote server
    3. Send some data
    4. Receive a reply
"""
import socket

# CREATE A SOCKET
try:
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Address family: AF_INET, version IPv4
    # Type: SOCK_STREAM, connection oriented TCP (Transmission Control Protocol)
    print('Socket created.', type(my_socket))
except socket.error as e:
    print('Failed to create socket. Error: {}'.format(e))
    raise e

# CONNECT TO A SERVER - for remote servers, we need IP address and port number to connect to
host = 'www.google.com'

# Getting the IP address
try:
    # Returns the remote host's IP address by url name
    remote_ip = socket.gethostbyname(host)
    print('IP address of {} is {}.'.format(host, remote_ip))
except socket.gaierror:
    print('Hostname could not be resolved.')
    raise

# Connect to remote server through port
port = 80  # Port 80 is the default port for HTTP
# Port 443 is the default port for HTTPS

my_socket.settimeout(3)  # Timeout (sec) before blocking socket operations, otherwise it may hang if it cannot connect

try:
    # socket.connect((@ip_address, @port_number))
    my_socket.connect((remote_ip, port))

    # Display the address where the socket is currently connected from
    print('Socket from address: {}'.format(my_socket.getsockname()))

    # A pipe is connecting socket.getsockname() to socket.getpeername()

    # Display the address where the socket is currently connected to - socket endpoint
    print('Is connected to address: {}'.format(my_socket.getpeername()))

except socket.error:
    print('Timeout exceeded, cannot connect to remote host.')
    raise

print('Socket connected to {} on IP {} on port {}.'.format(host, remote_ip, port))

# SENDING DATA
# Message must be bytes type
msg = b'GET / HTTP/1.1\r\n\r\n'  # HTTP 'command' to fetch the main page of a website

try:
    my_socket.sendall(msg)
    print('Message {} sent successfully.'.format(msg))
except socket.error:
    print('Send failed.')
    raise

print('=' * 30)

# RECEIVING DATA
# socket.recv(@bufsize) - @bufsize maximum of data received at once
reply = my_socket.recv(2048)  # It's also a bytes string
print('Response:\n{}'.format(reply))

# Closing the socket
my_socket.close()
# It is a good practice to use the context manager (with) when working with sockets
