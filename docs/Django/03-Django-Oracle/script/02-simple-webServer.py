# Importing everything (*) from the socket module.
from socket import *

# Function to create a server.
def createServer():
    # Create a socket object 'serversocket' using IPv4 addressing (AF_INET) and TCP protocol (SOCK_STREAM).
    serversocket = socket(AF_INET, SOCK_STREAM)
    
    try:
        # Bind the socket to the address ('localhost', 8888).
        serversocket.bind(('localhost', 8888))
        
        # Listen for incoming connections with a backlog queue size of 5.
        serversocket.listen(5)
        
        # Loop to continuously accept connections.
        while(1):
            # Accept a new connection and store the client socket and its address.
            (clientsocket, address) = serversocket.accept()
            
            # Receive data (up to 5000 bytes) from the client and decode it from bytes to a string.
            rd = clientsocket.recv(5000).decode()
            
            # Split the received data into lines.
            pieces = rd.split("\n")
            
            # If there are pieces (lines) of data, print the first line.
            if len(pieces) > 0:
                print(pieces[0])
            
            # Prepare the response data with HTTP headers.
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"  # Empty line indicates the end of HTTP headers.
            data += "<html><body>Hello World</body></html>\r\n\r\n"  # HTML response body.
            
            # Send the response data to the client, encoded as bytes.
            clientsocket.sendall(data.encode())
            
            # Shutdown the writing portion of the client socket.
            clientsocket.shutdown(SHUT_WR)
    
    # Handle keyboard interrupt (Ctrl+C).
    except KeyboardInterrupt:
        print("\nShutting down...\n")
    
    # Handle other exceptions.
    except Exception as e:
        print("Error")
        print(e)
    
    # Close the server socket.
    serversocket.close()

# Print a message to indicate how to access the server.
print("Access http://localhost:8888")

# Call the createServer function to start the server.
createServer()
