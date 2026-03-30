from socket import *

servername = "10.20.203.1"
serverport = 12000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((servername,serverport))
username = input ("Enter username: ")
while True:
    print("Distributed Leaderboard System:")
    print("1. Send score")
    print("2. Get leaderboard")
    print("3. Exit")

    sentence = input("Input option(1/2/3): ")
    if(sentence == "1"):
        score = input("Enter score: ")
        sentence = "SEND " + username + " " + score
    
    elif(sentence == "2"):
        sentence = "GET"
    
    elif(sentence == "3"):
        sentence = "EXIT"
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024).decode()
        print("From Server: \n" + modifiedSentence)
        break 
    
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024).decode()
    print("From Server: " + modifiedSentence)
clientSocket.close()
