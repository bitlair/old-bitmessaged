from socket import *
import plugins.bitlicht
address = ('', 6005)
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(address)

while(1):
    recv_data, addr = server_socket.recvfrom(2048)
    if recv_data == "bitlicht.test" :
        bitlicht.test()
    elif recv_data == "bitlicht.flash":
        bitlicht.flash()
    elif "bitpanel.message" in recv_data:
        print("Bitpanel message: %s"%(recv_data[17:]))
