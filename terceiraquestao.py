class ContaBancaria:
    def __init__(self, numero_conta, saldo, titular):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.titular = titular

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}")
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")

minha_conta = ContaBancaria("12345-6", 1000, "João")
minha_conta.depositar(500)
minha_conta.sacar(200)
minha_conta.mostrar_saldo()
