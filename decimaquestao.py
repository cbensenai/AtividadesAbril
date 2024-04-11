class Pedido:
    def __init__(self):
        self.itens = {}
        self.total = 0
        self.status = "Em andamento"

    def adicionar_item(self, item, quantidade, preco_unitario):
        if item in self.itens:
            self.itens[item]["quantidade"] += quantidade
        else:
            self.itens[item] = {"quantidade": quantidade, "preco_unitario": preco_unitario}

        self.total += quantidade * preco_unitario

    def calcular_total(self):
        return self.total

    def alterar_status(self, novo_status):
        self.status = novo_status

    def mostrar_itens(self):
        for item, info in self.itens.items():
            print(f"Item: {item}, Quantidade: {info['quantidade']}, Preço unitário: R${info['preco_unitario']}")

pedido = Pedido()
pedido.adicionar_item("Pizza", 2, 30)
pedido.adicionar_item("Refrigerante", 1, 5)
pedido.mostrar_itens()
print(f"Total do pedido: R${pedido.calcular_total()}")
pedido.alterar_status("Concluído")
print(f"Status do pedido: {pedido.status}")
