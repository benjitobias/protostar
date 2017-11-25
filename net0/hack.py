import struct
import socket

IP_ADDRESS = "172.16.104.130"
PORT = 2999

def get_number_to_send(s):
    data = s.recv(1024)
    number = data.split(" ")[2].strip("'")
    print data
    return int(number)

def convert_to_little_endian_representation(s, number):
    return struct.pack("<i", number)

def main():
    s = socket.socket()
    s.connect((IP_ADDRESS, PORT))
    number =  get_number_to_send(s)
    new_number = convert_to_little_endian_representation(s, number)
    s.send(new_number)
    print "Sending: %s" % new_number 
    print s.recv(1024)
    s.close()

if '__main__' == __name__:
    main()
