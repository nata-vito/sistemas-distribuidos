import socket
import argparse
import os

# Função para iniciar o servidor
def start_server(host, port, directory):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Servidor rodando em {host}:{port}...")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Conexão estabelecida com {client_address}")
                request = client_socket.recv(1024).decode('utf-8')
                print(f"Requisição recebida: {request}")
                handle_request(client_socket, request, directory)

# Função para tratar a requisição do cliente
def handle_request(client_socket, request, directory):
    lines = request.splitlines()
    if len(lines) > 0 and lines[0].startswith("GET"):
        path = lines[0].split(' ')[1].strip()
        if path == "/":
            # Envia a lista de arquivos disponíveis no diretório
            files = os.listdir(directory)
            response = "200 OK\n\n" + "\n".join(files)
            client_socket.sendall(response.encode('utf-8'))
        else:
            # Tenta enviar o arquivo solicitado
            filepath = os.path.join(directory, path.lstrip('/'))
            if os.path.exists(filepath):
                file_size = os.path.getsize(filepath)
                with open(filepath, 'rb') as f:
                    file_content = f.read()
                    response = f"200 OK\nLength: {file_size}\n\n"
                    client_socket.sendall(response.encode('utf-8') + file_content)
            else:
                # Arquivo não encontrado
                response = "404 Nao encontrado\n\n"
                client_socket.sendall(response.encode('utf-8'))

# Função para iniciar o cliente
def start_client(host, port, directory, file_name=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        if file_name:
            # Solicita o arquivo específico
            request = f"GET /{file_name}\n\n"
        else:
            # Solicita a lista de arquivos
            request = "GET /\n\n"

        client_socket.sendall(request.encode('utf-8'))

        # Recebe a resposta
        response = client_socket.recv(4096).decode('utf-8')
        if response.startswith("200 OK"):
            print("Resposta do servidor:")
            if "Length" in response:
                # Recebe o conteúdo do arquivo
                header, content = response.split('\n\n', 1)
                save_path = os.path.join(directory, file_name)
                with open(save_path, 'wb') as f:
                    f.write(content.encode('utf-8'))
                print(f"Arquivo '{file_name}' salvo em {directory}")
            else:
                # Exibe a lista de arquivos
                print(response.split('\n\n', 1)[1])
        else:
            print(response)

# Ponto de entrada principal
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Aplicação cliente-servidor TCP com transferência de arquivos')
    parser.add_argument('mode', choices=['server', 'client'], help='Modo de operação: server ou client')
    parser.add_argument('host', type=str, help='IP ou hostname do servidor')
    parser.add_argument('port', type=int, help='Porta do servidor')
    parser.add_argument('directory', type=str, help='Diretório de arquivos')
    parser.add_argument('--file', type=str, help='Arquivo a ser transferido (apenas no modo client)', default=None)

    args = parser.parse_args()

    if args.mode == 'server':
        start_server(args.host, args.port, args.directory)
    elif args.mode == 'client':
        start_client(args.host, args.port, args.directory, args.file)
