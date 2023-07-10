class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.limite_diario = 500
        self.saques_realizados = 0
        self.operacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f"Depósito de R${valor:.2f}")

    def sacar(self, valor):
        if self.saques_realizados >= 3:
            self.operacoes.append("Limite máximo de saques diários atingido.")
        elif valor > self.limite_diario:
            self.operacoes.append("Limite diário de saque excedido.")
        elif valor > self.saldo:
            self.operacoes.append("Saldo insuficiente para saque.")
        else:
            self.saldo -= valor
            self.saques_realizados += 1
            self.operacoes.append(f"Saque de R${valor:.2f}")

    def extrato(self):
        print("Extrato:")
        for operacao in self.operacoes:
            print(operacao)
        print(f"Saldo atual: R${self.saldo:.2f}")


# Criando uma instância da conta bancária
conta = ContaBancaria()

while True:
    print("Selecione uma opção:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("0. Sair")
    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 0:
        print("Encerrando o programa.")
        break
    elif opcao == 1:
        valor = float(input("Digite o valor a depositar: R$"))
        conta.depositar(valor)
    elif opcao == 2:
        valor = float(input("Digite o valor a sacar: R$"))
        conta.sacar(valor)
    elif opcao == 3:
        conta.extrato()
    else:
        print("Opção inválida. Tente novamente.")
