import socket
import threading

HOST = ''  # Symbolic name meaning all available interface
PORT = 8880  # Arbitrary non-privileged port


def client_thread(conn, addr):
    # Handles the connection
    print(f"Connected with {address}.")
    conn.send(b'Welcome to the server. Type something and hit enter '
              b'(EXIT for stop connection)\n')

    while True:
        # Communication between client and server
        data = conn.recv(1024)
        if not data:
            # Received 0 bytes, connection on the other side has closed
            break

        reply = b'ECHO...' + data
        print(f"Server has received msg: {data} from {addr}, "
              f"server is echoing it.")
        conn.sendall(reply)

    # Close connection when all tasks are done
    conn.close()
    print(f"Client {addr} has disconnected.")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    print("Server created.")

    try:
        server.bind((HOST, PORT))
        print(f"Socket bind to port {PORT} complete.")
    except socket.error as e:
        print(f"Bind failed. Error: {e}")
        raise e

    server.listen(10)
    print("Server is now listening.")

    while True:
        connection, address = server.accept()

        # Start the new thread for the connection
        threading.Thread(
            target=client_thread,
            args=(connection, address),
        ).start()
