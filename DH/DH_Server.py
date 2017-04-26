import sys
from random import randrange
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

print "Starting Server..."

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 7500))
server.listen(1)
client, addr = server.accept()

print "Starting conection with: " + addr[0]

print "Receiving P..."
P = client.recv(8)
print "P: " + P

print "Receiving G..."
G = client.recv(8)
print "G: " + G

print "Generating B..."
b = randrange(int(P)-2)
print "B: " + str(b)

print "Calculating Kb..."
kb = exp(int(G),b,int(P))
print "Kb:" + str(kb)
print "Sending Kb..."
client.sendall(str(kb))

print "Receiving Ka..."
Ka = client.recv(10)
print "Ka:" + Ka

print "Calculating the key..."
k = exp(int(Ka),b,int(P))
print "Key: " + str(k)

print "Adios."

client.close()
server.close()
