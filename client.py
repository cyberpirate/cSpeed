#!/usr/bin/python3

'''
    udp socket client
    Silver Moon
'''
 
import socket   #for sockets
import sys  #for exit
 
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except Exception as e:
    print('Failed to create socket')
    sys.exit()
 
host = '208.113.164.65'
port = 34197
 
while(1) :
    msg = input('Enter message to send : ')
     
    try :
        #Set the whole string
        s.sendto(bytes(msg, 'utf-8'), (host, port))
         
        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
         
        print('Server reply : ' + reply)
     
    except Exception as e:
        print('Error : ' + str(e))
        sys.exit()