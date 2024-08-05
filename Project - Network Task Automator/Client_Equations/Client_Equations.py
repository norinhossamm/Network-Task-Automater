import socket

# Notice that that we follow protocol taht the first message w send is the length of the messages about  yo come

#Every thing in capital is constants
PORT =5050 # port number
HEADER = 64 #how many bytes we will gonna receive are specified in the header
FORMAT = 'utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"

# SERVER="192.168.174.1"
SERVER= "127.0.0.1"
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creating socket (family,type)
client.connect(ADDR)

def send(msg):
    flag = 0
    message = msg.encode(FORMAT) #TO encode the messages to bytes
    msg_Length = len(message)
    send_Length=str(msg_Length).encode(FORMAT)
    # because not every time we have 64 bits (64 -send_Length)  
    send_Length += b' '* (HEADER - len(send_Length))   #byte represntation of this string
    client.send(send_Length)
    client.send(message)
    res = client.recv(2048).decode(FORMAT)
    if res != '0' :
        print("The Total delay = ",res)
    
    # print(res)

print("Enter the Length of bits please")
send(input())
print("Enter the Rate of Transimission please")
send(input())
print("Enter the distance please")
send(input())
print("Enter the Speed please")
send(input())
# send("!DISCONNECT")
# send("10")
# send("2")
# send(DISCONNECT_MESSAGE)
