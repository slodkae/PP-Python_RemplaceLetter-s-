s = 'Naze'
b = bytearray(s)
b[2] = 'm'
s = str(b)
print(s)