class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def atualizar_estoque(self, quantidade):
        self.estoque += quantidade

    def calcular_preco_total(self, quantidade):
        return self.preco * quantidade

meu_produto = Produto("Camiseta", 50, 100)
meu_produto.atualizar_estoque(-10)
print(f"Preço total: R${meu_produto.calcular_preco_total(5)}")
