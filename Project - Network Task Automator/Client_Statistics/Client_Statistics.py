from socket import *
import os

serverIP = "127.0.0.1"
StatPort = 13000

clientSocket = socket(AF_INET, SOCK_STREAM) 

clientSocket.connect((serverIP,StatPort))

command = "SCAN"
clientSocket.sendall(command.encode())

stat_data = clientSocket.recv(200000)

with open('Statistics.txt','wb') as file: #File received 
    file.write(stat_data)

print('Statistics file received!')

clientSocket.close() 
