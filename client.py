import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

file_loc = input("Digite o caminho do arquivo:")

IP_dest = input("Digite o ip de destino:")

file_2_trans = open(file_loc,"rb")

file_format = file_loc.split(".")

my_socket.send(file_format[-1])

while True:
	r = file_2_trans.read(1024)
	
	if not sending: break

	my_socket.send(r)

