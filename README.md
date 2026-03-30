# Distributed Leaderboard System

## Overview

This project implements a **Distributed Leaderboard System** using **TCP socket programming in Python**.
Multiple clients can connect to a central server, submit scores, and retrieve a dynamically updated leaderboard.

The system supports **concurrent clients** using multithreading and ensures **data consistency** using synchronization mechanisms.

---

## Features

* Multi-client support using threads
* Real-time leaderboard updates
* Sorted leaderboard display (highest score first)
* Persistent client-server communication
* Basic input validation and error handling
* Thread-safe updates using locks (mutex)

---

## Architecture

The system follows a **client-server model**:

* **Server**

  * Listens for incoming connections
  * Handles each client in a separate thread
  * Maintains a shared leaderboard

* **Client**

  * Connects to server via TCP
  * Sends commands (SEND, GET, EXIT)
  * Displays server responses

---

## Communication Protocol

The system uses a simple text-based protocol:

| Command                   | Description                  |
| ------------------------- | ---------------------------- |
| `SEND <username> <score>` | Adds or updates user score   |
| `GET`                     | Retrieves sorted leaderboard |
| `EXIT`                    | Closes connection            |

---

## Technologies Used

* Python
* Socket Programming (TCP)
* Multithreading (`threading` module)

---

## How to Run

### 1. Start Server

```bash
python server.py
```

### 2. Start Client

```bash
python client.py
```

---

## Multi-Device Setup (Optional)

To run on multiple laptops:

1. Connect both devices to the same network
2. On server:

   * Set host to `0.0.0.0`
3. On client:

   * Set server IP (e.g., `192.168.x.x`)
4. Run server first, then client

---

## Example Usage

```
Client 1:
SEND Alice 100

Client 2:
SEND Bob 80

Client:
GET

Output:
Alice: 100
Bob: 80
```

---

## Performance Evaluation

* Tested with multiple concurrent clients (3–5)
* Server handled simultaneous requests with minimal latency
* Thread-based concurrency ensured efficient request handling

---

## Error Handling

* Handles abrupt client disconnections
* Validates input format
* Prevents race conditions using locks

---

## Future Enhancements

* Secure communication using SSL/TLS
* User authentication system
* Persistent database storage
* GUI-based client interface

---

## Conclusion

This project demonstrates a **concurrent client-server system** with real-time data updates and synchronization. It effectively showcases concepts of **socket programming, multithreading, and distributed system design**.
