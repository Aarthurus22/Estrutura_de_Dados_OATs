# Classe que representa um empregado
# Guarda apenas alguns dados básicos

class Empregado:

    def __init__(self, id, primeiro_nome, ultimo_nome):
        self.id = id
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome

    # Método usado para imprimir o objeto de forma mais legível
    def __str__(self):
        return f"{self.id} - {self.primeiro_nome} {self.ultimo_nome}"


# Classe No (Node)
# Cada nó da lista encadeada guarda um empregado
# e uma referência para o próximo nó

class No:

    def __init__(self, empregado):
        self.empregado = empregado
        self.proximo = None


# Lista encadeada utilizada para tratar colisões na tabela hash
# Quando dois elementos geram o mesmo índice, eles ficam nessa lista

class ListaEncadeada:

    def __init__(self):
        self.cabeca = None  # primeiro nó da lista

    # Insere um empregado no final da lista
    def inserir(self, empregado):

        novo_no = No(empregado)

        # Se a lista estiver vazia, o novo nó vira a cabeça
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca

            # percorre a lista até o último nó
            while atual.proximo:
                atual = atual.proximo

            # adiciona o novo nó no final
            atual.proximo = novo_no

    # Busca um empregado pelo id dentro da lista
    def buscar(self, id):

        atual = self.cabeca

        # percorre a lista procurando o id
        while atual:

            if atual.empregado.id == id:
                return atual.empregado

            atual = atual.proximo

        return None

    # Imprime todos os elementos da lista
    def imprimir(self):

        atual = self.cabeca

        while atual:
            print(atual.empregado, end=" -> ")
            atual = atual.proximo

        print("None")


# Classe da Tabela Hash
# Utiliza encadeamento (chaining) para tratar colisões

class TabelaHash:

    def __init__(self, tamanho):

        # tamanho da tabela
        self.tamanho = tamanho

        # cria a tabela inicialmente vazia
        self.tabela = [None] * tamanho

    # Função hash simples
    # Calcula o índice usando o resto da divisão
    def funcao_hash(self, id):

        return id % self.tamanho

    # Insere um empregado na tabela
    def inserir(self, empregado):

        # calcula o índice onde o elemento será colocado
        indice = self.funcao_hash(empregado.id)

        # se ainda não existe lista nesse índice, cria uma
        if self.tabela[indice] is None:
            self.tabela[indice] = ListaEncadeada()

        # insere o elemento na lista encadeada
        self.tabela[indice].inserir(empregado)

    # Busca um empregado pelo id
    def buscar(self, id):

        indice = self.funcao_hash(id)

        lista = self.tabela[indice]

        # se não houver lista nesse índice, não existe elemento
        if lista is None:
            return None

        return lista.buscar(id)

    # Imprime toda a tabela hash
    def imprimir(self):

        for i in range(self.tamanho):

            print(f"Índice {i}: ", end="")

            if self.tabela[i] is None:
                print("vazio")

            else:
                self.tabela[i].imprimir()




# TESTE DO PROGRAMA

if __name__ == "__main__":

    tabela = TabelaHash(5)


    emp1 = Empregado(1123, "Arthur", "Aquino")
    emp2 = Empregado(5432, "Luan", "Lima")
    emp3 = Empregado(2221, "Jefte", "Goes")
    emp4 = Empregado(4314, "Leo", "Baraúna")
    emp5 = Empregado(1233, "Bruno", "Menezes")


    tabela.inserir(emp1)
    tabela.inserir(emp2)
    tabela.inserir(emp3)
    tabela.inserir(emp4)
    tabela.inserir(emp5)


    print("Tabela Hash:")
    tabela.imprimir()


    print("\nBusca por ID 2221:")

    resultado = tabela.buscar(2221)

    if resultado:
        print("Encontrado:", resultado)
    else:
        print("Não encontrado")