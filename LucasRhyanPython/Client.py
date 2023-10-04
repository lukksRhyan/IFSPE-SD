import socket

def msg_values() -> list[int]:
    values = []

    while(True):
      val = input("Insira um número: \n")
      if(not val.isnumeric()):
         break
      values.append(val)
            
    
    return values

def msg_values_str(int_values) -> list[str]:
   str_values = []
   for val in int_values: str_values.append(str(val))
   return str_values

def msg_values_int(str_values) -> list[int]:
   int_values = []
   for val in str_values: int_values.append(int(val))
   return int_values


HOST = '127.0.0.1'
ROUTERPORT = 50000

while True:
    #define qual a funcao
    print("Escolha a acao:")
    action = input("1.Somar numeros 2.Ordenar numeros:\n")
    
    #chama a funcao para definir os numeros
    content = ','.join(msg_values_str(msg_values()))
    message = ':'.join([action, content])
    #message = str(action + ':' + content)

    print(content)

    #conexao
    RouterSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    RouterSocket.connect((HOST, ROUTERPORT))
    RouterSocket.sendall(str.encode(message))

    data = RouterSocket.recv(1024)
    print('Mensagem de retorno:', data.decode())

