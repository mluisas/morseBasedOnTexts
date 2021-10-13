from BinaryTree import BinaryTree
from functions import *


if __name__ == '__main__':
    text = input("""Escreva aqui um texto e a partir da frequencia de cada letra, um novo sistema de código Morse 
    será criado: """)
    clean_text = text_letters(text)
    freq = freq(clean_text)
    tree = BinaryTree(sorted(freq, key=freq.get))
    print()
    print(bfs(tree))
