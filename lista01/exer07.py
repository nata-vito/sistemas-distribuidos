import xmlrpc.client
import argparse
from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import threading

# Funções do servidor
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro: Divisão por zero"
    return x / y

# Função do servidor para iniciar o servidor
def start_server(host, port):
    with SimpleXMLRPCServer((host, port), requestHandler=SimpleXMLRPCRequestHandler) as server:
        server.register_introspection_functions()
        server.register_function(add, 'add')
        server.register_function(subtract, 'subtract')
        server.register_function(multiply, 'multiply')
        server.register_function(divide, 'divide')
        print(f"Servidor rodando em {host}:{port}...")
        server.serve_forever()

# Função do cliente para realizar chamadas RPC
def run_client(host, port):
    with xmlrpc.client.ServerProxy(f"http://{host}:{port}/") as proxy:
        # Realizando chamada multicall: (2+3), (5*5), (7-2), (40/8)
        multicall = xmlrpc.client.MultiCall(proxy)
        multicall.add(2, 3)
        multicall.multiply(5, 5)
        multicall.subtract(7, 2)
        multicall.divide(40, 8)

        multicall_results = multicall()
        print("Resultados Multicall:")
        for result in multicall_results:
            print(result)

        # Realizando chamadas simples: a=(2+3), b=a*2, c=b-5, d=a/c
        a = proxy.add(2, 3)
        b = proxy.multiply(a, 2)
        c = proxy.subtract(b, 5)
        if c != 0:
            d = proxy.divide(a, c)
        else:
            d = "Erro: Divisão por zero"

        print("\nResultados Simples:")
        print(f"a = {a}")
        print(f"b = {b}")
        print(f"c = {c}")
        print(f"d = {d}")

# Função para rodar o servidor em uma thread separada para facilitar testes locais
def start_server_thread(host, port):
    server_thread = threading.Thread(target=start_server, args=(host, port))
    server_thread.daemon = True
    server_thread.start()
    return server_thread

# Ponto de entrada principal
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Aplicação XML-RPC para operações matemáticas básicas')
    parser.add_argument('mode', choices=['server', 'client'], help='Modo de operação: server ou client')
    parser.add_argument('host', type=str, help='Endereço do servidor (localhost recomendado)')
    parser.add_argument('port', type=int, help='Porta do servidor (ex: 50000)')
    
    args = parser.parse_args()

    if args.mode == 'server':
        start_server(args.host, args.port)
    elif args.mode == 'client':
        run_client(args.host, args.port)
