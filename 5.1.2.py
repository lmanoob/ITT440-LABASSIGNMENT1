import socket

 

localIP     = "192.168.50.164"

port   = 8888

bufferSize  = 1024

 

msgFromServer       = "Hello UDP Client"

bytesToSend         = str.encode(msgFromServer)

 

# Create a datagram socket

s = socket.socket()
print("Berjaya buat sokett")


 

# Bind to address and ip

s.bind(('', port))
print("Berjaya bind soket di port: " + str(port))

 

# Listen for incoming datagrams

while(True):

    bytesAddressPair = s.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

   

    # Sending a reply to client

    s.sendto(bytesToSend, address)