# TCP Protocol Client

import socket                           # Import socket module

HOST = socket.gethostname()             # localhost
PORT = 12345                            # Port to listen on

num = str(input("Enter a number: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(num.encode())
    data = s.recv(1024)

print('Message from Server:', data.decode())
s.close()