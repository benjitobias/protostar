import struct
import socket

IP_ADDRESS = "172.16.104.130"
PORT = 2998

def get_number_to_send(s):
    data = s.recv(1024)
    number = struct.unpack("i", data)[0]
    return str(number)

def main():
    s = socket.socket()
    s.connect((IP_ADDRESS, PORT))
    number =  get_number_to_send(s)
    print number
    s.send(number)
    print "Sending: %s" % number 
    s.send("\r\n")
    print s.recv(1024)
    s.close()

if '__main__' == __name__:
    main()
