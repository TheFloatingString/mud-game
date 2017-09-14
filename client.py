import socket
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.connect(("localhost",9999))
while True:
  message = raw_input("type a message: ")
  lenght = len(message)
  serversocket.send(message)

a = serversocket.recv(lenght)

print a
