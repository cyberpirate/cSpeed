#!/usr/bin/python3

'''
    Simple udp socket server
'''
 
import socket
import sys
 
HOST = ''    # Symbolic name meaning all available interfaces
PORT = 34197 # Arbitrary non-privileged port
 
# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket created')
except Exception as e:
    print('Failed to create socket. Error Code : ' + e)
    sys.exit()
 
 
# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except Exception as e:
    print('Bind failed. Error Code : ' + e)
    sys.exit()
     
print('Socket bind complete')
 
#now keep talking with the client
while 1:
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
     
    if not data: 
        break
     
    reply = 'OK...' + data
     
    s.sendto(reply , addr)
    print('Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip())
     
s.close()