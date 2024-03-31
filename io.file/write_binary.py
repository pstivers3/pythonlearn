#!/usr/bin/env python3

import struct

packed = struct.pack('>i4sh', 7, b'spam', 8)
print('packed binary: ', packed)

file = open('data.bin', 'wb')
file.write(packed)

file.close()
