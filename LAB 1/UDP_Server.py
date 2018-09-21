# UDP Protocol Server

import socket

HOST = socket.gethostname()         # localhost
PORT = 12345                        # Port to listen on

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST, PORT))

while True:
    data, addr = s.recvfrom(1024)
    num = int(data.decode())

    print("Message from Client:", num)

    if num % 2 == 0:
        res = 'The number you entered is EVEN'
    else:
        res = 'The number you entered is ODD'

    s.sendto(res.encode(), addr)
