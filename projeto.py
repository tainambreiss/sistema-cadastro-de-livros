class Livro:
    def __init__(self,titulo, autor, ID):
        self.titulo = titulo
        self.__autor = autor
        self.__id = id
    self.__status_emprestimo = "disponivel"


class Membro:
    def __init__(self, nome, numero_membro):
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico_emprestimos = []

class Biblioteca:
    def __init__(self):
        self.catalogo_livros = []
        self.registro_membros = []

    def adicionar_livro(self, livro):
        self.catalogo_livros.append(livro)

    def adicionar_membro(self, membro):
        self.registro_membros.append(membro)

    def emprestar_livro(self, livro, membro):
        if livro.status_emprestimo == "Disponível":
            livro.status_emprestimo = "Emprestado"
            membro.historico_emprestimos.append(livro)
            print(f"{livro.titulo} foi emprestado para {membro.nome}.")
        else:
            print(f"{livro.titulo} não está disponível para empréstimo.")

    def devolver_livro(self, livro, membro):
        if livro in membro.historico_emprestimos:
            livro.status_emprestimo = "Disponível"
            membro.historico_emprestimos.remove(livro)
            print(f"{livro.titulo} foi devolvido por {membro.nome}.")
        else:
            print(f"{livro.titulo} não foi emprestado por {membro.nome}.")

    def pesquisar_livros(self, criterio, termo):
        resultados = []
        for livro in self.catalogo_livros:
            if criterio.lower() == 'titulo' and termo.lower() in livro.titulo.lower():
                resultados.append(livro)
            elif criterio.lower() == 'autor' and termo.lower() in livro.autor.lower():
                resultados.append(livro)
            elif criterio.lower() == 'id' and str(termo) == str(livro.livro_id):
                resultados.append(livro)
        return resultados


# Exemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Adicionando livros e membros à biblioteca
    livro1 = Livro("Python Programming", "John Doe", 1)
    livro2 = Livro("Data Science 101", "Jane Smith", 2)
    membro1 = Membro("Alice", 101)
    membro2 = Membro("Bob", 102)

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_membro(membro1)
    biblioteca.adicionar_membro(membro2)

    # Realizando operações de empréstimo e devolução
    biblioteca.emprestar_livro(livro1, membro1)
    biblioteca.emprestar_livro(livro2, membro2)
    biblioteca.devolver_livro(livro1, membro1)

    # Pesquisando livros por título, autor ou ID
    resultados_pesquisa = biblioteca.pesquisar_livros('titulo', 'python')
    for resultado in resultados_pesquisa:
        print(f"Resultado da pesquisa: {resultado.titulo} por {resultado.autor}")