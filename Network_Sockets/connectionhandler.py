import socket
import threading

HOST = ''  # Symbolic name meaning all available interface
PORT = 8880  # Arbitrary non-privileged port


def client_thread(conn, addr):
    # Handles the connection
    print('Connected with {}.'.format(address))
    conn.send(b'Welcome to the server. Type something and hit enter (EXIT for stop connection)\n')
    while True:
        # Communication between client and server
        data = conn.recv(1024)
        reply = b'ECHO...' + data
        print('Server has received msg: {} from {}, server is echoing it.'.format(data, addr))
        conn.sendall(reply)
        if data == b'EXIT\r\n':
            break
    # Close connection when all tasks are done
    conn.close()
    print('Client {} has disconnected.'.format(addr))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    print('Server created.')

    try:
        server.bind((HOST, PORT))
        print('Socket bind to port {} complete.'.format(PORT))
    except socket.error as e:
        print('Bind failed. Error: {}'.format(e))
        raise e

    server.listen(10)
    print('Server is now listening.')

    while True:
        connection, address = server.accept()

        # Start the new thread for the connection
        threading.Thread(target=client_thread, args=(connection, address)).start()
