from socket import *
import os

serverIP = "127.0.0.1"
serverPort = 13002

clientSocket = socket(AF_INET, SOCK_STREAM) 

clientSocket.connect((serverIP,serverPort))


old_filename = input("Enter old file name: ")
new_filename = input("Enter new file name: ")
command = f'RENAME {old_filename} {new_filename}'
clientSocket.sendall(command.encode())

print(clientSocket.recv(1024).decode())


clientSocket.close() 