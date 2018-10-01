# UDP Protocol Server

# Import socket module
import socket

# localhost
HOST = socket.gethostname()             

# Port to listen on, this must be the same for client and server
PORT = 12345           

# Set up connection type using AF_INET for socekt programming and SOCK_STREAM for a TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address
s.bind((HOST, PORT))

while True:
    # Receive data from client
    data, addr = s.recvfrom(1024)
    
    # Store data received in num variable
    num = int(data.decode())

    # Print the data received
    print("Message from Client:", num)

    # The following algorithm determins if num is a prime number or not
    if num > 1:
                for i in range(2,num):
                    if (num % i) == 0:
                        res = ("%d is not a prime number" %num)
                        break
                    else:
                        res = ("%d is a prime number" %num)
    else:
        res = ("%d is not a prime number" %num)
    
    # Send back result of algorithm
    s.sendto(res.encode(), addr)
