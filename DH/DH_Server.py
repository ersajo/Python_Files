import sys
from random import randrange
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

def genB():
    while True:
        num = randrange(int(P))
        if es_primo(num):
            return num

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 7000))
server.listen(1)
client, addr = server.accept()

P = client.recv(8)
print "P: " + P
b = genB()
print "B: " + str(b)

while True:
    recibido = client.recv(1024)
    if recibido == "close":
        break
    print str(addr[0]) + " dice: ", recibido
    #client.sendall(recibido)

print "Adios."

client.close()
server.close()
