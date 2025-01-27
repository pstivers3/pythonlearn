#!/usr/bin/env python3

s = 'sp\xc4m'                                          # Non-ASCII Unicode text
print('s is   : ', s)
print('s[2] is: ', s[2])                               # Sequence of characters

file = open('unidata.txt', 'w', encoding='utf-8')      # Write/encode UTF-8 text
file.write(s)                                          # 4 characters written
file.close()

text = open('unidata.txt', encoding='utf-8').read()    # Read/decode UTF-8 text
print('text is: ', text)
