class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def definir_nome(self, novo_nome):
        self.nome = novo_nome

    def definir_idade(self, nova_idade):
        self.idade = nova_idade

    def definir_altura(self, nova_altura):
        self.altura = nova_altura

    def obter_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura}m"

    def cumprimentar(self):
        return f"Olá, eu sou {self.nome}!"

pessoa = Pessoa("João", 30, 1.75)
print(pessoa.obter_informacoes())
print(pessoa.cumprimentar())
