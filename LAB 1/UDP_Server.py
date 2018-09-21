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

    if num > 1:
                for i in range(2,num):
                    if (num % i) == 0:
                        res = ("%d is not a prime number" %num)
                        break
                    else:
                        res = ("%d is a prime number" %num)
    else:
        res = ("%d is not a prime number" %num)
    s.sendto(res.encode(), addr)
