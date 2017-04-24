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
a = str(randrange(int(p)-2))
g = str(randrange(int(p)))
ka = exp(int(g),int(a),int(p))

print "P: " + p
print "G: " + g
print "A: " + a
print "Ka:" + str(ka)
client = socket.socket()
client.connect(('127.0.0.1', 7000))
client.send(p)
client.send(g)
while True:
    mensaje = raw_input("Mensaje a enviar >>")
    client.send(mensaje)
    if mensaje == "close":
        break
    #print client.recv(1024)
print "Adios."

client.close()
