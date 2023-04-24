#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# The modules required
import sys
import socket
import struct

'''
It takes 2 commandline arguments and calls function send_and_receive_tcp.

you can execute this file with the command: 
python3 CourseWork2023.py <ip> <port> 

windows: ipython3 CourseWork2023.py 195.148.20.105 10000

THIS work includes only basic parts, NONE of extra features is done
''' 
 
def send_and_receive_tcp(address, port):
    print("You gave arguments: {} {}".format(address, port))

    message = "HELLO\r\n"
    print(message)
    # create TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect socket to given address and port
    s.connect((address, port))
    # python3 sendall() requires bytes like object. encode the message with str.encode() command
    data= str.encode(message)
    # send given message to socket
    s.sendall(data)

    # receive data from socket
    ret = s.recv(4096*4)
    # data you received is in bytes format. turn it to string with .decode() command
    ret_string = ret.decode()
    # print received data
    print(ret_string)
    # close the socket
    s.close()

    # Get your CID and UDP port from the message
    token = ret_string.split()[1]
    udp_port = int(ret_string.split()[2])
        
    # Continue to UDP messaging. You might want to give the function some other parameters like the above mentioned cid and port.
    send_and_receive_udp(address, udp_port, token)
    return
 
 
def send_and_receive_udp(address, port, token):
    message = "Hello from " + token + "\n"
    print(message)
    
    cid = str.encode(token)
    ack = True
    eom = False
    data_remaining = 0
    content_length = len(message)
    packet = str.encode(message)
    content_with_header = struct.pack("!8s??HH128s", cid, ack, eom, data_remaining, content_length, packet)

    # create udp socket    
    s_ = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s_.sendto(content_with_header, (address, port))

    while (True):
        (message_received, _) = s_.recvfrom(4096*64)
        header_ = message_received[:14]
        data_ = message_received[14:].decode().rstrip('\x00')
        print("received data from server: ", data_)

        reverseArray = data_.split(" ")[::-1]        
        if (reverseArray[0] == 'Bye.'):
            break
    
        message_to_send = " ".join(reverseArray)
        print("sending data to server: ", message_to_send)
        
        content_length = len(message_to_send)
        packet = str.encode(message_to_send)
        message_with_header = struct.pack("!8s??HH128s", cid, ack, eom, data_remaining, content_length, packet)
        s_.sendto(message_with_header, (address, port))


    s_.close()
    return
 
 
def main():
    USAGE = 'usage: %s <server address> <server port>' % sys.argv[0]
 
    try:
        # Get the server address, port and message from command line arguments
        server_address = str(sys.argv[1])
        server_tcpport = int(sys.argv[2])
    except IndexError:
        print("Index Error")
    except ValueError:
        print("Value Error")
    # Print usage instructions and exit if we didn't get proper arguments
        sys.exit(USAGE)
 
    send_and_receive_tcp(server_address, server_tcpport)
 
 
if __name__ == '__main__':
    # Call the main function when this script is executed
    main()
