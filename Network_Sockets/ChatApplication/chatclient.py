"""
Telnet is a protocol used on the Internet or local area network to provide a bidirectional interactive text-oriented
communication facility using a virtual terminal connection.

Client tasks:
    1. Listen for incoming messages from the server.
    2. Check user input. If the user types in a message then send it to the server.
"""
import socket
import sys
import select


def prompt(conn):
    sys.stdout.write('<You> '.format(conn.getsockname()))
    sys.stdout.flush()


def incoming_message(conn):
    # Incoming messages from remote host
    data = conn.recv(4096)
    if data:
        print(data.decode('utf-8'))
        prompt(conn)


def send_message(conn):
    # Sending messages to remote host
    data = sys.stdin.readline().encode('utf-8')
    conn.sendall(data)
    if b'/exit' in data:
        # Exiting keyword
        conn.close()
        sys.exit()
    prompt(conn)


if __name__ == '__main__':

    if len(sys.argv) < 3 or not sys.argv[2].isdigit():
        print('Usage: python chatclient.py hostname port')
        sys.exit()

    host, port = sys.argv[1], int(sys.argv[2])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.settimeout(2)

        try:
            client_socket.connect((host, port))
            print('Connected to remote host.')
            prompt(client_socket)
        except socket.error:
            print('Unable to connect to {}:{}.'.format(host, port))
            raise

        while True:
            socket_list = [sys.stdin, client_socket]
            ready_to_read, ready_to_write, in_error = select.select(socket_list, [], [])
            """
            select.select(@rlist, @wlist, @xlist[, @timeout]) takes three sequences of 'waitable objects' as arguments:
                @rlist, wait until ready for reading
                @wlist: wait until ready for writing
                @xlist: wait for an 'exceptional condition'
            
            The return value is a triple of lists of objects that are ready: subsets of the first three arguments.
            The optional @timeout specifies a time-out as a floating point number in seconds. When the timeout argument
            is omitted the function blocks until at least one file descriptor (i.e.: file object, socket) is ready.
            """

            for sock in ready_to_read:
                if sock == client_socket:
                    # Incoming message from remote server
                    incoming_message(sock)
                else:
                    # User entered a message
                    send_message(client_socket)
