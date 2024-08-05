from socket import *
serverIP = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP,serverPort))

PortNumber = input('Enter a port number to check its state: ')
clientSocket.send(bytes(PortNumber,"utf-8"))


# modifiedSentence = clientSocket.recv(1024)
# print('From Server:', modifiedSentence.decode("utf-8"))
clientSocket.close()