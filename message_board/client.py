#!/usr/bin/env python3
'''Generic TCP client for sending messages to a server.
'''
import socket
import sys


def main(server_IP, server_port):
    try:
        while True:
            message = input("Message: ")

            # Create the socket
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server_IP, int(server_port)))
            client_socket.sendall(message.encode('utf-8'))
            client_socket.close()

    except KeyboardInterrupt:
        pass
    except ConnectionRefusedError:
        print("Unable to connect to server: {} on port {}".format(server_IP,
                                                                  server_port))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./client SERVER_IP_ADDRESS SERVER_PORT")
        sys.exit(1)
    else:
        main(sys.argv[1], sys.argv[2])
