class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def emitir_som(self):
        pass  

    def informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Espécie: {self.especie}")

meu_animal = Animal("Rex", 5, "Cachorro")
meu_animal.emitir_som()
meu_animal.informacoes()
