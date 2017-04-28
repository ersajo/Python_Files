from random import random, randrange
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def llavePublica():
    bits=2048
    new_key = RSA.generate(bits, e=65537)
    public_key = new_key.publickey().exportKey("PEM")
    llavePublica = open("llavePublicaCandy.txt", "w")
    llavePublica.write(public_key)
    llavePublica.close()

def llavePrivada():
    bits=2048
    new_key = RSA.generate(bits, e=65537)
    public_key = new_key.publickey().exportKey("PEM")
    private_key = new_key.exportKey("PEM")
    llavePrivada = open("llavePrivadaCandy.txt","w")
    llavePrivada.write(private_key)
    llavePrivada.close()

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
def gcd(a,b):
    while b != 0:
        (a,b) = (a, a % b)
    return a;

def genE():
    p = genP()
    q = genP()
    n = p*q
    phi = (p-1)*(q-1)
    e = randrange(n)
    while(True):
        if(gcd(e,phi) == 1):
            break
        e = randrange(n)
        print e
    return e

llavePrivada()
llavePublica()
