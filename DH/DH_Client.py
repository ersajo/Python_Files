import sys
from random import random, randrange
import socket

def exp(num, exp, res, mod):
    if exp == 0:
        return res
    else:
        res = (res * num) % mod
        exp -= 1
        exp(num, exp, res, mod)

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
p = str(p)[0:8]
a = num = randrange(int(p))
ka = exp(3,4,1,5)
print ka

client = socket.socket()
client.connect(('127.0.0.1', 7000))
print "P: " + p
print "A: " + str(a)
client.send(p)
while True:
    mensaje = raw_input("Mensaje a enviar >>")
    client.send(mensaje)
    if mensaje == "close":
        break
    #print client.recv(1024)
print "Adios."

client.close()
