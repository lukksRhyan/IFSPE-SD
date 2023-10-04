import socket
HOST = 'localhost'
SUMPORT = 50020

RouterSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
RouterSocket.bind((HOST,SUMPORT))
RouterSocket.listen()
print('Aguardando conexao de um cliente')

while True:
    conn, ender = RouterSocket.accept()
    data = conn.recv(1024)
    print('Conectador em', ender)

    if not data:
        continue
    
    received_data = data.decode()
    if(received_data == 'PING'):
        conn.sendall(str.encode("OK"))
        continue
    if (received_data== 'close'):
        print("Encerrando conexao")
        conn.close()

    received_data = received_data.split(',')
    print(received_data)
    #Cria uma list vazia para receber somente int e converte os str
    total = 0
    for val in received_data: 
        total += (int(val))
        print(val)
        print(total)
    #transforma o resultado para uma str e o envia de volta
    conn.sendall(str.encode(str(total)))