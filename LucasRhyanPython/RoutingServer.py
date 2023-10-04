import socket
HOST = 'localhost'

ROUTERPORT = 50000
SORTINGPORT = 50010
SUMPORT = 50020

RouterSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
RouterSocket.bind((HOST,ROUTERPORT))
RouterSocket.listen()
print('Aguardando conexao de um cliente')

#CONEXAO INICIAL AO SERVIDOR DE SOMA
SumSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SumSocket.connect((HOST, SUMPORT))
SumSocket.sendall(str.encode("PING"))
if (SumSocket.recv(1024).decode() == "OK"): print("conexao ok")


#CONEXAO INICIAL AO SERVIDOR DE ORDENACAO
SortSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SortSocket.connect((HOST, SORTINGPORT))
SortSocket.sendall(str.encode("PING"))
if (SortSocket.recv(1024).decode() == "OK"): print("conexao ok")


while True:
     conn, ender = RouterSocket.accept()
     data = conn.recv(1024)
     received_data = data.decode()
     print('Conectador em', ender)

     response = "Erro"
     action,content = received_data.split(':')
     
     if (action== '1'):
          SumSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          SumSocket.connect((HOST, SUMPORT))
          SumSocket.sendall(str.encode(content))

          response = SumSocket.recv(1024)
     elif(action == '2'):
          SortSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          SortSocket.connect((HOST, SORTINGPORT))
          SortSocket.sendall(str.encode(content))
          response = SortSocket.recv(1024)

     conn.sendall(response)
     if not data:
         continue
 

