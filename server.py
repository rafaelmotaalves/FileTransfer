import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.bind(('127.0.0.1', 5000))
my_socket.listen(1)

print("I'm waiting files, where are they?")

while True:
    conn, addr = my_socket.accept()
    
    print("I started receiving a file, yey!")
    
    file_name = conn.recv(1024) #recebe o nome do arquivo
    conn.send("name-received".encode()) #envia a confirmacao de nome de arquivo recebido
    file_size = int(conn.recv(1024).decode())
    conn.send("size-received".encode())
    w = open(file_name.decode(), 'wb')
    


    if file_size > 0:
      perc_per_iter = float(1024*100/file_size) # porcentagem de quanto é transferido por iteração
    else:
      perc_per_iter = 100
    perc = perc_per_iter
    piece = conn.recv(1024) #recebe o primeiro pedaço do arquivo
    
    while piece:
        w.write(piece)
        print('\r{}% recebido.'.format(min(100, int(perc))), end='',)
        piece = conn.recv(1024)
        perc += perc_per_iter 
    
    print("\nReceived " + file_name.decode() + " successfully.")
    w.close()
    conn.close()