# Import the socket module, which provides access to the BSD socket interface.
import socket

# Create a socket object 'mysock' using IPv4 addressing (AF_INET) and TCP protocol (SOCK_STREAM).
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server specified by the tuple ('data.pr4e.org', 80).
mysock.connect(("data.pr4e.org", 80))

# Define the HTTP command to send to the server. Here, we're requesting the page 'page1.htm'.
# The 'GET' method is used to retrieve data from the specified URL.
# HTTP version is specified as 1.0. '\r\n' signifies the end of a line in HTTP, and '\r\n\r\n' signifies the end of the header section.
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()

# Send the HTTP command encoded as bytes to the server.
mysock.send(cmd)

# Continuously receive data (in chunks of 512 bytes) from the server until there's no more data.
while True:
    # Receive data (up to 512 bytes) from the server and store it in 'data'.
    data = mysock.recv(512)
    
    # If the length of 'data' is less than 1, it means there's no more data to receive, so break out of the loop.
    if len(data) < 1:
        break
    
    # Decode the received data (which is in bytes) into a string and print it.
    print(data.decode(), end="")

# Close the socket connection.
mysock.close()
