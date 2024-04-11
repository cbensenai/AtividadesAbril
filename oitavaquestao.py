class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        return self.altura * self.largura

    def calcular_perimetro(self):
        return 2 * (self.altura + self.largura)

meu_retangulo = Retangulo(5, 10)
print(f"Área do retângulo: {meu_retangulo.calcular_area()}")
print(f"Perímetro do retângulo: {meu_retangulo.calcular_perimetro()}")
