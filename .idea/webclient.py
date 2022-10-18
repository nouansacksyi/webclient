#import socket module
from socket import *
import sys # for arguments
host = sys.argv[1]
port = int(sys.argv[2])
filename = sys.argv[3]
# Create client socket
#Fill in start
s = socket(socket.AF_INET, socket.SOCK_STREAM)
#Fill in end
print('Waiting for connection')
try:
    #connect to the Server Socket
    #Fill in start
    s.connect((host , port))
    #Fill in end
except socket.error as e:
    print(str(e))
# send HTTP GET request
#Fill in start
print('# Sending data to server')
request = "GET / HTTP/1.0\r\n\r\n"
#Fill in end
#receive the header and print it out
#Fill in start
print('# Receive data from server')
reply = s.recv(1024)
#Fill in end
# output message body
message = ""
while message.find("</html>") < 0:
    #Fill in start
    print("Hello World!")
    #Fill in end

start = message.find("<body>")+6
end = message.find("</body>")
print(message[start:end:1])
ClientSocket.close()