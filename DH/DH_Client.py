import sys
from random import random, randrange
import socket

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
p = str(p)[:8]
a = randrange(int(p)-2)
g = randrange(int(p))
ka = exp(g,a,int(p))

print "P: " + str(p)
print "G: " + str(g)
print "A: " + str(a)
print "Ka:" + str(ka)
client = socket.socket()
client.connect(('127.0.0.1', 7500))
client.send(str(p))
client.send(str(g))
client.send(str(ka))
Kb = client.recv(10)
print "kb:" + Kb

k = exp(int(Kb),a,int(p))
print "K: " + str(k)
"""while True:
    mensaje = raw_input("Mensaje a enviar >>")
    client.send(mensaje)
    if mensaje == "close":
        break
    print client.recv(10)"""
print "Adios."

client.close()
