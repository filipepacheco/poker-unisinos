import socket

HOST = 'localhost'
PORT = 50000

# AF_INET: IPV4
# SOCK_STREAM: TCP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print("Wait for connection of client")
connection, address = s.accept()

print("Connected on", address)

while True:
    data = connection.recv(1024)
    if not data:
        print("close connection")
        connection.close()
        break
    connection.sendall()
