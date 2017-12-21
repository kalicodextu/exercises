#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.Util import number

num = number

# Returns the size of the number N in bits.
print 'enter a numer:'
a = int(raw_input())
size = num.size(a)
print 'The size of %s in bits: %s' % (a, size)

# getRandomInteger(N, randfunc=None)
r_num = num.getRandomInteger(20)
print '%s is a random number with at most 20 bits' % r_num

# getRandomRange(a, b, randfunc=None)
rr_num = num.getRandomRange(1, 100)
print '%s is a random number between 1 and 100.' % rr_num

# getRandomNBitInteger(N, randfunc=None)
nBit_num = num.getRandomNBitInteger(10)
print '%s is a random number with exactly 10-bits, i.e. a random number between 2**(10-1) and (2**10)-1.' % nBit_num

# getPrime(N, randfunc=None)
n_prime = num.getPrime(10)
print '%s is a random 1024 bits prime number.' % n_prime

# getStrongPrime
nS_prime = num.getStrongPrime(1024)
print '%s is a random strong 1024-bit prime number.' % nS_prime

# isPrime
bPrime = num.isPrime(997)
if bPrime:
    print '997 is a prime'
else:
    print '997 not a prime'


# long_to_bytes(n, blocksize=0)
strnum = num.long_to_bytes(1024)
print '12345678910 to bytes: %s' % strnum.encode()

# bytes_to_long(s)
numstr = num.bytes_to_long(strnum)
print '%s to long: %s' % (strnum.encode(), numstr)
