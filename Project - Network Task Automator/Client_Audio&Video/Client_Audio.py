from socket import *
import os

serverIP = "127.0.0.1"
AudioPort = 13001

clientSocket = socket(AF_INET, SOCK_STREAM) 


clientSocket.connect((serverIP,AudioPort))

audio_file = input("Which audio/(video) file do you want?\n")

clientSocket.sendall(audio_file.encode())


audio_data= clientSocket.recv(2000000)

with open(audio_file,'wb') as file:
    file.write(audio_data)

print('File received: ',audio_file)


clientSocket.close() 