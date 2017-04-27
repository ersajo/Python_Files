import sys
from random import random, randrange

def exp(base, expo, mod):
    ans = 1
    if expo == 0:
        ans = 1
    else:
        while expo >= 1:
            ans *= base
            expo -= 1
            ans = ans % mod
        return ans

def es_primo(num):
    i = 1;
    if num < 2:
        return False
    while num % i != 0:
        i += 1
        if num % i == 0:
            return False
    return True

def genP():
    while True:
        ran = str(random()).split('.')
        num = int(ran[1])
        if es_primo(num):
            return num

p = genP()
q = genP()

n = p*q;

print "p: " + str(p)
print "q: " + str(q)
print "n: " + str(n)
