import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)

print ("Starting server on " + str(server_address))

sock.listen(1)

while (1):
	connection, client_address = sock.accept()

try:
	print ("Connected to " + str(client_address))

	while (1):
		data = connection.recv(16)
		if data:
			print ("Got " + data + " from client")
			connection.sendall(data)
		else:
			print ("No more data from " + str(client_address))
			break

finally:
	print ("Closing connection")
	connection.close()

