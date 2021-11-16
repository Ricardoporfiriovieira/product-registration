# import os
produtos = []
n = 0
substituto = 0
posi = 0
cont = "SIM"
cont4 = "SIM"
deln = 0
delall = False
op = 0
# limpa = lambda:  os.system('clear')

while op != 5:
    # limpa()
    print(
        """
   -=-=-=-=-= SOFTWARE DE CADASTRO DE PRODUTOS -=-=-=-=-=--=--=-=-
   [ 1 ] - Cadastrar produto
   [ 2 ] - Alterar Produto
   [ 3 ] - Listar  e Contar Produto
   [ 4 ] - Deletar Produto
   [ 5 ] - Sair do Programa
   """
    )
    op = int(input("""Informe a opção desejada: """))
    print("")
    if op == 1:
        resp = "SIM"
        while resp == "SIM":
            quant = int(input("Quantos produtos você quer cadastrar? "))
            if quant >= 1:
                delall = False
                for c in range(1, quant + 1):
                    produtos.append(input(f"Digite o {c}º Produto "))
                if produtos[len(produtos) - 1] != "":
                    resp = (
                        input("Deseja cadastrar mais produtos? [sim / não] ")
                        .upper()
                        .strip()
                    )
                else:
                    del produtos[len(produtos) - 1]
                    print("opção inválida, tente novamente!")
                    resp = "SIM"
            else:
                resp = "não"

        # limpa()
        print("")

    elif op == 2 and delall != True:
        cont = "SIM"
        for c in range(1, len(produtos) + 1):
            print(f"{c}º - ", produtos[c - 1])

        while cont == "SIM":
            n = int(input("Quantos produtos você deseja Alterar? "))
            if len(produtos) - n >= 0:
                for c in range(1, n + 1):
                    posi = int(
                        input("Digite a posição do produto que você deseja alterar: ")
                    )
                    if posi > len(produtos) - 1:
                        while posi > len(produtos) - 1:
                            posi = int(input("Opção inválida tente novamente: "))
                    produtos[posi - 1] = input("Digite o novo produto: ")
                cont = input("Deseja continuar? [sim / não] ").upper().strip()
            else:
                print("Opção inválida tente novamente!")
                cont = "SIM"
        # limpa()
        print("")

    elif op == 3:
        print("Todos os produtos cadastrados na lista: ")
        for c in range(1, len(produtos) + 1):
            print(f"{c}º - {produtos[c - 1]}")
        print(f"Atualmente a lista contém {len(produtos)} produtos")

    elif op == 4:
        # limpa()
        cont4 = "SIM"
        while cont4 == "SIM":
            vrau = len(produtos)
            print("Todos os produtos cadastrados na lista: ")
            for c in range(1, len(produtos) + 1):
                print(f"{c}º - {produtos[c - 1]}")
            deln = int(input("Quantos Produtos você quer deletar? "))
            if vrau - deln <= 1:
                delall = True
            if len(produtos) - deln >= 0:
                for c in range(1, deln + 1):

                    print("Todos os produtos cadastrados na lista: ")
                    for c in range(1, len(produtos) + 1):
                        print(f"{c}º - {produtos[c - 1]}")

                    pog = int(
                        input("Qual a posição do produto que você deseja deletar? ")
                    )
                    del produtos[pog - 1]

                if delall == True:
                    print("Todos os produtos da lista foram deletados!")
                    produtos = []
                    cont4 = "nao"
                else:
                    cont4 = input("Deseja continuar? [sim / não]: ").upper().strip()
            else:
                print(
                    "Não é possível deletar essa quantidade de ítens, tente novamente!"
                )
                cont4 = "SIM"
        # limpa()
        print("")
    elif op < 0 or op > 5:
        print("Opção inválida!")

print("acabou!")
