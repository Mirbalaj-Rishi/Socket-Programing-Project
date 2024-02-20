import socket
import threading
global FORMAT
FORMAT = 'utf-8'
global DISCONNECTMESSAGE
DISCONECTMESSAGE = "!Disconnect"
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



class interface:
    def __init__(self,machineName,IP,portNumber): #sets default values and asks the user if they want to change it
        self.machineName = machineName
        self.myIP = IP
        self.portNumber = portNumber
        storeHistory = "ask"
        self.storeHistory = storeHistory
    def questions(self):
        
        

        #ADD MACHINENAME AND STOREHISTORY OPTIONS
    
        print(f"Would you like to specify the port number? [the default is {self.portNumber}]")
        socketUpdate = mainMenu("y", "n")
        if socketUpdate == "y":
            portNumber = int(input("please type in the port you want to use: "))
        print("")

        print(f"""Your Current Display Name Is {self.machineName}.
        Would you like to change it?""")
        machineUpdate = mainMenu("y", "n")
        if machineUpdate == "y":
            machineName = input("please type what you want your display name to be: ")
            print(machineName)
              

class serverCode:
    def __init__ (self, machineName, storeHistory, portNumber, IP):
        self.machineName = machineName
        self.storeHistory = storeHistory
        self.portNumber = portNumber
        self.hostIP = IP
    #function ideas [ip ban] [make a keyword paste something] [change port] [transfer owner] 
    
    def clientConnection(connection, clientAddress):
        connected = True
        
        clientName = "Will Find Name At Some Point"
        print(f" {clientName}, connected ")
        while connected:
            message = connection.recv(2048).decode(FORMAT)
            if message == DISCONNECTMESSAGE: # this disconnects the client from the server to prevent issues disconnecting 
                connected = False
            print(f"{clientName}: {message}")
    def serverRun(self):
        displayIP = "XXX.XXX.XXX.XXX"
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind((self.hostIP, self.portNumber))
        print("Server Is Starting.....")
        print(f"Please Connect to {displayIP}")
        serverSocket.listen() #listen for connection
        while True:
            thread1 = threading.Thread(serverSocket.listen())
            thread1.start()
            connection, clientAddress = serverSocket.accept() #this will allow to get the address we are connected and information about the connect
            """This allows us to handle mutiple clients by creating a new thread for each client"""
            thread = threading.Thread(target=clientConnection, args=(connection, clientAddress)) 
            thread.start()
            print(f" Active connections {threading.active_count() - 2} ") #the start thread counts as a thread so total threads are client threads + start thread





# RUN CODE



serverOrClient = "helloIAmAVariable"
"""this will prompt the user server or client and call the class that is needed"""

machineName = socket.gethostname()
IP = socket.gethostbyname(socket.gethostname())
port = 6060
                          
serverOrClient = mainMenu("server", "client") #ask user if server or client
userInput = interface(machineName,IP,port)
userInput.questions()
server = serverCode(userInput.machineName, userInput.storeHistory, userInput.portNumber, userInput.myIP)
if serverOrClient == "server":
    print("---------------------------------------------------------------------------------------")
    server.serverRun()



    
    

