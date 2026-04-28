from TreeNode import TreeNode

class Tree:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = TreeNode(valor)
        else:
            self.raiz.inserir(valor)

    def travessia_in_order(self):
        if self.raiz is not None:
            self.raiz.travessia_in_order()
            print()

    # Método para iniciar o percurso pós-ordem
    def travessia_post_order(self):
        if self.raiz is not None:
            self.raiz.travessia_post_order()
            print()