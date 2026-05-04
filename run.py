from socket   import *         #-
from time     import sleep     #-
from random   import *         #-
from constRPC import *         #-
#-
from client   import *         #-
from server   import *         #-
from dbclient import *         #-

def executar_servidor():
  print(f"--- Iniciando MODO SERVIDOR no IP {HOST_SERVER} ---")
  # O servidor escuta em todas as interfaces ('')[cite: 1]
  s = Server(PORTS) 
  s.run()[cite: 1]

def executar_cliente1():
  print(f"--- Iniciando MODO CLIENTE 1 (Criador) ---")
  c1 = Client(PORTC1)[cite: 5]
  # Conecta ao IP central do servidor definido no constRPC
  dbC1 = DBClient(HOST_SERVER, PORTS)[cite: 4, 5]
    
  print("Criando lista remota...")
  dbC1.create()[cite: 5]
  dbC1.appendData('Dado da Máquina Cliente 1')[cite: 5]
    
  print(f"Enviando Stub para Cliente 2 em {HOST_C2}...")
  # Envia o objeto stub inteiro para o IP do Cliente 2[cite: 5]
  c1.sendTo(HOST_C2, PORTC2, dbC1)[cite: 5]
  print("Objeto enviado com sucesso.")

def executar_cliente2():
  print(f"--- Iniciando MODO CLIENTE 2 (Receptor) ---")
  c2 = Client(PORTC2)[cite: 5]
    
  print("Aguardando objeto Stub da Máquina Cliente 1...")
  data = c2.recvAny()[cite: 2, 5]
  dbC2 = pickle.loads(data)[cite: 5]
    
  print("Stub recebido! Adicionando dados à lista compartilhada...")
  dbC2.appendData('Dado da Máquina Cliente 2')[cite: 5]
    
  print("Resultado final obtido do servidor:")
  print(dbC2.getValue())[cite: 5]
    
  # Encerra o servidor remotamente[cite: 5]
  c2.sendTo(HOST_SERVER, PORTS, [STOP])[cite: 5]

if __name__ == "__main__":
  if len(sys.argv) < 2:
      print("Uso: python run.py [1|2|3]")
      print("1 = Servidor, 2 = Cliente 1, 3 = Cliente 2")
      sys.exit(1)

  escolha = sys.argv[1]

  if escolha == '1':
      executar_servidor()
  elif escolha == '2':
      executar_cliente1()
  elif escolha == '3':
      executar_cliente2()
  else:
      print("Parâmetro inválido. Use 1, 2 ou 3.")
