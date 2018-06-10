import socket
import re
import os
import sys

from util.format import byte_to_string

PORT_DEST = 5000 #porta padrão do servidor

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file_loc = input("Digite o caminho do arquivo:")
ip_dest = input("Digite o ip de destino:")
file = open(file_loc,"rb")
file_size = os.path.getsize(file_loc)
file_name = re.split(r'[\\/]', file_loc)[-1] #pega o nome do arquivo tanto o caminho no padrão C:/User quanto C:\User

print("Nome do arquivo a ser transferido: ", file_name)
file_size_array = byte_to_string(file_size).split(" "); 
print("Tamanho do arquivo: ",round(float(file_size_array[0]), 2)," ",file_size_array[1])

my_socket.connect((ip_dest, PORT_DEST))
my_socket.send(file_name.encode()) #envia o nome do arquivo ao servidor
my_socket.recv(1024) #recebe a confirmacao que o servidor recebeu o nome
my_socket.send(str(file_size).encode())
my_socket.recv(1024);

if file_size > 0:
  perc_per_iter = float(1024*100/file_size) # porcentagem de quanto é transferido por iteração
else:
  perc_per_iter = 100
perc = perc_per_iter

while True:
  r = file.read(1024)
  if not r: break
  my_socket.send(r) #envia 1024 bytes lidos do arquivo para o servidor
  print('\r{}% transferido.'.format(min(100, int(perc))), end='',)
  perc += perc_per_iter 

print('\nArquivo tranferido!')

my_socket.close()