import os
from Crypto.PublicKey import RSA

def generate_RSA(name):
    new_key = RSA.generate(bits=2048, e=65537)

    publickey = new_key.publickey().exportKey("PEM")
    llavePublica = open(name + "Public.txt", "w")
    llavePublica.write(publickey)
    llavePublica.close()

    privatekey = new_key.exportKey("PEM")
    llavePrivada = open(name + "Private.txt", "w")
    llavePrivada.write(privatekey)
    llavePrivada.close()

def menu():
    os.system('clear')
    print "1. Generate keys."
    print "2. Encrypt file"
    print "3. Decrypt file"
    print "q. Quit"

while True:
    menu()
    optMenu = raw_input ("Choose an option >> ")
    if optMenu == "1":
        name = raw_input("Enter the name to the keys \n>>")
        print "Generating keys"
        generate_RSA(name)
        print "Done!"
        raw_input("Press enter to continue")
    elif optMenu == "2":
        print "Encrypt file"
        raw_input("Press enter to continue")
    elif optMenu == "3":
        print "Decrypt file"
        raw_input("Press enter to continue")
    elif optMenu == "q":
        print "Bye"
        break
    else:
        raw_input("Wrong option...\nPress enter to continue")   #Opcion erronea
