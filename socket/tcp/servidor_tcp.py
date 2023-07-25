import socket

def criar_servidor_tcp(host, porta):
    # Cria um objeto socket usando a família de endereços e o tipo de socket
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Associa o servidor ao endereço e à porta especificados
        servidor.bind((host, porta))

        # Configura o servidor para ouvir por conexões
        servidor.listen(2)
        print(f"Servidor TCP aguardando conexões em {host}:{porta}...")

        while True:
            # Aguarda a chegada de uma conexão
            conexao, endereco_cliente = servidor.accept()
            print(f"Conexão estabelecida com {endereco_cliente}")

            # Envia uma mensagem de boas-vindas para o cliente
            mensagem_boas_vindas = "Bem-vindo ao servidor TCP!"
            conexao.sendall(mensagem_boas_vindas.encode())

            # Fecha a conexão com o cliente
            conexao.close()
            print(f"Conexão com {endereco_cliente} encerrada.")

    except KeyboardInterrupt:
        print("Servidor interrompido pelo usuário.")

    finally:
        # Fecha o socket do servidor quando o loop termina
        servidor.close()

if __name__ == "__main__":
    HOST = "127.0.0.1"  # Endereço local
    PORTA = 12345       # Porta para conexões
    criar_servidor_tcp(HOST, PORTA)