#!/usr/bin/python3

'''
    udp socket client
    Silver Moon
'''
 
import socket   #for sockets
import sys  #for exit

def intToBytes(n):
    b = bytearray([0, 0, 0, 0])   # init
    b[3] = n & 0xFF
    n >>= 8
    b[2] = n & 0xFF
    n >>= 8
    b[1] = n & 0xFF
    n >>= 8
    b[0] = n & 0xFF    
    
    # Return the result or as bytearray or as bytes (commented out)
    ##return bytes(b)  # uncomment if you need
    return b

def bytesToInt(b, offset):
    n = (b[offset+0]<<24) + (b[offset+1]<<16) + (b[offset+2]<<8) + b[offset+3]
    return n

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except Exception as e:
    print('Failed to create socket')
    sys.exit()

host = '208.113.164.65'
port = 34196

i = 0

while(1) :
     
    try :
        #Set the whole string
        msg = str(i).encode('utf-8')
        i = i + 1
        s.sendto(msg, (host, port))
         
        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
         
        print('Server reply : ' + str(reply))
     
    except Exception as e:
        print('Error : ' + str(e))
        sys.exit()