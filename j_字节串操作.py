x = 523**23
nbyte, rem = divmod(x.bit_length(), 8)
if rem:
    nbyte += 1

# print(x.to_bytes(16, 'little'))   error!
print(x.to_bytes(nbyte, 'little'))



