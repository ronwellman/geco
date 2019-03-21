#!/usr/bin/env python3
'''Generic TCP client for sending messages to a server.
'''
import socket
import sys


def main(server_IP, server_port):

    # get username


    try:
        while True:

            # get the message to send


            # concatenate username to message


            # Create the socket


                # connect to server


                # send message


    except KeyboardInterrupt:
        pass
    except ConnectionRefusedError:
        print("Unable to connect to server: {} on port {}".format(server_IP,
                                                                  server_port))
    except OSError as e:
        print("Error: {}".format(e))


if __name__ == "__main__":

    # ensure comand line inputs have been received
    # ./client.py IP_ADDRESS PORT_NUM
