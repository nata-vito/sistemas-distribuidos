import xmlrpc.client

# Definindo o host e a porta do servidor
host = "localhost"
port = 50000  # Substitua pela porta do seu servidor

# Criando o proxy para se comunicar com o servidor
proxy = xmlrpc.client.ServerProxy(f"http://{host}:{port}/")

# Executando as funções e imprimindo os resultados
print("Resultado da soma (add):", proxy.add(10, 5))          # Exemplo: 10 + 5
print("Resultado da subtração (subtract):", proxy.subtract(10, 5))  # Exemplo: 10 - 5
print("Resultado da multiplicação (multiply):", proxy.multiply(10, 5))  # Exemplo: 10 * 5
print("Resultado da divisão (divide):", proxy.divide(10, 5))      # Exemplo: 10 / 5
