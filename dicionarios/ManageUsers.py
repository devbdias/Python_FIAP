from crud_functions import *

usuarios = {}
opcoes = ["A", "I", "P", "E", "L"]

opcao = perguntar()

while opcao in opcoes:
    if opcao == "I":
        limpar_console()
        inserir(usuarios)
    elif opcao == "L":
        limpar_console()
        listar(usuarios)
    elif opcao == "P":
        limpar_console()
        pesquisar(usuarios)
    elif opcao == "E":
        limpar_console()
        excluir(usuarios)
    elif opcao == "A":
        limpar_console()
        atualizar(usuarios)
    else:
        limpar_console()
        print("Aplicação encerrada!")
        
    opcao = perguntar()
