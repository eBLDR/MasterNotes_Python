"""
TCP Chat Server

Server tasks:
    1. Accept multiple incoming connections for client.
    2. Read incoming messages from each client and broadcast them to all other connected clients.
"""
import socket
import threading


def client_thread(conn, addr):
    client_connected(conn, addr)
    while True:
        data = conn.recv(RECV_BUFFER)
        if not data:
            # Received 0 bytes, connection on the other side has closed
            client_disconnected(conn, addr)
            break
        else:
            msg = '\r<{}> {}'.format(str(conn.getpeername()), data.decode(ENCODING)).replace('\n', '')
            broadcast_data(conn, msg)


def client_connected(conn, addr):
    CONNECTION_LIST_LOCK.acquire()
    CONNECTION_LIST.append(conn)
    print('Client {} connected.'.format(addr))
    broadcast_data(conn, '\rUser {} has entered the room.'.format(addr))
    CONNECTION_LIST_LOCK.release()


def client_disconnected(conn, addr=''):
    CONNECTION_LIST_LOCK.acquire()
    CONNECTION_LIST.remove(conn)
    print('Client {} disconnected.'.format(addr))
    broadcast_data(conn, '\rUser {} has left the room.'.format(addr))
    conn.close()
    CONNECTION_LIST_LOCK.release()


def broadcast_data(producer_socket, msg):
    # Broadcasts the message to all clients except the master socket (server) and the producer
    for sock in CONNECTION_LIST:
        if sock != producer_socket and sock != server_socket:
            try:
                sock.sendall(msg.encode(ENCODING))
            except Exception:
                # Socket connection broken, user may have pressed Ctrl+C
                client_disconnected(sock)
                raise


if __name__ == '__main__':
    HOST = '127.0.0.1'  # Localhost
    PORT = 5000
    MAX_CLIENTS = 10
    RECV_BUFFER = 4096
    ENCODING = 'utf-8'

    CONNECTION_LIST = []
    CONNECTION_LIST_LOCK = threading.Lock()  # To avoid concurrency issues

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            server_socket.bind((HOST, PORT))
        except socket.error as e:
            print('Bind failed. Error: {}'.format(e))
            raise e

        server_socket.listen(MAX_CLIENTS)

        CONNECTION_LIST.append(server_socket)

        print('Chat server started on {}.'.format(server_socket.getsockname()))

        while True:
            connection, address = server_socket.accept()
            threading.Thread(target=client_thread, args=(connection, address)).start()
