import sys
import random
import socket

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
        ran = str(random.random()).split('.')
        num = int(ran[1])
        if es_primo(num):
            return num

p = genP()

def genA():
    while True:
        ran = str(random.random()).split('.')
        num = int(ran[1])
        while num > p:
            ran = str(random.random()).split('.')
            num = int(ran[1])
        if es_primo(num):
            return num
print p
print genA()

client = socket.socket()
client.connect(('127.0.0.1', 7000))

while True:
    mensaje = raw_input("Mensaje a enviar >>")
    client.send(mensaje)
    if mensaje == "close":
        break
    print client.recv(1024)
print "Adios."

client.close()
