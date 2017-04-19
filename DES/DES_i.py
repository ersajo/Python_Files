import os
from Crypto.Cipher import DES
from Crypto.Util import Counter
from Crypto import Random

archivo = "winter.bmp"

def menu():                         #Funcion que simulara el menu en el shell
    os.system('clear')              #Limpiamos pantalla del shell
    print ("Choose an option")      #Inicio de menu
    print ("\te - Encrypt")         #Primer opcion
    print ("\td - Decrypt")         #Segunda opcion
    print ("\tq - Quit")            #Opcion para terminar la ejecucion del programa

def enc_file_ECB(in_filename, key):
    ECB = DES.new(key, DES.MODE_ECB)
    with open(in_filename, 'rb') as in_file:
        with open('Img/c_ECB.bmp', 'wb') as fECB:
            while True:
                header = in_file.read(44)
                chunk = in_file.read()
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                fECB.write(header)
                fECB.write(ECB.encrypt(chunk))

def enc_file_CBC(in_filename, key):
    CBC = DES.new(key, DES.MODE_CBC, '12345678')
    with open(in_filename, 'rb') as in_file:
        with open('Img/c_CBC.bmp', 'wb') as fCBC:
            while True:
                header = in_file.read(44)
                chunk = in_file.read()
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                fCBC.write(header)
                fCBC.write(CBC.encrypt(chunk))

def enc_file_OFB(in_filename, key):
    OFB = DES.new(key, DES.MODE_OFB, '12345678')
    with open(in_filename, 'rb') as in_file:
        with open('Img/c_OFB.bmp', 'wb') as fOFB:
            while True:
                header = in_file.read(44)
                chunk = in_file.read()
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                fOFB.write(header)
                fOFB.write(OFB.encrypt(chunk))

def enc_file_CFB(in_filename, key):
    CFB = DES.new(key, DES.MODE_CFB, '12345678')
    with open(in_filename, 'rb') as in_file:
        with open('Img/c_CFB.bmp', 'wb') as fCFB:
            while True:
                header = in_file.read(44)
                chunk = in_file.read()
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                fCFB.write(header)
                fCFB.write(CFB.encrypt(chunk))

def enc_file_CTR(in_filename, key):
    nonce = "0000"
    ctr = Counter.new(DES.block_size*8/2, prefix=nonce)
    CTR = DES.new(key, DES.MODE_CTR, counter=ctr)
    with open(in_filename, 'rb') as in_file:
        with open('Img/c_CTR.bmp', 'wb') as fCTR:
                            while True:
                                header = in_file.read(44)
                                chunk = in_file.read()
                                if len(chunk) == 0:
                                    break
                                elif len(chunk) % 16 != 0:
                                    chunk += ' ' * (16 - len(chunk) % 16)
                                fCTR.write(header)
                                fCTR.write(CTR.encrypt(chunk))

def dec_file_ECB(in_filename, key):
    ECB = DES.new(key, DES.MODE_ECB)
    with open(in_filename, "rb") as in_file:
        with open('Img/d_ECB.bmp', 'wb') as fECB:
            while True:
                header = in_file.read(44)
                chunk = in_file.read()
                if len(chunk) == 0:
                    break
                fECB.write(header)
                fECB.write(ECB.decrypt(chunk).strip())

def dec_file_CBC(in_filename, key):
    CBC = DES.new(key, DES.MODE_CBC, '12345678')
    with open(in_filename, "rb") as in_file:
        with open('Img/d_CBC.bmp', 'wb') as fCBC:
            while True:
                header = in_file.read(44)
                chunk = in_file.read()
                if len(chunk) == 0:
                    break
                fCBC.write(header)
                fCBC.write(CBC.decrypt(chunk).strip())

def dec_file_OFB(in_filename, key):
    OFB = DES.new(key, DES.MODE_OFB, '12345678')
    with open(in_filename, "rb") as in_file:
        with open('Img/d_OFB.bmp', 'wb') as fOFB:
            while True:
                header = in_file.read(44)
                chunk = in_file.read()
                if len(chunk) == 0:
                    break
                fOFB.write(header)
                fOFB.write(OFB.decrypt(chunk).strip())

def dec_file_CFB(in_filename, key):
    CFB = DES.new(key, DES.MODE_CFB, '12345678')
    with open(in_filename, "rb") as in_file:
        with open('Img/d_CFB.bmp', 'wb') as fCFB:
            while True:
                header = in_file.read(44)
                chunk = in_file.read()
                if len(chunk) == 0:
                    break
                fCFB.write(header)
                fCFB.write(CFB.decrypt(chunk).strip())

def dec_file_CTR(in_filename, key):
    nonce = "0000"
    ctr = Counter.new(DES.block_size*8/2, prefix=nonce)
    CTR = DES.new(key, DES.MODE_CTR, counter=ctr)
    with open(in_filename, "rb") as in_file:
        with open('Img/d_CTR.bmp', 'wb') as fCTR:
            while True:
                header = in_file.read(44)
                chunk = in_file.read()
                if len(chunk) == 0:
                    break
                fCTR.write(header)
                fCTR.write(CTR.decrypt(chunk).strip())

os.system('clear')
key = raw_input ("Write a key >> ")
while len(key) != 8:
    os.system('clear')
    key = raw_input ("Wrong key, Key must be 8 characters.\n Write another key >> ")
with open("key.txt","w") as fkey:
    fkey.write(key)
while True: #Ciclo para llamar al menu al finalizar la opcion
    menu()  #Se llama al menu
    optMenu = raw_input ("Choose an option >> ")  #raw_input funciona para leer una cadena
                                                    #Se lee la opcion y se guarda en una variable
    if optMenu == "e":                              #Primer opcion
        print("Encrypt")                            #Para verificar la entrada
        enc_file_ECB('Img/'+archivo,key)
        enc_file_CBC('Img/'+archivo,key)
        enc_file_OFB('Img/'+archivo,key)
        enc_file_CFB('Img/'+archivo,key)
        enc_file_CTR('Img/'+archivo,key)
        raw_input("Press enter to continue")
    elif optMenu == "d":                            #Segunda opcion
        print("Decrypt")                            #Para verificar la entrada
        img = raw_input("Write the name of the file >>")
        mode = raw_input("Select a mode:\n1. ECB\n2. CBC\n3. OFB\n4. CFB\n5. CTR\n>>")

        if mode == '1':
            print 'ECB'
            dec_file_ECB('Img/'+ img, key)
        elif mode == '2':
            print 'CBC'
            dec_file_CBC('Img/'+ img, key)
        elif mode == '3':
            print 'OFB'
            dec_file_OFB('Img/'+ img, key)
        elif mode == '4':
            print 'CFB'
            dec_file_CFB('Img/'+ img, key)
        elif mode == '5':
            print 'CTR'
            dec_file_CTR('Img/'+ img, key)

        raw_input("Press enter to continue")
    elif optMenu == "q":                            #Opcion para terminar la ejecucion
        break                                       #Finaliza el programa
    else:
        raw_input("Wrong option...\nPress enter to continue")   #Opcion erronea
