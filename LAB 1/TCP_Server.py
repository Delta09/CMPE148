# TCP Protocol Server

import socket

HOST = socket.gethostname()         # localhost
PORT = 12345                        # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Got connection from', addr)
        while True:
            data = conn.recv(1024)

            if not data:
                break

            num = int(data.decode())

            print("Message from Client:", num)

            if num % 2 == 0:
                res = 'The number you entered is EVEN'
            else:
                res = 'The number you entered is ODD'
            conn.send(res.encode())