import socket

def cliente_tcp(host, porta):
    try:
        # Cria um objeto socket usando a família de endereços e o tipo de socket
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conecta ao servidor
        cliente.connect((host, porta))

        # Recebe a mensagem de boas-vindas do servidor
        mensagem_boas_vindas = cliente.recv(1024).decode()
        print(f"Mensagem do servidor: {mensagem_boas_vindas}")

    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor. Verifique se o servidor está em execução.")
    except KeyboardInterrupt:
        print("Cliente interrompido pelo usuário.")

    finally:
        # Fecha o socket do cliente
        cliente.close()

if __name__ == "__main__":
    HOST = "127.0.0.1"  # Endereço do servidor
    PORTA = 12345       # Porta do servidor
    cliente_tcp(HOST, PORTA)