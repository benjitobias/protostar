import struct
import socket

IP_ADDRESS = "172.16.104.130"
PORT = 2997

def get_numbers(s):
    numbers = []

    for i in xrange(4):
        numbers.append(s.recv(4))
    print "Recieved numbers"
    print numbers
    return numbers

def calculate_total(numbers):
    total = 0
    for num in numbers:
        total += struct.unpack("<I", num)[0]
    print "Total: %d" % total
    return total

def main():
    s = socket.socket()
    s.connect((IP_ADDRESS, PORT))
    numbers =  get_numbers(s)
    total = calculate_total(numbers)
    total &= 0xffffffff
    total = struct.pack("<I", total)
    s.send(total)
    #print "Sending: %s" % new_number 
    print s.recv(1024)
    s.close()

if '__main__' == __name__:
    main()
