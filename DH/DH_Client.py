import sys
from random import random, randrange
import socket

ip = '127.0.0.1'

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

client = socket.socket()
client.connect((ip, 7500))
print "Connecting to " + ip + "..."

print "Generating P..."
p = genP()
p = str(p)[:8]
print "P: " + str(p)
print "Sending P..."
client.send(str(p))

print "Generating G..."
g = randrange(int(p))
print "G: " + str(g)
print "Sending G..."
client.send(str(g))

print "Generating A..."
a = randrange(int(p)-2)
print "A: " + str(a)

print "Calculating Ka..."
ka = exp(g,a,int(p))
print "Ka:" + str(ka)
client.send(str(ka))
print "Sending Ka"

print "Receiving Kb..."
Kb = client.recv(10)
print "kb:" + Kb

print "Calculating the key..."
k = exp(int(Kb),a,int(p))
print "K: " + str(k)

print "Adios."

client.close()
