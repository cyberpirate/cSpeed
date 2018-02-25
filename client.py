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

i = 0

while(1) :
     
    try :
        #Set the whole string
        msg = bytes([i])
        i = i + 1
        s.sendto(msg, (host, port))
         
        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
         
        print('Server reply : ' + reply)
     
    except Exception as e:
        print('Error : ' + str(e))
        sys.exit()