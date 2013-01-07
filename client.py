from socket import *
import sys
import select

address = ('localhost', 6005)
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.sendto('bitpanel.message <zarya> bla die die bla bla', address)
