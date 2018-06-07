import socket
import re

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file_loc = input("Digite o caminho do arquivo:")
ip_dest = input("Digite o ip de destino:")
file = open(file_loc,"rb")
file_name = re.split(r'[\\/]', file_loc)[-1] #pega o nome do arquivo tanto o caminho no padrão C:/User quanto C:\User

my_socket.connect((ip_dest, 5000))

my_socket.send(file_name.encode()) #envia o nome do arquivo ao servidor
my_socket.recv(1024) #recebe a confirmacao que o servidor recebeu o nome

while True:
	r = file.read(1024)
	if not r: break
	my_socket.send(r) #envia 1024 bytes lidos do arquivo para o servidor

my_socket.close()