class Estudante:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

notas_aluno = [8, 7, 6, 9]
aluno = Estudante("Maria", 20, notas_aluno)
print(f"Média do aluno: {aluno.calcular_media()}")
print(f"Situação do aluno: {aluno.verificar_aprovacao()}")
