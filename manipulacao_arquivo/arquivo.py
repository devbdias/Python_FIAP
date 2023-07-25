caminho = r'Python FIAP\manipulacao_arquivo'

with open(fr"{caminho}\arquivo1.txt", "a") as arquivo:
    arquivo.write("teste!2\n")

with open(fr"{caminho}\arquivo1.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)