# UDP Protocol Client

# Import socket module
import socket

# localhost
HOST = socket.gethostname()             

# Port to listen on, this must be the same for client and server
PORT = 12345

# Take input from user
num = str(input("Enter a number: "))

# Set up connection type using AF_INET for socekt programming and SOCK_DGRAM for a UDP connection
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Try sending message to server
try:
    # Send num to address
    s.sendto(num.encode(), (HOST, PORT))

    # Receive the data from the server
    data, addr = s.recvfrom(1024)

    # Print message from the server
    print('Message from Server:', data.decode())

finally:
    # Close socket
    s.close()
