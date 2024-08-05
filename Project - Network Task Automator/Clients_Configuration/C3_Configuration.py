import socket

PORT =5060# port number
HEADER = 64 #how many bytes we will gonna receive are specified in the header
FORMAT = 'utf-8'

# SERVER="192.168.174.1"
SERVER= "127.0.0.1"
ADDR = (SERVER,PORT)


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creating socket (family,type)
client.connect(ADDR)

ip_address = client.recv(1024).decode('utf-8')
print('Assigned IP address:', ip_address)
client.close()