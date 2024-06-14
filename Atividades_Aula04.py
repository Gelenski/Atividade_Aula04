#Questão 1
# class Livro:
#     def __init__(self, titulo, autor, ano_publicacao):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
#         self.disponivel = True

#Questão 2

# class Livro:
#     def __init__(self, titulo, autor, ano_publicacao):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
#         self.disponivel = True

#     def __str__(self):
#         return f"'{self.titulo}' por {self.autor}, publicado em {self.ano_publicacao}"

# livro1 = Livro("Lua Nova", "Stephenie Meyer", 2006)
# livro2 = Livro("O Pequeno Príncipe", " Saint-Exupéry", 1943)

# print(livro1)
# print(livro2)

# #Questão 3

# class Livro:
#     def __init__(self, titulo, autor, ano_publicacao):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
#         self.disponivel = True

#     def __str__(self):
#         return f"'{self.titulo}' por {self.autor}, publicado em {self.ano_publicacao}"

#     def emprestar(self):
#         self.disponivel = False

# livro = Livro("Lua Nova", "Stephenie Meyer", 2006)

# livro.emprestar()

# print(f"O livro está disponível? {'Sim' if livro.disponivel else 'Não'}")

#Questão 4

class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}, publicado em {self.ano_publicacao}"

    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        return [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]

livro1 = Livro("Lua Nova", "Stephenie Meyer", 2006)
livro2 = Livro("O Pequeno Príncipe", " Saint-Exupéry", 1949)
livro3 = Livro("1984", "George Orwell", 1949)
livro4 = Livro("Cem Anos de Solidão", "Gabriel Garcia Marquez", 1967)

livro1.emprestar()

livros_disponiveis_1949 = Livro.verificar_disponibilidade(1949)
for livro in livros_disponiveis_1949:
    print(livro)

livros_disponiveis_2006 = Livro.verificar_disponibilidade(2006)
for livro in livros_disponiveis_2006:
    print(livro)
