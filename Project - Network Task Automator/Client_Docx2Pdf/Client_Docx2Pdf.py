import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)

fliename="Hi.docx"
#filepath="C:\Users\Habiba\OneDrive\Desktop\networks pro\Hi.docx"

client_socket.send(fliename.encode('utf-8'))
print("name sent successfully!")

# client_socket.send(fliename.encode())
# print("name sent successfully!")

client_socket.close()