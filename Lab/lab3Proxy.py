#!/usr/bin/python

import select
import socket


TCP_PORT = 21000
UDP_PORT = 21000

DEST_IP = '195.148.20.105'
DEST_PORT = 20000

MESSAGE_BUFFER_SIZE = 4096*2

def handle_tcp(sock):
    '''
    This function should do the following:
    * When receiving a message from the client print the message content and somehow implicate where it came from. For example "Client sent X"
    * Create a TCP socket.
    * Forward the message to the server using the socket.
    * Print what you received from the server
    * Forward it to the client.
    * Close socket
    '''
    
    sock.listen(5)
    client_socket, client_address = sock.accept()
    
    message_from_client = client_socket.recv(MESSAGE_BUFFER_SIZE)
    
    print("Client: {} sent ({})".format(client_address, message_from_client.decode()))


    server_address = (DEST_IP, DEST_PORT)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(server_address)
    
    server_socket.sendall(message_from_client)
    
    message_from_server = server_socket.recv(MESSAGE_BUFFER_SIZE)
    print("Message from server: ", message_from_server.decode())
    
    client_socket.sendall(message_from_server)
    
                
    client_socket.close()            
    server_socket.close()
        
    print("TCP happended")                    
    return


def handle_udp(sock):
    '''
    This function should do the following
    * When receiving a message from the client print the message content and somehow implicate where it came from. For example "Client sent X"
    * Create a UDP socket
    * Forward the message to the server using the socket.
    * A loop that does the following:
        * Print what you received from the server
        * Forward it to the client.
        * Break. DO NOT use message content as your break logic (if "QUIT" in message). Use socket timeout or some other mean.  
    * Close socket
    '''

    #client - proxy 
    (data, client_address) = sock.recvfrom(MESSAGE_BUFFER_SIZE)
    print("Client: {} sent message: ({})".format(client_address, data.decode()))
    
    #proxy - server
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(10)
    server_address = (DEST_IP, DEST_PORT)
    
    s.sendto(data, server_address)
    print("forwarding the client message: ({}) to server: {} ".format(data.decode(), server_address))
        
    print('\nLooping proxy, socket timeout 10 sec (or press Ctrl-C to stop)...')
    try:
        while (True):
            (received_from_server, server_address) = s.recvfrom(MESSAGE_BUFFER_SIZE)
            print("Message: ({}) received from Server: {} ".format(received_from_server.decode(), server_address))

            sock.sendto(received_from_server, client_address)
            print("forwarding received message: ({}) from server to client {} ".format(received_from_server.decode(), client_address))
    except socket.timeout:
        print("socket timeout")        
        
    s.close()
    print("UDP happened")
    return


def main():
    try:
        print("Creating sockets")
        '''
        Create and bind TCP and UDP sockets here. Use hard coded values TCP_PORT and UDP_PORT to choose your port. 
        Note that while loop below  uses these sockets, so name them tcp_socket and udp_socket or modify the loop below.
        '''
        tcp_proxy_address = ('', TCP_PORT)
        udp_proxy_address = ('', UDP_PORT)
        
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("socket created")
        
        tcp_socket.bind(tcp_proxy_address)
        udp_socket.bind(udp_proxy_address)
        

    except OSError:
        '''
    This will be raised if you are trying to create a socket but it is still active. Likely your code crashed or otherwise closed before you closed the socket. Wait a second and the socket should become available. Alternatively you can create a logic here that binds the socket to X_PORT+1. Doing this is not mandatory
        '''
        print("OSError was rised. Port is in use. Wait a second.")

    try:
        while True:
            i, o, e = select.select([tcp_socket, udp_socket], [], [], 5)
            if tcp_socket in i:
                handle_tcp(tcp_socket)
            if udp_socket in i:
                handle_udp(udp_socket)
    except NameError:
        print("Please create the sockets. NameError was raised doe to them missing.")
    finally:
        '''
        !!Close sockets here!!
        '''
        tcp_socket.close()
        udp_socket.close()
        
    

if __name__ == '__main__':
    main()
