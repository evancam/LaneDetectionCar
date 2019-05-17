import bluetooth

bdCarAddr = "B8:27:EB:16:E7:17"
bdBaseAddr = "B8:27:EB:77:22:50"

def serverconnect(port, addr, protocol):
    
    serverSock = bluetooth.BluetoothSocket(protocol)
    serverSock.bind((addr, port))
    serverSock.listen(1)
    clientSock, address = serverSock.accept()

    return (serverSock, clientSock)

def clientconnect(port, addr, protocol):

    sock = bluetooth.BluetoothSocket(protocol)
    sock.connect((addr, port))

    return sock

