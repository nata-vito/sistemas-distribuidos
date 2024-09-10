import socket
import argparse

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Servidor rodando em {host}:{port}...")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Conexão estabelecida com {client_address}")
                data = client_socket.recv(1024)
                if not data:
                    break
                response = data.decode('utf-8').upper()
                client_socket.sendall(response.encode('utf-8'))
                print(f"Mensagem recebida e enviada de volta: {response}")

def start_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        message = input("Digite uma mensagem para enviar ao servidor: ")
        client_socket.sendall(message.encode('utf-8'))
        data = client_socket.recv(1024)
        print(f"Resposta do servidor: {data.decode('utf-8')}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Aplicação cliente-servidor TCP')
    parser.add_argument('mode', choices=['server', 'client'], help='Modo de operação: server ou client')
    parser.add_argument('host', type=str, help='IP ou hostname do servidor')
    parser.add_argument('port', type=int, help='Porta do servidor')

    args = parser.parse_args()

    if args.mode == 'server':
        start_server(args.host, args.port)
    elif args.mode == 'client':
        start_client(args.host, args.port)
