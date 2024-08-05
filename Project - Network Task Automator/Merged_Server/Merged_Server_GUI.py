from socket import *
from pydocx import PyDocX as pydoc
from fpdf import FPDF as fpdf
from docx2pdf import convert
from ipaddress import ip_address
from PIL import Image
from threading import *
import os
import nmap
import pythoncom

#Function that handles WORD2PDF CONVERSION
def Word2PDF_handler(connectionSocket):
    filename = connectionSocket.recv(1024).decode()
    print(filename)
    # filenamex=open("C:\\Users\\Habiba\\OneDrive\\Desktop\\networks pro\\Hi.docx","w")
    pythoncom.CoInitialize()
    convert(filename)
    #print("Error converting the file:", str(e))
    connectionSocket.close()

#Function that handles IMAGE CONVERSION
def ImageConversion_handler(connectionSocket):
    
    name, path, format = [i for i in connectionSocket.recv(2048).decode('utf-8').split('\n')]

    print(f"Received{name}")
    print(f"Received {path}")
    print(f"Received {format}")
    SavedImage = name + '.' + format

    im = Image.open(path) #open image
    im.save(SavedImage)
    im.close()

    # Delete the original image file
    #os.remove(ImagePath.decode())
    # im.save(SavedImage, format=ImageFormat)
    print("Image successfully converted!")
    connectionSocket.close()

#Function that returns the range of IPs in a list[]
def ips(start, end):
    '''Return IPs in IPv4 range, inclusive.'''
    start_int = int(ip_address(start).packed.hex(), 16)
    end_int = int(ip_address(end).packed.hex(), 16)
    # return ip_address(i)
    return [ip_address(ip).exploded for ip in range(start_int, end_int)]

#Function that handles NETWORK CONFIGURATION
def Configuration_client(conn):
    global i
    assigned_ip = ip_addresses[i]
    i=i+1
    conn.sendall(assigned_ip.encode('utf-8'))
    conn.close

#Function that handles NETWORK EQUATIONS
def Equations_handler(connectionSocket): # this function will run in parallel due to threads
    # length = connectionSocket.recv(2048)
    # print("received l")
    # rate = connectionSocket.recv(2048)
    # print("received r")

    length, rate = [int(i) for i in connectionSocket.recv(2048).decode('utf-8').split('\n')]

    TransDelay = int(length)/int(rate)
    print(TransDelay)

    connectionSocket.send(bytes(str(TransDelay),"utf-8"))
    connectionSocket.close()

#Function that handles NETWORK STATISTICS
def Statistics_handler(connectionSocket):
    command = connectionSocket.recv(1024).decode()
    #Name of the file
    statfile = "Network_Statistics.txt"
    #Range of ports to be scanned
    begin = 20
    end = 25
    #Instantiate a PortScanner object
    scanner = nmap.PortScanner()
    txtfile = open (statfile, "w")
    #Loop to scan the range of ports
    for i in range(begin,end+1):
        #Scan the target port
        res = scanner.scan(ServerIP,str(i))
        #The result is a dictionary containing several information we only need to check if the port is opened or closed so we will access only the state
        res = res['scan'][ServerIP]['tcp'][i]['state']
        result = f'port {i} is {res}'
        txtfile.write(result)           
        txtfile.write("\n")
    txtfile.close()
    #File transmission
    with open (statfile,'rb') as file:
        stat_data = file.read()
    connectionSocket.sendall(stat_data)
    connectionSocket.close()

#Function that handles NETWORK ALARM
def Alarm_handler(connectionSocket):
    receivedPort = connectionSocket.recv(2048)
    #Receive port number from client to check its state
    PortNumber = receivedPort.decode()
    print(f"Received {PortNumber}")
    #Instantiate a PortScanner object
    scanner = nmap.PortScanner()
    res = scanner.scan(ServerIP, PortNumber)
    #Get the state -> open/closed
    res = res['scan'][ServerIP]['tcp'][int(PortNumber)]['state']
    #Declare a network alarm in case the port is closed
    if (res == 'closed'):
        lbl = (f"NETWORK ALARM!!! PORT {PortNumber} is {res}")
    elif (res == "open"):
        lbl = (f"PORT {PortNumber} is {res}")
    connectionSocket.sendall(bytes(lbl,"utf-8"))
    connectionSocket.close()

#Function that handles AUDIO/VIDEO FILE TRANSMISSION
def Audio_handler(connectionSocket):
    audio_file = connectionSocket.recv(1024).decode()
    #Reads the audio file as bytes/binary
    src = "../" + audio_file
    with open (src,'rb') as file:
        audio_data = file.read()
    print(f"Server audio file = {audio_file}")
    connectionSocket.sendall(audio_data)
    print(f"audio file sent")
    connectionSocket.close()

#Function that handles RENAMING FILES
def Rename_handler(connectionSocket):
    # Receive the rename command from the client
    data = connectionSocket.recv(1024).decode()
    command, old_filename, new_filename = data.split()
    # Rename the file
    try:
        os.rename(old_filename, new_filename)
        response = f"File '{old_filename}' renamed to '{new_filename}'"
    except OSError as e:
        response = f"Error renaming file: {e}"
    # Send the response back to the client
    connectionSocket.sendall(response.encode())
    connectionSocket.close()

#Function that handles all connections and sends each one to the right function
def Connection_handler(SOKET, handler, socket_label):
    while True:
        connectionSocket, client_addr = SOKET.accept()
        print(f"Client {client_addr} is connected on {socket_label}")
        thread = Thread(target = handler, args=(connectionSocket,))
        thread.start()

#SERVER
ServerIP = "127.0.0.1"

#Variables
messages =[]
HEADER = 64 #how many bytes we will gonna receive are specified in the header
FORMAT = 'utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"

#Global counters
i=0     # defined for ip addresses counter
ii=0     # defined for the Delay counter to shift the array 4 places if the code runs more than 1 time

#PORTS
StatPort = 13000
AudioPort = 13001
RenamePort = 13002
EquationsPort = 5050 
ConfigurationPort = 5060
AlarmPort = 12000
ImagePort = 12001
Word2PdfPort = 12345 

#SOCKETS

#Socket for Network configuration server
ADDR2 = (ServerIP,ConfigurationPort)
Configuration_Socket = socket(AF_INET,SOCK_STREAM) #creating socket (family,type)
Configuration_Socket.bind(ADDR2) # to bind we must have ip and port number
Configuration_Socket.listen(5)

#Socket for Equations server
ADDR1 = (ServerIP,EquationsPort)
Equations_Socket = socket(AF_INET,SOCK_STREAM) #creating socket (family,type)
Equations_Socket.bind(ADDR1) # to bind we must have ip and port number
Equations_Socket.listen(5)

#Socket for RENAMING FILES server
RenameSocket = socket(AF_INET, SOCK_STREAM)
RenameSocket.bind((ServerIP, RenamePort))
RenameSocket.listen(5)

#Socket for AUDIO/VIDEO server
AudioSocket = socket(AF_INET, SOCK_STREAM)
AudioSocket.bind((ServerIP, AudioPort))
AudioSocket.listen(5)

#Socket for NETWORK STATISTICS server
StatSocket = socket(AF_INET, SOCK_STREAM)
StatSocket.bind((ServerIP, StatPort))
StatSocket.listen(5)

#Socket for NETWORK ALARM server
AlarmSocket = socket(AF_INET, SOCK_STREAM)
AlarmSocket.bind((ServerIP, AlarmPort))
AlarmSocket.listen(5)

#Socket for IMAGE CONVERSION Server
ImageSocket = socket(AF_INET, SOCK_STREAM)
ImageSocket.bind((ServerIP, ImagePort))
ImageSocket.listen(5)

#Socket for WORD2PDF CONVERSION server
Word2PdfSocket = socket(AF_INET, SOCK_STREAM)
Word2PdfSocket.bind((ServerIP, Word2PdfPort))
Word2PdfSocket.listen(5)

print("The server is ready to receive")

#THREADS

#Renaming thread
Rename_Thread = Thread (target= Connection_handler, args = (RenameSocket, Rename_handler, "Renaming port 13002"))
Rename_Thread.start()

#Statistics thread
Stat_Thread = Thread (target= Connection_handler, args = (StatSocket, Statistics_handler, "Statistics port 13000"))
Stat_Thread.start()

#Audio thread
Audio_Thread = Thread (target= Connection_handler, args = (AudioSocket, Audio_handler, "Audio port 13001"))
Audio_Thread.start()

#Equations  thread
Equations_Thread = Thread (target= Connection_handler, args = (Equations_Socket, Equations_handler, "Equations port 5050"))
Equations_Thread.start()

#Configuration thread
ip_addresses= ips('192.168.174.2','192.168.174.253')
Configuration_Thread = Thread (target= Connection_handler, args = (Configuration_Socket, Configuration_client, "Configuration port 5060"))
Configuration_Thread.start()

#Alarm thread
Alarm_Thread = Thread (target= Connection_handler, args = (AlarmSocket, Alarm_handler, "Alarm port 12000"))
Alarm_Thread.start()

#Image Thread
Image_Thread = Thread (target= Connection_handler, args = (ImageSocket, ImageConversion_handler, "Image conversion on port 12001"))
Image_Thread.start()

#Word2Pdf Thread
Word2Pdf_Thread = Thread (target= Connection_handler, args = (Word2PdfSocket, Word2PDF_handler, "Word2Pdf on port 12345"))
Word2Pdf_Thread.start()