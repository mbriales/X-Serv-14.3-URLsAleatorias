#!/usr/bin/python

import socket   # For create server
import random   # For create random objects

# Creates my socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# For reuse the port if not running processes
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Binds localhost and port
mySocket.bind(('localhost', 1301))
# Queue for TCP connection requests
mySocket.listen(5)

# Creates a random number between 1 and 10000
URLaleatoria = str(random.randint(1, 10000))

try:
    while True:
        print 'Waiting for connection'
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'
        print recvSocket.recv(1301)
        print 'Answering back...'
        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body>" +
                        "<p>Hola " +
                        # Prints user address
                        str(address[0]) +
                        ". Dame otra " +
                        # Gives a random URL
                        "<a href='URL-aleatoria'>" + URLaleatoria + "</a>"
                        "</p>" +
                        "</body></html>" +
                        "\r\n")
        recvSocket.close()
    print 'random.randint(a, b)'
# Closes the socket when Ctrl-C input
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
