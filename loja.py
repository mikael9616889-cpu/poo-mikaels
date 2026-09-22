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


def mostrar_menu():
    print("\n--- LOJINHA ---")
    print("1 - Cadastrar produto")
    print("2 - Listar catálogo")
    print("3 - Vender produto")
    print("4 - Repor produto")
    print("5 - Sair")


def listar(catalogo):
    if not catalogo:
        print("O catálogo está vazio.")
        return False

    print("\n--- CATÁLOGO ---")
    for numero, produto in enumerate(catalogo, start=1):
        print(f"{numero} - ", end="")
        produto.exibir()
    return True


def escolher_produto(catalogo):
    if not listar(catalogo):
        return None

    try:
        numero = int(input("Número do produto: "))
        return catalogo[numero - 1] if 1 <= numero <= len(catalogo) else None
    except ValueError:
        return None


def main():
    catalogo = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                nome = input("Nome do produto: ").strip()
                if not nome:
                    print("Cadastro recusado: o nome não pode ficar vazio.")
                    continue
                preco = float(input("Preço (use ponto, ex.: 4.50): "))
                estoque = int(input("Estoque inicial: "))
                catalogo.append(Produto(nome, preco, estoque))
                print("Produto cadastrado com sucesso.")
            except ValueError as erro:
                print(f"Cadastro recusado: {erro}")

        elif opcao == "2":
            listar(catalogo)

        elif opcao in ("3", "4"):
            produto = escolher_produto(catalogo)
            if produto is None:
                if catalogo:
                    print("Número de produto inválido.")
                continue
            try:
                qtd = int(input("Quantidade: "))
            except ValueError:
                print("Quantidade inválida: digite um número inteiro.")
                continue

            if opcao == "3":
                produto.vender(qtd)
            else:
                produto.repor(qtd)

        elif opcao == "5":
            print("Até logo!")
            break

        else:
            print("Opção inválida. Escolha um número de 1 a 5.")


if __name__ == "__main__":
    main()
