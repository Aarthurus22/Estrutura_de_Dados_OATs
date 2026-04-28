"""
INSTITUIÇÃO: UNEX (Sistemas de Informação)
DISCIPLINA: Estrutura de Dados
ALUNO: Arthur de Aquino Costa
"""

from Tree import Tree

def main():
    tree = Tree()

    # Valores da atividade inseridos na ordem correta 
    valores = [50, 30, 70, 20, 40, 60, 80]
    
    for valor in valores:
        tree.inserir(valor)

    print("Travessia Pós-Ordem (Esquerda -> Direita -> Raiz):")
    tree.travessia_post_order()

if __name__ == "__main__":
    main()