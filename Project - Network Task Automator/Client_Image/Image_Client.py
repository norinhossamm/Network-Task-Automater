from socket import *
serverIP = "127.0.0.1"
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP,serverPort))

imageName = input('Enter image name: ')
clientSocket.send(bytes(imageName,"utf-8"))

imagePath = input('Enter image path: ')
clientSocket.send(bytes(imagePath,"utf-8"))

imageFormat = input('Enter image new format: ')
clientSocket.send(bytes(imageFormat,"utf-8"))

# modifiedSentence = clientSocket.recv(1024)
# print('From Server:', modifiedSentence.decode("utf-8"))
clientSocket.close()