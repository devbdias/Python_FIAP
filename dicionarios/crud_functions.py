import os
import platform

def perguntar():
    return input("O que deseja realizar?\n"+
              "<I> Para Inserir um usuário \n"+
              "<P> Para Pesquisar um usuário \n"+
              "<E> Para Excluir um usuário \n"+
              "<L> Para Listar um usuário \n"+
              "<A> Para Atualizar um usuário \n"+
              "Opção selecionada: "
              ).upper()

def salvar(dicionario):
    with open(r"Python FIAP\dicionarios\db\db.txt") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(f"{chave}:{valor}")
    
def inserir(dicionario):
    login = input("Digite o login: ").upper()
    nome = input("Digite o nome: ").upper()
    data = input("Digite a data: ").upper()
    estacao_acessada = input("Qual a última estação acessada: ").upper()

    # Adiciona os dados do usuário ao dicionário 'dicionario'
    dicionario[login] = {
        'nome': nome,
        'data': data,
        'última estação acessada': estacao_acessada
    }
    salvar(dicionario)

def listar(dicionario):
    lista = []
    for login, dados in dicionario.items():
        lista.append((login, dados['nome']))
    if not lista:
        print('Não há dados para listar.')
    else:
        for login, nome in lista:
            print(f"Login: {login}, Nome: {nome}")

def pesquisar(dicionario):
    login_pesquisa = input("Digite o login do usuário que deseja pesquisar: ").upper()
    if login_pesquisa in dicionario:
        dados = dicionario[login_pesquisa]
        print(f"Login: {login_pesquisa}, Nome: {dados['nome']}, Data: {dados['data']}, Estação: {dados['última estação acessada']}")
    else:
        print("Usuário não encontrado.")

def excluir(dicionario):
    login_excluir = input("Digite o login do usuário que deseja excluir: ").upper()
    if login_excluir in dicionario:
        del dicionario[login_excluir]
        print(f"Usuário com login '{login_excluir}' excluído com sucesso.")
    else:
        print("Usuário não encontrado.")
        
def atualizar(dicionario):
    login_atualizar = input("Digite o login do usuário que deseja atualizar: ").upper()
    if login_atualizar in dicionario:
        print(f"Dados atuais do usuário {login_atualizar}:")
        print(f"Nome: {dicionario[login_atualizar]['nome']}")
        print(f"Data: {dicionario[login_atualizar]['data']}")
        print(f"Estação: {dicionario[login_atualizar]['última estação acessada']}")

        nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ").upper()
        data = input("Digite a nova data (ou pressione Enter para manter a atual): ").upper()
        estacao_acessada = input("Digite a nova última estação acessada (ou pressione Enter para manter a atual): ").upper()

        # Atualiza os campos do usuário se o usuário digitar algo, caso contrário, mantém os valores atuais
        if nome:
            dicionario[login_atualizar]['nome'] = nome
        if data:
            dicionario[login_atualizar]['data'] = data
        if estacao_acessada:
            dicionario[login_atualizar]['última estação acessada'] = estacao_acessada
            
        salvar(dicionario)
        
        print("Usuário atualizado com sucesso.")
    else:
        print("Usuário não encontrado.")

def salvar(dicionario):
    with open(r"Python FIAP\dicionarios\db\db.txt", "+a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(f"{chave}:{valor}")
            
def limpar_console():
    sistema_operacional = platform.system()

    if sistema_operacional == "Windows":
        os.system("cls")
    else:
        os.system("clear")