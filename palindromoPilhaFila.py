from collections import deque
import re

# Exercício Pilha + Fila

def eh_palindromo(texto):
    # 1º Normalização: remove espaços, pontuação e ignora maiúsculas
    texto_normalizado = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()

    fila = deque()
    pilha = []

    # 2º Insere todos os caracteres na fila e na pilha
    for caractere in texto_normalizado:
        fila.append(caractere)   # Fila (FIFO)
        pilha.append(caractere)  # Pilha (LIFO)

    # 3º Compara os caracteres removidos da fila e da pilha
    while fila:
        if fila.popleft() != pilha.pop():
            return False

    # 4º Se todas as comparações forem iguais, é palíndromo
    return True


texto_usuario = input("Digite uma palavra ou frase: ")

if eh_palindromo(texto_usuario):
    print("É um palíndromo")
else:
    print("Não é um palíndromo.")