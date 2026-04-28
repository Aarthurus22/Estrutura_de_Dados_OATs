class TreeNode:
    def __init__(self, dado):
        self.dado = dado
        self.filho_esquerdo = None
        self.filho_direito = None

    def inserir(self, valor):
        if valor == self.dado:
            return

        if valor < self.dado:
            if self.filho_esquerdo is None:
                self.filho_esquerdo = TreeNode(valor)
            else:
                self.filho_esquerdo.inserir(valor)
        else:
            if self.filho_direito is None:
                self.filho_direito = TreeNode(valor)
            else:
                self.filho_direito.inserir(valor)

    def travessia_in_order(self):
        if self.filho_esquerdo is not None:
            self.filho_esquerdo.travessia_in_order()

        print(f"{self.dado}, ", end="")

        if self.filho_direito is not None:
            self.filho_direito.travessia_in_order()

    # Novo método para Percurso Pós-Ordem (Esquerda -> Direita -> Raiz)
    def travessia_post_order(self):
        if self.filho_esquerdo is not None:
            self.filho_esquerdo.travessia_post_order()

        if self.filho_direito is not None:
            self.filho_direito.travessia_post_order()
            
        print(f"{self.dado}, ", end="")

    def get_dado(self):
        return self.dado

    def set_dado(self, dado):
        self.dado = dado

    def get_filho_esquerdo(self):
        return self.filho_esquerdo

    def set_filho_esquerdo(self, filho_esquerdo):
        self.filho_esquerdo = filho_esquerdo

    def get_filho_direito(self):
        return self.filho_direito

    def set_filho_direito(self, filho_direito):
        self.filho_direito = filho_direito