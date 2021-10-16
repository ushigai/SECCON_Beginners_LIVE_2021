from Crypto.Util.number import *
from flag import flag

flag = bytes_to_long(flag.encode("utf-8"))
p = getPrime(512) 
q = getPrime(512)
n = p * q
e = 3

assert flag.bit_length() == 343
assert n < flag ** e

print("n =", n)
print("e =", e)
print("c =", pow(flag, e, n))
