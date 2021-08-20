from Crypto.Util.number import *
from flag import flag

flag = bytes_to_long(flag.encode("utf-8"))
p, q = getPrime(512), getPrime(512)
n = p * q
e = 3

assert flag.bit_length() == 343
assert n < flag ** e

print("c =", pow(flag, e, n))
print("e =", e)
print("n =", n)
