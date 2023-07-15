import socket
import sys

HOST = '127.0.0.1'
PORT = 3450

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        sys.stdout.write(conn, addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
print('done')
