import socket

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
