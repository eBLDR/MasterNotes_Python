import socket

HOST = ''  # Symbolic name meaning all available interface, it could be any IP
PORT = 8888  # Arbitrary non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    print('Socket created.')

    # Binding a socket to a particular address and port, by doing this we
    # ensure that all incoming data which is directed towards that port number
    # is received by this application
    # Only one socket can be bound to each port (generally)
    try:
        server.bind((HOST, PORT))
        print('Socket bind to port {} complete.'.format(PORT))
    except socket.error as e:
        print('Bind failed. Error: {}'.format(e))
        raise e

    # Listen for incoming connections
    # socket.listen(@backlog) - @backlog specifies the number of accepted
    # connections that the system will allow before refusing new connections
    server.listen(10)
    print('Socket is now listening.')

    """
    At this point, we can use telnet package (linux) as a client for sending a
    msg to the server; i.e.: telnet localhost <port_number>
    """

    # Waiting and accepting the incoming connection from the client
    # First value returned is the connection/channel (socket object) from the
    # server to the incoming client, the second is the client's address bound
    # to the socket on the client's end
    connection, address = server.accept()
    print('Connected with {}.'.format(address))

    # Communicate with the client
    data = connection.recv(1024)  # Server reads client message
    print('Server has received msg: {}, server is echoing it.'.format(data))

    connection.sendall(data)  # Server replies to client with a simple echo

    connection.close()

    # LIVE SERVER - a server that will be alive always
    # Create and bind the socket, put it to listen, and then proceed with the
    # code below...
    while True:
        conn, addr = server.accept()  # Accept new incoming connection
        print('Connected with {}.'.format(address))
        data = conn.recv(1024)

        # Just to close the server from the client - don't use this on real cases
        if data == b'\r\n':
            print('Got key message. Server is shutting down.')
            break

        print('Server has received msg: {}, server is echoing it.'.format(
            data
        ))
        reply = b'ECHO...' + data
        conn.sendall(reply)

        # Closing client connection after data is sent - if desired
        conn.close()
