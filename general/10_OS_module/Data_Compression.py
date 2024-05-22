""" zlib library used for compression and decompression"""
import zlib
s=b'Hello hello hello'
print(len(s))
t=zlib.compress(s)
print(len(t))