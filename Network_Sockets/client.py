"""
A network socket is an internal endpoint for sending or receiving data within
a node on a computer network.
"""
import socket

# CREATE A SOCKET
try:
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Address family: AF_INET, version IPv4
    # Type: SOCK_STREAM, connection oriented TCP (Transmission Control Protocol)
    print("Socket created.", type(my_socket))
except socket.error as e:
    print(f"Failed to create socket. Error: {e}")
    raise e

# CONNECT TO A SERVER - for remote servers, we need IP address and port number
# to connect to
host = "www.google.com"

# Getting the IP address
try:
    # Returns the remote host's IP address by url name
    remote_ip = socket.gethostbyname(host)
    print(f"IP address of {host} is {remote_ip}.")
except socket.gaierror:
    print("Hostname could not be resolved.")
    raise

# Connect to remote server through port
port = 80  # Port 80 is the default port for HTTP
# Port 443 is the default port for HTTPS

my_socket.settimeout(3)  # Timeout (sec) before blocking socket operations,
# otherwise it may hang if it cannot connect

try:
    # socket.connect((@ip_address, @port_number))
    my_socket.connect((remote_ip, port))

    # Display the address where the socket is currently connected from
    print("Socket from address: {}".format(my_socket.getsockname()))

    # A pipe is connecting socket.getsockname() to socket.getpeername()

    # Display the address where the socket is currently connected to - socket
    # endpoint
    print("Is connected to address: {}".format(my_socket.getpeername()))

except socket.error:
    print("Timeout exceeded, cannot connect to remote host.")
    raise

print(f"Socket connected to {host} on IP {remote_ip} on port {port}.")

# SENDING DATA
# Message must be bytes type
msg = b'GET / HTTP/1.1\r\n\r\n'  # HTTP 'command' to fetch the main page of a
# website

try:
    my_socket.sendall(msg)
    print(f"Message {msg} sent successfully.")
except socket.error:
    print("Send failed.")
    raise

print("=" * 30)

# RECEIVING DATA
# socket.recv(@bufsize) - @bufsize maximum of data received at once
reply = my_socket.recv(2048)  # It's also a bytes string
print(f"Response:\n{reply}")

# Closing the socket
my_socket.close()
# It is a good practice to use the context manager (with) when working with
# sockets
