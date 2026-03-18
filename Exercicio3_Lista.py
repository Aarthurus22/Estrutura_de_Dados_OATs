# Classe que representa uma música

class Musica:

    def __init__(self, id, nome, artista):
        self.id = id
        self.nome = nome
        self.artista = artista
        self.proximo = None
        self.anterior = None

    def __str__(self):
        return f"{self.nome} - {self.artista}"


# Classe Playlist usando lista duplamente encadeada

class Playlist:

    def __init__(self):
        self.inicio = None
        self.fim = None

    # Adiciona música no final
    def adicionar(self, musica):

        if self.inicio is None:
            self.inicio = musica
            self.fim = musica
        else:
            self.fim.proximo = musica
            musica.anterior = self.fim
            self.fim = musica

    # Remove música do início
    def remover_inicio(self):

        if self.inicio is None:
            print("Playlist vazia")
            return

        print(f"Removendo: {self.inicio}")

        # se tiver apenas uma música
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None

    # Lista do início ao fim
    def listar(self):

        atual = self.inicio

        while atual:
            print(atual)
            atual = atual.proximo

    # Lista do fim ao início
    def listar_reverso(self):

        atual = self.fim

        while atual:
            print(atual)
            atual = atual.anterior


# Simulação do player

class Player:

    def __init__(self, playlist):
        self.atual = playlist.inicio

    def mostrar_atual(self):

        if self.atual:
            print(f"Tocando: {self.atual}")
        else:
            print("Nenhuma música")

    def proxima(self):

        if self.atual and self.atual.proximo:
            self.atual = self.atual.proximo
            self.mostrar_atual()
        else:
            print("Não há próxima música")

    def anterior(self):

        if self.atual and self.atual.anterior:
            self.atual = self.atual.anterior
            self.mostrar_atual()
        else:
            print("Não há música anterior")



# TESTE DO PROGRAMA

if __name__ == "__main__":

    playlist = Playlist()

    # músicas do Rhapsody of Fire
    m1 = Musica(1, "Land of Immortals", "Rhapsody of Fire")
    m2 = Musica(2, "Emerald Sword", "Rhapsody of Fire")
    m3 = Musica(3, "Dawn of Victory", "Rhapsody of Fire")
    m4 = Musica(4, "Holy Thunderforce", "Rhapsody of Fire")
    m5 = Musica(5, "Rain of a Thousand Flames", "Rhapsody of Fire")

    playlist.adicionar(m1)
    playlist.adicionar(m2)
    playlist.adicionar(m3)
    playlist.adicionar(m4)
    playlist.adicionar(m5)

    print("Playlist normal:")
    playlist.listar()

    print("\nPlaylist reversa:")
    playlist.listar_reverso()

    print("\nSimulação do player:")

    player = Player(playlist)

    player.mostrar_atual()

    print("\nAvançando 2 músicas:")
    player.proxima()
    player.proxima()

    print("\nVoltando 1 música:")
    player.anterior()

    print("\nRemovendo música do início:")
    playlist.remover_inicio()

    print("\nPlaylist atualizada:")
    playlist.listar()