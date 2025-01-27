#!/usr/bin/env python3

# hexdump -C data.bin # to read file
import struct

packed = struct.pack('>i4sh', 7, b'spam', 8)
print('packed binary: ', packed)

file = open('../files/data.bin', 'wb')
file.write(packed)

file.close()
