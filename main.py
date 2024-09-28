menu = '''
_______________________________
             MENU

         Deposito [1]
         Saque    [2]
         Extrato  [3]
         Sair     [4]
_______________________________

'''
SALDO = 0 
COUNT = 0 # Contador de saque
deposito = 1
saque = 2
extrato = 3 
sair = 4
historico = []

def depositar(valor):
    global SALDO
    if valor > 0:
        SALDO += valor
        historico.append(f"Depósito de R${valor:.2f}")  # Registra o depósito
        print(f"R${valor:.2f}, depositados. Saldo atual: R${SALDO:.2f}")
    else:
        print("Valor inválido")

def sacar(valor):
    global COUNT
    global SALDO
    if valor > SALDO:
        print("Saldo insuficiente")
    elif valor > 500:
        print("Valor inválido")
    elif COUNT > 3:
        print("Limite de saques diários excedido")
    elif valor < 0:
        print("Valor inválido")
    else:
        SALDO -= valor
        historico.append(f"Saque de R${valor:.2f}")  # Registra o saque
        print(f"R${valor:.2f} sacados com sucesso. Saldo atual: R${SALDO:.2f}")
        COUNT += 1
      
def mostrar_extrato():
    print("Extrato:")
    if not historico:  # Verifica se o histórico está vazio
        print("Nenhuma transação registrada.")
    else:
        for transacao in historico:  # Mostra cada transação registrada
            print(transacao)
    print(f"Saldo atual: R${SALDO:.2f}")

while True:
    print(menu)
    entrada = int(input("Selecione o número: "))
    
    if entrada == sair:
        print("Saindo do sistema...")
        break
    elif entrada == deposito:
        depositar(float(input("Digite o valor: ")))
    elif entrada == saque:
        sacar(float(input("Digite o valor: ")))
    elif entrada == extrato:
        mostrar_extrato()
    else:
        print("Opção inválida")
