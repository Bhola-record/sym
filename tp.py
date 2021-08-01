import socket

r = socket.socket()
host = input("Enter Key :")
port = 8080

r.connect ((host, port))
print ("Connected")
