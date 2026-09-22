"""Lojinha: cadastro, venda e reposição de produtos."""


class Produto:
    def __init__(self, nome, preco, estoque=0):
        self.nome = nome
        self.__preco = 0
        self.__estoque = 0
        # Usar as properties aqui garante que o objeto já nasça validado.
        self.preco = preco
        self.estoque = estoque

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")
        self.__preco = float(valor)

    @property
    def estoque(self):
        return self.__estoque

    @estoque.setter
    def estoque(self, valor):
        if valor < 0:
            raise ValueError("O estoque não pode ser negativo.")
        self.__estoque = int(valor)

    def exibir(self):
        print(f"{self.nome} | R$ {self.preco:.2f} | estoque: {self.estoque}")

    def repor(self, qtd):
        if qtd <= 0:
            print("Reposição recusada: a quantidade deve ser positiva.")
            return False

        self.estoque += qtd
        print(f"Reposição realizada: {qtd} unidade(s) adicionada(s).")
        return True

    def vender(self, qtd):
        if qtd <= 0:
            print("Venda recusada: a quantidade deve ser positiva.")
            return False
        if qtd > self.estoque:
            print("Venda recusada: estoque insuficiente.")
            return False

        self.estoque -= qtd
        print(f"Venda realizada: {qtd} unidade(s).")
        return True
