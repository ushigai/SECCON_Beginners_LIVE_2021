from Crypto.Util.number import *
from random import getrandbits
from flag import flag


def culc1(x, y):
    res = 0
    for i in range(max(x.bit_length(), y.bit_length())):
        x_, y_ = (x >> i) & 1, (y >> i) & 1
        z = x_ * y_
        res += 2**i * z
    return res

def culc2(x, y):
    res = 0
    for i in range(max(x.bit_length(), y.bit_length())):
        x_, y_ = (x >> i) & 1, (y >> i) & 1
        z = x_ + y_ - x_ * y_
        res += 2**i * z
    return res

def culc3(x, y):
    res = 0
    for i in range(max(x.bit_length(), y.bit_length())):
        x_, y_ = (x >> i) & 1, (y >> i) & 1
        z = (x_*(1 - y_) + y_*(1 - x_))
        res += 2**i * z
    return res

flag = bytes_to_long(flag)
length = flag.bit_length()

cipher = []
going = 256
for i in range(going):
    a = getrandbits(length)
    b = getrandbits(length)
    c = getrandbits(length)
    key = culc1(culc2(a, b), culc2(a, c))
    cipher.append(culc3(flag, key))

file = open("output.txt", "w")
file.write("length = " + str(length) + "\n")
file.write("cipher = " + str(cipher) + "\n")
file.close()
