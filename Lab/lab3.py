#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# The modules required
import sys
import socket

'''
Use this template to create exercise 1 of lab3. Follow the hints found in the comments to complete the task.
'''
 
 
def send_and_receive_tcp(address, port, message):
    # create TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect socket to given address and port
    s.connect((address, port))
    # python3 sendall() requires bytes like object. Encode the message with .encode() command    
    # send given message to socket
    s.sendall(message.encode())
    # receive data from socket
    received = s.recv(4096)
    # data you received is in bytes format. turn it to string with .decode() command
    data = received.decode()
    # print received data
    print(data)
    # close the socket
    s.close()  

    # Uncomment for second part of the exercise:
    #send_and_receive_udp(address, port, data)
    return
 
 
def send_and_receive_udp(address, port, message):
    # create UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # You turned the message in to str in previous function. Turn it back to bytes
    data = str.encode(message)
    # send given message to given address and port using the socket.
    s.sendto(data, (address, port))

    # Loop the following
    while (True):
        # receive data from socket
        received_data, _ = s.recvfrom(4096)
        # Data you receive is in bytes format. Turn it to string with .decode() command
        data = received_data.decode()
        # print received data
        print(data)        
        # if received data contains the word 'QUIT' break the loop
        if ('QUIT' in data):
            break
               
    # close the socket
    s.close()
    return
 
 
def main():
    USAGE = 'usage: %s <server address> <server port> <message>' % sys.argv[0]
 
    try:
        # Get the server address, port and message from command line arguments
        server_address = str(sys.argv[1])
        server_tcpport = int(sys.argv[2])
        message = str(sys.argv[3])
    except IndexError:
        print("Index Error")
    except ValueError:
        print("Value Error")
    # Print usage instructions and exit if we didn't get proper arguments
        sys.exit(USAGE)
 
    send_and_receive_tcp(server_address, server_tcpport, message)
 
 
if __name__ == '__main__':
    # Call the main function when this script is executed
    main()
