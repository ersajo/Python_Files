import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 7000))
server.listen(1)
client, addr = server.accept()

while True:
    recibido = client.recv(1024)
    if recibido == "close":
        break
    print str(addr[0]) + " dice: ", recibido
    client.sendall("Holo" + str(54))

print "Adios."

client.close()
server.close()
