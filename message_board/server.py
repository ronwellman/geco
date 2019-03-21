#!/usr/bin/env python3
'''Generic TCP Server for receiving messages and printing them out to the
screen.
'''
import socket

PORT = 5555
IP = '0.0.0.0'

# build a socket via IPV4 TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ensure socket can be immediately reused
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind on every IPV4 Address via port 5555
server_socket.bind((IP, PORT))

# listen for incoming connections
server_socket.listen(10)

try:

    while True:
        # accept incoming connections
        client_socket, client_address = server_socket.accept()
        print("Connection from: {} on port {}".format(client_address[0],
                                                      client_address[1]))

        # read in a message
        message = client_socket.recv(65535)

        print("Message: {}".format(message.decode('utf-8').strip()))

        client_socket.close()

except KeyboardInterrupt:
    server_socket.close()
