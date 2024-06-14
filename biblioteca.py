#Questão 5 e 6 e 7
from Atividades_Aula04 import Livro

livro1 = Livro("O Alquimista", "Paulo Coelho", 1988)
livro2 = Livro("Cem Anos de Solidão", "Gabriel Garcia Marquez", 1967)

livro1.emprestar()

print(f"O livro 'O Alquimista' está disponível após o empréstimo? {'Sim' if livro1.disponivel else 'Não'}")  # Saída: Não

livros_disponiveis_1949 = Livro.verificar_disponibilidade(1949)
for livro in livros_disponiveis_1949:
    print(livro)

livros_disponiveis_2006 = Livro.verificar_disponibilidade(2006)
for livro in livros_disponiveis_2006:
    print(livro)