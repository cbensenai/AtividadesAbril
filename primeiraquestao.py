class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("O carro foi ligado.")
        else:
            print("O carro já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print("O carro foi desligado.")
        else:
            print("O carro já está desligado.")

    def acelerar(self, velocidade):
        if self.ligado:
            self.velocidade += velocidade
            print(f"O carro acelerou para {self.velocidade} km/h.")
        else:
            print("É necessário ligar o carro antes de acelerar.")

meu_carro = Carro("Toyota", "Corolla", 2022, "Prata")
meu_carro.ligar()
meu_carro.acelerar(40)
meu_carro.desligar()
