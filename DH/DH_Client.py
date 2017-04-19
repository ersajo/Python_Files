import socket

client = socket.socket()
client.connect(('192.168.0.16', 7000))

while True:
    mensaje = raw_input("Mensaje a enviar >>")
    client.send(mensaje)
    if mensaje == "close":
        break
    print client.recv(10)
print "Adios."

client.close()
