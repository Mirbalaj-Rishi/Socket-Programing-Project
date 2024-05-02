print("This Program Was Made By Mirbalaj Rishi")
import socket
import threading
global FORMAT
FORMAT = 'utf-8'
global DISCONNECTMESSAGE
DISCONNECTMESSAGE = "!Disconnect"
print("""
------------------------------------------------------------------------
This code was written by Mirbalaj Rishi
UI Comming Soon
------------------------------------------------------------------------
""")

#___________________________________
# general purpose menu system by Mirbalaj Rishi



def mainMenu(Option1, Option2):
    goodChoice = "no"
    while goodChoice == "no":
        userChoice = input(f"""
Please Input Your Choice
1.{Option1}
2.{Option2}

""").lower()
    
        print()
        if userChoice == "1" or userChoice == Option1.lower():
            goodChoice = "yes"
            return Option1
        elif userChoice == "2" or userChoice == Option2.lower():
            goodChoice = "yes"
            return Option2
        else:
            goodChoice = "no"
            print("please choose one of the options below")



#-----------------------------------------------------



class interface: # sets up the interface that the user will use to set up the server or connect to the server
    def __init__(self,machineName,IP,portNumber): #sets default values and asks the user if they want to change it
        self.machineName = machineName
        self.myIP = IP
        self.portNumber = portNumber
        storeHistory = "ask"
        self.storeHistory = storeHistory
    def questions(self): # changes stuff
        
        

        #ADD MACHINENAME AND STOREHISTORY OPTIONS
    
        
        

        print(f"""Your Current Display Name Is {self.machineName}.
        Would you like to change it?""")
        machineUpdate = mainMenu("y", "n")
        if machineUpdate == "y":
            self.machineName = input("please type what you want your display name to be: ")
        print("")
        print(f"Would you like to specify the port number? [the default is {self.portNumber}]")
        socketUpdate = mainMenu("y", "n")
        if socketUpdate == "y":
            portNumber = int(input("please type in the port you want to use: "))

class chatCode: #this is used by the server and client to send chat messages 
    def __init__ (self, machineName,socketName):
        self.myName = machineName
        self.storeHistory = "no"
        self.socketName = socketName
    
    def receiveFunction(self): # this is used for an individual connection 
        connected = True
        
        #otherName = "someone"
        #print(f"| {otherName}, connected |")
        while connected:
            message = self.socketName.recv(2048).decode(FORMAT)
            if message != "":
                print(f"{message}")
            if message == DISCONNECTMESSAGE: # this disconnects the client from the server to prevent issues disconnecting 
                connected = False
    def receive(self): # this is used to thread the receive function
        threadReceive = threading.Thread(target= (self.receiveFunction), args= ()) 
        threadReceive.start()
        
    
    def sendFunction(self, myName): # this is used to send stuff to an individual
        self.socketName.send(bytes(f"| {self.myName}: Connected |", FORMAT)) 
        while True:
            userInput = input()
            if userInput == "!CMD":
                print("| Commands Comming Soon |")
            else:
                self.socketName.send(bytes(f"{self.myName}: {userInput}", FORMAT))
                print("| Message Sent |")
    def send(self): # this is used to thread sendFunction
        
        threadSend = threading.Thread(target= (self.sendFunction), args= (self.myName,)) 
        threadSend.start()
        

        
class serverCode: # this is run exclusivly by the server 
    def __init__ (self, machineName, portNumber, IP):
        self.machineName = machineName
        self.portNumber = portNumber
        self.myIP = IP
    #function ideas [ip ban] [make a keyword paste something] [change port] [transfer owner] 
    """
    def clientConnection(connection, clientAddress):
        connected = True
        
        clientName = "Someone"
        print(f" {clientName}, connected ")
        while connected:
            message = connection.recv(2048).decode(FORMAT)
            if message == DISCONNECTMESSAGE: # this disconnects the client from the server to prevent issues disconnecting 
                connected = False
            print(f"{clientName}: {message}")
    """
    def serverRun(self): # this gets the server to run 
        displayIP = "XXX.XXX.XXX.XXX"
        displayIP = self.myIP
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind((self.myIP, self.portNumber))
        print("| Server Is Starting..... |")
        print(f"| Please Connect to {displayIP} |")
        serverSocket.listen() #listen for connection
        conn,addr = serverSocket.accept()
        chatting = chatCode(self.machineName,conn)
        chatting.receive()
        chatting.send()
        """
        while True:
            thread1 = threading.Thread(serverSocket.listen())
            thread1.start()
            connection, clientAddress = serverSocket.accept() #this will allow to get the address we are connected and information about the connect
           #This allows us to handle mutiple clients by creating a new thread for each client
            print(f" Active connections {threading.active_count() - 2} ") #the start thread counts as a thread so total threads are client threads + start thread
        """   

class clientCode: # this is run exclusivly by the client 
    def __init__(self, machineName, portNumber, IP):
        self.machineName = machineName
        self.serverPortNumber = portNumber
        self.serverIP = IP

    def clientRun(self): # this runs the client 
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        clientSocket.connect((self.serverIP, self.serverPortNumber)) 
        
        chatting = chatCode(self.machineName,clientSocket)
        chatting.receive()
        chatting.send()
           
        
        




# RUN CODE



serverOrClient = "helloIAmAVariable"
"""this will prompt the user server or client and call the class that is needed"""

machineName = socket.gethostname()
IP = socket.gethostbyname(socket.gethostname())
port = 6060
                          
serverOrClient = mainMenu("server", "client") #ask user if server or client
userInput = interface(machineName,IP,port)
userInput.questions()
if serverOrClient == "server":
    server = serverCode(userInput.machineName, userInput.portNumber, userInput.myIP)
    print("---------------------------------------------------------------------------------------")
    server.serverRun()
elif serverOrClient == "client":
    client = clientCode(userInput.machineName, userInput.portNumber, input("Please give the IP address of the server you want to connect to: "))
    print("---------------------------------------------------------------------------------------")
    client.clientRun()
    




    
    

