usuarios = {}

emails = ["xpto@xyz.com", "xkcd@phd.com"]

tupla = list(enumerate(emails))

print(tupla)

for chave in range(0,len(tupla)):
    print(f"Email: {tupla[chave][1]}")
    usuarios[tupla[chave]] = [input("Digite o nome: "), input("Digite o nível: ")]
    
for chave, dado in usuarios.items():
    print(f"Usuário: {chave[0]}")
    print(f"Email: {chave[1]}")
    print(f"Nome: {dado[0]}")
    print(f"Nível: {dado[1]}")