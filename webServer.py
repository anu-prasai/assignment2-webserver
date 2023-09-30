# import socket module
from socket import *
import sys 
#socket=one endpoint of a two-way communication link between two programs running on the network
def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM) #in this line - we have made a socket instance and passed it two parameters, AF_INET = address-family ipv4 and SOCK_STREAM= connection oriented TCP protocol
    # Prepare a server socket
    serverSocket.bind(("", port)) #bind() method allows the server to bind to a specific IP and port so it can listen to incoming request ; empty parameters on bind lets you bind to all IP address
    # Fill in start
    serverSocket.listen(1) #put the socket in listening mode, 1 here means that only one connection here is kept waiting; if a 2nd connection tries to bind, it will be refused
    # Fill in end

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
                         
        try:
            message = connectionSocket.recv(1024) #recieve 1024 bytes of data from the client
            filename = message.split()[1]
            # opens the client requested file which would be helloworld.html file
            # Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
            f = open(filename[1:],"rb")
            #print(f)
            content=f.read()
            #print(content)
            f.close()
            #outputdata=b"Content-Type: text/html; charset=UTF-8\r\n"
            connectionSocket.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nConnection: keep-alive\r\nServer: Windows\r\n\r\n')
            #connectionSocket.send(b"Content-Type: text/html; charset=UTF-8\r\n\r\n")
            #connectionSocket.send(b"Connection: keep-alive\r\n\r\n")
            #connectionSocket.send(b"Server: Windows\r\n\r\n")
            # Fill in start -This variable can store your headers you want to send for any valid or invalid request.
            # Content-Type above is an example on how to send a header as bytes
            # Fill in end
            connectionSocket.send(content)
            # Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok?
            # Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
            # Fill in start

            # Fill in end

            # Send the content of the requested file to the client
            #for i in f: # for line in file

            #print("hello")
            connectionSocket.close()

        except Exception as e:
            errormessage = b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\nConnection: keep-alive\r\nServer: Windows\r\n"
            connectionSocket.send(errormessage)
            connectionSocket.close()
             # Close client socket
            # Fill in start

            # Fill in end

    # Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
    # serverSocket.close()
    # sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
