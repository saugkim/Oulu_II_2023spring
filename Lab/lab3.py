#!/usr/bin/python          

import sys
import socket


# create socket for tcp connection
# create connection with given ip(first argument) and port(second argument)
# send given mesesage (last argument) as bytes (encode) to the server 
# receive message as bytes from server and print it as a text (decode)
# close connection
# return message from server (bytes)
def send_and_receive_tcp(IP, port, message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, port))
    s.sendall(message.encode())
    ret = s.recv(4096)
    print(ret.decode())
    s.close()    
    return ret

# create socket for udp (using socket.SOCK_DGRAM)
# no connection made
# input text message from user 
# send user message to TCP server and receive reply from TCP server
# re-send replied message from TCP to UDP server
# loop until user input is QUIT
def send_and_receive_udp(IP, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while (True):
        message = input("give me message: ")
        if (message == 'QUIT'):
            print("QUIT")
            break       
        ret = send_and_receive_tcp(IP, port, message)
        s.sendto(ret, (IP, port))


def main():
    try:
        # Get the server address, port and message from command line arguments
        server_address = str(sys.argv[1])
        server_port = int(sys.argv[2])
    except IndexError:
        print("Index Error")
    except ValueError:
        print("Value Error")
    
    
    args = sys.argv[1:]
    if (len(args) == 2):
        send_and_receive_udp(server_address, server_port)
    elif (len(args) == 3):
        send_and_receive_tcp(server_address, server_port, args[2])
    else:
        print("Wrong input")


if __name__ == "__main__":
    main()