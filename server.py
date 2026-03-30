from socket import *
import threading 

def logic(connectionSocket):
    print("This will handle the logic of the thread")
    while True:
        sentence = connectionSocket.recv(1024).decode()
        if not sentence:
            break

        arr = sentence.split()
        if(arr[0] == "SEND"):
            if(len(arr) != 3):
                print("Invalid command")
                connectionSocket.send("Invalid command".encode())
                continue

            #update dictionary with {arr[1]: arr[2]}
            username = arr[1]
            score = int(arr[2])+leaderboard[username] if username in leaderboard else int(arr[2])

            with lock:
                leaderboard[username] = score

            print("Updated the leaderboard successfully")
            connectionSocket.send("Updated the leaderboard successfully".encode())

        elif(arr[0] == "GET"):
            #return the dictionary or something 
            print("Return the leaderboard successfully")

            with lock:
                leaderboard_sorted = dict(sorted(leaderboard.items(), key = lambda item: item[1], reverse=True))
            
            result = ""
            for name, score in leaderboard_sorted.items():
                   result += name + ": " + str(score) + "\n"
            print(result)
            connectionSocket.send(result.encode())

        elif(arr[0] == "EXIT"):
            print("Closing the connection")
            connectionSocket.send("Closing the connection".encode())
            break
    
    connectionSocket.close()


servername = "0.0.0.0"
serverport = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((servername,serverport))
serverSocket.listen(5)
print("The server is ready to receive")

leaderboard = {}
lock = threading.Lock()



while True:
    connectionSocket, addr = serverSocket.accept()
    server_thread = threading.Thread(target=logic,args=(connectionSocket,))
    server_thread.start()
    
