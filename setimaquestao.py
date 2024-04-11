class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def informacoes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Número de páginas: {self.num_paginas}"

    def calcular_palavras_por_pagina(self, num_palavras):
        return num_palavras / self.num_paginas

meu_livro = Livro("Dom Casmurro", "Machado de Assis", 256)
print(meu_livro.informacoes())
print(f"Palavras por página: {meu_livro.calcular_palavras_por_pagina(50000)}")
