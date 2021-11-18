#!/usr/bin/python3
import socket
import threading
import subprocess

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((bind_ip, bind_port))
server.listen(5)

print("* Listening on %s:%d" % (bind_ip, bind_port))

def handle_client(client_socket):
	while True:
		client_socket.send(b"Input (a) name(s) of file/directory => ")
		request = client_socket.recv(1024).decode().strip()
		print("* Received: %s" % request)
		if (request == "end"):
			break
		
		command = "ls " + request
		print(command)
		subprocess.run(command, shell=True, stdout=client_socket, stderr=client_socket, text=True)
	client_socket.close()

while True:
	client, addr = server.accept()
	print("* Accepted connection from: %s:%d" % (addr[0], addr[1]))

	client_handler = threading.Thread(target=handle_client, args=(client,))
	client_handler.start()
