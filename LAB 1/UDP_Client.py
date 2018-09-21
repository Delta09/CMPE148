# UDP Protocol Client

import socket                           # Import socket module

HOST = socket.gethostname()             # localhost
PORT = 12345                            # Port to listen on

num = str(input("Enter a number: "))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s.sendto(num.encode(), (HOST, PORT))

    data, addr = s.recvfrom(1024)
    print('Message from Server:', data.decode())

finally:
    s.close()
