from tkinter import *
from socket import *
from threading import *
import subprocess
import os

TK_SILENCE_DEPRECATION=1

serverIP = "127.0.0.1"

def CallServer():
    file_path = os.path.join("..", "Merged_Server_GUI.py")
    subprocess.call(["python", file_path])

Server_thread = Thread (target= CallServer)

# create root window
root = Tk()
root.title("Network Task Automator")
canvas1 = Canvas(root, width=700, height=100, relief='raised')
canvas1.pack()

Welcome_lbl = Label(root, text = "Welcome", font=('helvetica', 20) )
canvas1.create_window(350, 50, window=Welcome_lbl)
Server_thread.start()

#PORTS
StatPort = 13000
AudioPort = 13001
RenamePort = 13002
EquationsPort = 5050 
ConfigurationPort = 5060
AlarmPort = 12000
ImagePort = 12001


# entry2 = Entry(root)
# entry2.pack()

# def entryfunc ():
#     AlarmSocket = socket(AF_INET, SOCK_STREAM)
#     AlarmSocket.connect((serverIP,AlarmPort))

#     print("inside function")
#     print(f"{entry2.get()}")
#     #Socket for NETWORK ALARM client
#     print("Client is ready to send")
#     AlarmSocket.send(bytes(entry2.get(),"utf-8"))
#     AlarmSocket.close()

# submitbtn =  Button(root, text="Get Input", command=lambda:entryfunc())
# submitbtn.pack()

def NetworkAlarm():
    root.iconify()
    Network_window = Toplevel()
    Network_window.title("Convert Image")
    Network_window.geometry("700x600")

    entry = Entry(Network_window)
    entry.pack()

    
    def getPortNumber(PortNumber):
        AlarmSocket = socket(AF_INET, SOCK_STREAM)
        AlarmSocket.connect((serverIP,AlarmPort))
        print("inside function")
        print(f"{PortNumber}")
        #Socket for NETWORK ALARM client
        
        print("Client is ready to send")
        AlarmSocket.send(bytes(PortNumber,"utf-8"))
        AlarmSocket.close()

    submit = Button(Network_window, text="Get Input", command=lambda:getPortNumber(entry.get()))
    submit.pack()

    def BackCommand():
        Network_window.destroy()
        root.deiconify()

    back_button = Button(Network_window, text="Back", command=BackCommand)
    back_button.pack()



def RenameFile():
      root.iconify()
      Rename_window = Toplevel()
      Rename_window.title("Renaming File")
      Rename_window.geometry("700x600")

      Oldfileinput = Entry(Rename_window)
      Oldfileinput.pack()

      Newfileinput = Entry(Rename_window)
      Newfileinput.pack()

    
      def FileRenamed(old_filename, new_filename):
          RenameSocket = socket(AF_INET, SOCK_STREAM) 

          RenameSocket.connect((serverIP,RenamePort))
          #old_filename = input("Enter old file name: ")
          #new_filename = input("Enter new file name: ")
          command = f'RENAME {old_filename} {new_filename}'
          RenameSocket.sendall(command.encode())

          #print(clientSocket.recv(1024).decode())

          RenameSocket.close() 
    

      submitbtn = Button(Rename_window, text= "Rename", command=lambda:FileRenamed(Oldfileinput.get(),Newfileinput.get()))
      submitbtn.pack()


      def BackCommand():
        Rename_window.destroy()
        root.deiconify()

      back_button = Button(Rename_window, text="Back", command=BackCommand)
      back_button.pack()


def AudioVidTransfer():
      root.iconify()
      Transfer_window = Toplevel()
      Transfer_window.title("Audio/Video Download")
      Transfer_window.geometry("700x600")

      Input = Entry(Transfer_window)
      Input.pack()

      def Transfer(audio_file):
        TransferSocket = socket(AF_INET, SOCK_STREAM) 

        TransferSocket.connect((serverIP,AudioPort))

        #audio_file = input("Which audio file do you want?\n")

        TransferSocket.sendall(audio_file.encode())   
        print(f"audio file = {audio_file}")

        audio_data= TransferSocket.recv(200000)
        
        with open(audio_file,'wb') as file:
           file.write(audio_data)

        #print('File received: ',audio_file)

        TransferSocket.close() 


      transfersubmit = Button(Transfer_window, text= "Download", command=lambda:Transfer(Input.get()))
      transfersubmit.pack()

      def BackCommand1():
            Transfer_window.destroy()
            root.deiconify()

      back_button1 = Button(Transfer_window, text="Back", command=BackCommand1)
      back_button1.pack()



def Word2PDF():
    WTP_socket = socket(AF_INET, SOCK_STREAM)

    # Define the server address and port
    server_address = ('localhost', 12345)

    # Connect to the server
    WTP_socket.connect(server_address)

    fliename="Hi.docx"
    #filepath="C:\Users\Habiba\OneDrive\Desktop\networks pro\Hi.docx"

    WTP_socket.send(fliename.encode('utf-8'))
    #print("name sent successfully!")

    # client_socket.send(fliename.encode())
    # print("name sent successfully!")

    WTP_socket.close()


def Statistics():
    root.iconify()
    Statistics_window = Toplevel()
    Statistics_window.title("Network Statistics")
    Statistics_window.geometry("700x600")
    
    def getStatics(label):
        clientSocket = socket(AF_INET, SOCK_STREAM) 
        clientSocket.connect((serverIP,StatPort))

        command = "SCAN"
        clientSocket.sendall(command.encode())
        stat_data = clientSocket.recv(200000)
        print(stat_data)
        label.config(text= stat_data)


        with open('Statistics.txt','wb') as file: #File received 
            file.write(stat_data)

        output = clientSocket.recv(200000)
        print(output)
        print('Statistics file received!')
        clientSocket.close() 
        

    submit = Button(Statistics_window , text="SCAN!", command=lambda:getStatics(client_lbl))
    submit.pack()
    client_lbl = Label(Statistics_window, text = "", font=('helvetica', 16) )
    client_lbl.pack()

    def BackCommand():
        Statistics_window.destroy()
        root.deiconify()

    back_button = Button(Statistics_window, text="Back", command=BackCommand)
    back_button.pack()


def NetworkAlarm():
    root.iconify()
    Network_window = Toplevel()
    Network_window.title("Network Alarm")
    Network_window.geometry("700x600")

    entry = Entry(Network_window)
    entry.pack()

    
    def getPortNumber(PortNumber, lbl):
        AlarmSocket = socket(AF_INET, SOCK_STREAM)
        AlarmSocket.connect((serverIP,AlarmPort))
        print("inside function")
        print(f"{PortNumber}")
        #Socket for NETWORK ALARM client
        
        print("Client is ready to send")
        AlarmSocket.send(bytes(PortNumber,"utf-8"))
        receivedMsg = AlarmSocket.recv(2048).decode()
        lbl.config(text= receivedMsg)
        AlarmSocket.close()

    submit = Button(Network_window, text="SCAN!", command=lambda:getPortNumber(entry.get(), lbl))
    submit.pack()

    lbl = Label(Network_window, text = "", font=('helvetica', 16) )
    lbl.pack()

    def BackCommand():
        Network_window.destroy()
        root.deiconify()

    back_button = Button(Network_window, text="Back", command=BackCommand)
    back_button.pack()


def Configuration():
    root.iconify()
    config_window = Toplevel()
    config_window.title("Netowrk Configuration")
    config_window.geometry("700x600")

    def getIP(label):
        ConfigClient = socket(AF_INET, SOCK_STREAM) #creating socket (family,type)
        ConfigClient.connect((serverIP,ConfigurationPort))

        ip_address = ConfigClient.recv(1024).decode('utf-8')
        print('Assigned IP address:', ip_address)
        label.config(text= ip_address)

        ConfigClient.close()

    C1_btn = Button(config_window, text="Get IP Address for Client1", command=lambda:getIP(client1_lbl))
    C1_btn.pack()
    client1_lbl = Label(config_window, text = "", font=('helvetica', 16) )
    client1_lbl.pack()

    C2_btn = Button(config_window, text="Get IP Address for Client2", command=lambda:getIP(client2_lbl))
    C2_btn.pack()
    client2_lbl = Label(config_window, text = "", font=('helvetica', 16) )
    client2_lbl.pack()

    C3_btn = Button(config_window, text="Get IP Address for Client3", command=lambda:getIP(client3_lbl))
    C3_btn.pack()
    client3_lbl = Label(config_window, text = "", font=('helvetica', 16) )
    client3_lbl.pack()

    def BackCommand():
        config_window.destroy()
        root.deiconify()

    back_button = Button(config_window, text="Back", command=BackCommand)
    back_button.pack()


def Equations():
    root.iconify()
    Equations_window = Toplevel()
    Equations_window.title("Network Equations")
    Equations_window.geometry("700x600")

    HEADER = 64 #how many bytes we will gonna receive are specified in the header
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE="!DISCONNECT"
    def send(L, R, label):
        print (L,R)

        client = socket(AF_INET, SOCK_STREAM) #creating socket (family,type)
        client.connect((serverIP,EquationsPort))
        
        client.sendall(str.encode("\n".join([str(L), str(R)])))
        # client.send(bytes(L,"utf-8"))
        # client.send(bytes(R, "utf-8"))

        Trans = client.recv(2048).decode(FORMAT)
        print(Trans)
        if Trans != '0' :
            label.config(text= Trans)
        client.close()
    
    entryL = Entry(Equations_window)
    entryL.pack()
    # submitL = Button(Equations_window, text="send length of bits", command=lambda:send(entryL.get()))
    # submitL.pack()
    entryR = Entry(Equations_window)
    entryR.pack()
    submitR = Button(Equations_window, text="calculate transmisstion delay", command=lambda:send(entryL.get(),entryR.get(), client1_lbl))
    submitR.pack()
    client1_lbl = Label(Equations_window, text = "", font=('helvetica', 16) )
    client1_lbl.pack()

    def BackCommand():
        Equations_window.destroy()
        root.deiconify()

    back_button = Button(Equations_window, text="Back", command=BackCommand)
    back_button.pack()


def ConvertImage():
    root.iconify()
    Image_window = Toplevel()
    Image_window.title("Network Equations")
    Image_window.geometry("700x600")

    
    def Convert(name, path, format, label):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverIP,ImagePort))

        clientSocket.sendall(str.encode("\n".join([str(name), str(path), str(format)])))

        label.config(text= "Image has been converted successfully!")
       
        clientSocket.close()
    
    
    entryNewName = Entry(Image_window)
    entryNewName.pack()
    entryPath= Entry(Image_window)
    entryPath.pack()
    entryNewFormat= Entry(Image_window)
    entryNewFormat.pack()
    submit = Button(Image_window, text="Convert Image", command=lambda:Convert(entryNewName.get(),entryPath.get(), entryNewFormat.get(), lbl))
    submit.pack()
    lbl = Label(Image_window, text = "", font=('helvetica', 16) )
    lbl.pack()

    def BackCommand():
        Image_window.destroy()
        root.deiconify()

    back_button = Button(Image_window, text="Back", command=BackCommand)
    back_button.pack()


frame1 = Frame(root)
frame1.pack()


ImageConvert_btn = Button(frame1, text = "Convert an Image" , fg = "white", command=ConvertImage, width=15, height=5, bg="green", font= ('helvetica', 14))
ImageConvert_btn.pack(side="left")

Rename_btn = Button(frame1, text = "Rename a File" , fg = "white", command=RenameFile, width=15, height=5, bg="pink", font= ('helvetica', 14))
Rename_btn.pack(side="left")

AudioTransfer_btn = Button(frame1, text = "Download mp3/mp4" , fg = "white", command=AudioVidTransfer, width=15, height=5, bg="purple", font= ('helvetica', 14))
AudioTransfer_btn.pack(side="left")


frame2 = Frame(root)
frame2.pack()
Statistics_btn = Button(frame2, text = "Network Statistics" , fg = "white", command=Statistics, width=15, height=5, bg="red", font= ('helvetica', 14))
Statistics_btn.pack(side="left")


Alarm_btn = Button(frame2, text = "Network Alarm" , fg = "white", command=NetworkAlarm, width=15, height=5, bg="blue", font= ('helvetica', 14))
Alarm_btn.pack( side="left")


Config_btn = Button(frame2, text = "Configuration" , fg = "white", command=Configuration, width=15, height=5, bg="black", font= ('helvetica', 14))
Config_btn.pack( side="left")


frame3 = Frame(root)
frame3.pack()

WordtoPDF_btn = Button(frame3, text = "Word To PDF" , fg = "white", command=Word2PDF, width=15, height=5, bg="brown", font= ('helvetica', 14))
WordtoPDF_btn.pack(side="left")

Networkeqs_btn = Button(frame3, text = "Network Equations" , fg = "white", command=Equations, width=15, height=5, bg="orange", font= ('helvetica', 14))
Networkeqs_btn.pack(side="left")

# Execute Tkinter
root.mainloop()




# root= tk.Tk()

# root.title("Network Task Automator")
# canvas1 = tk.Canvas(root, width=700, height=600, relief='raised')
# canvas1.pack()

# label1 = tk.Label(root, text='Welcome!')
# label1.config(font=('helvetica', 18))
# canvas1.create_window(320, 25, window=label1)

# # label2 = tk.Label(root, text='Type 1 for SIC or 2 for SICXE:')
# # label2.config(font=('helvetica', 10))
# # canvas1.create_window(200, 100, window=label2)

# # entry1 = tk.Entry(root) 
# # canvas1.create_window(200, 140, window=entry1)

# def clicked():
    
#     lbl = tk.Label(root, text='Welcome!')
#     lbl.config(font=('helvetica', 12))
#     lbl.config(300, 
#         text = "I just got clicked")
 
# # button widget with red color text
# # inside
# btn = tk.Button(root, text = "Click me" ,fg = "red", command=clicked)
# # set Button grid
# btn.config(column=1, row=0)


# root.mainloop()