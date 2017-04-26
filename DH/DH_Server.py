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

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 7500))
server.listen(1)
client, addr = server.accept()



P = client.recv(8)
G = client.recv(8)
print "P: " + P
print "G: " + G
b = randrange(int(P)-2)
print "B: " + str(b)
kb = exp(int(G),b,int(P))
Ka = client.recv(10)
print "Ka:" + Ka
print "Kb:" + str(kb)
client.sendall(str(kb))

k = exp(int(Ka),b,int(P))
print "K: " + str(k)


"""while True:
    recibido = client.recv(1024)
    if recibido == "close":
        break
    print str(addr[0]) + " dice: ", recibido
    #client.sendall(str(kb))"""
print "Adios."

client.close()
server.close()
