import os
from Crypto.Cipher import DES

def menu():                         #Funcion que simulara el menu en el shell
    os.system('clear')              #Limpiamos pantalla del shell
    print ("Choose an option")      #Inicio de menu
    print ("\te - Encrypt")         #Primer opcion
    print ("\td - Decrypt")         #Segunda opcion
    print ("\tq - Quit")            #Opcion para terminar la ejecucion del programa

def enc_file(in_filename, out_filename, key):
    cipher = DES.new(key)

    with open(in_filename, 'r') as in_file:
        with open(out_filename, 'w') as out_file:
            while True:
                chunk = in_file.read()
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                out_file.write(cipher.encrypt(chunk))

def dec_file(in_filename, out_filename, key):
    cipher = DES.new(key)

    with open(in_filename, 'r') as in_file:
        with open(out_filename, 'w') as out_file:
            while True:
                chunk = in_file.read()
                if len(chunk) == 0:
                    break
                out_file.write(cipher.decrypt(chunk).strip())

os.system('clear')
key = raw_input ("Write a key >> ")
while len(key) != 8:
    os.system('clear')
    key = raw_input ("Wrong key, Key must be 8 characters.\n Write another key >> ")
while True: #Ciclo para llamar al menu al finalizar la opcion
    menu()  #Se llama al menu
    optMenu = raw_input ("Choose an option >> ")  #raw_input funciona para leer una cadena
                                                    #Se lee la opcion y se guarda en una variable
    if optMenu == "e":                              #Primer opcion
        print("Encrypt")                            #Para verificar la entrada
        with open('m.txt', 'r') as f:
            print 'm.txt: %s' % f.read().strip()
        enc_file('m.txt','e.txt',key)
        raw_input("Press enter to continue")
    elif optMenu == "d":                            #Segunda opcion
        print("Decrypt")                            #Para verificar la entrada
        with open('e.txt', 'r') as f:
            print 'e.txt: %s' % f.read()
        dec_file('e.txt','d.txt',key)
        raw_input("Press enter to continue")
    elif optMenu == "q":                            #Opcion para terminar la ejecucion
        break                                       #Finaliza el programa
    else:
        raw_input("Wrong option...\nPress enter to continue")   #Opcion erronea
