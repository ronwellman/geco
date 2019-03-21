#!/usr/bin/env python3
'''Generic TCP client for sending messages to a server.
'''
import socket
import sys


def main(server_IP, server_port):
    try:
        while True:

            # get the message to send
            message = input("Message: ")

            # Create the socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

                # connect to server
                s.connect((server_IP, int(server_port)))

                # send message
                s.sendall(message.encode('utf-8'))

    except KeyboardInterrupt:
        pass
    except ConnectionRefusedError:
        print("Unable to connect to server: {} on port {}".format(server_IP,
                                                                  server_port))
    except OSError as e:
        print("Error: {}".format(e))


if __name__ == "__main__":

    # ensure comand line inputs have been received
    if len(sys.argv) != 3:
        print("Usage: ./client SERVER_IP_ADDRESS SERVER_PORT")
        sys.exit(1)
    else:
        main(sys.argv[1], sys.argv[2])
