# TCP Protocol Client

# Import socket module
import socket

# localhost
HOST = socket.gethostname()             

# Port to listen on, this must be the same for client and server
PORT = 12345                            

#Take input from user
num = str(input("Enter a number: "))

#Set up connection type using AF_INET for socekt programming and SOCK_STREAM for a TCP connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    
    #Start connection with server
    s.connect((HOST, PORT))
    
    #Send encoded message
    s.send(num.encode())
    
    #Receive/Listen to message from Server
    data = s.recv(1024)

#Display message from server
print('Message from Server:', data.decode())

#Close connection
s.close()