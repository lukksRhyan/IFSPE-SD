import socket
HOST = 'localhost'
SORTINGPORT = 50010

RouterSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
RouterSocket.bind((HOST,SORTINGPORT))
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
 
     #Cria uma list vazia para receber somente int e converte os str
     data_to_int = []
     for val in received_data: data_to_int.append(int(val))
     #organiza os int
     data_to_int.sort()
 
     #desfaz o processo de conversao transformando de volta em uma lista de str
     final_data = []
     for val in data_to_int: final_data.append(str(val)) 
     print(final_data)
     #transforma os dados em uma unica str e os envia de volta
     conn.sendall(str.encode(','.join(final_data)))