import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.bind(('127.0.0.1', 5000))
my_socket.listen(1)

print("I'm waiting files, where are they?")

while True:
    conn, addr = my_socket.accept()
    
    print("I started receiving a file, yey!")
    
    file_name = conn.recv(1024) #recebe o nome do arquivo
    w = open(file_name.decode(), 'wb')
    conn.send("name-received".encode()) #envia a confirmacao de nome de arquivo recebido
    
    piece = conn.recv(1024) #recebe o primeiro pedaço do arquivo
    
    while piece:
        w.write(piece)  
        piece = conn.recv(1024) 
    
    print("Received " + file_name.decode() + " successfully.")
    w.close()
    conn.close()