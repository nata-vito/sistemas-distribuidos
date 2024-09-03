import sys
import argparse
import xmlrpc.server

parser = argparse.ArgumentParser()
parser.add_argument('--server', action='store_true', help='suado para iniciar a aplicação como servidora')
parser.add_argument('--host', default='192.168.56.1', help='nome ou endereço do servidor')
parser.add_argument('--port', type=int, default=50000, help='porta do servidor')

args = parser.parse_args()

Address = args.host
Port = args.port

with xmlrpc.server.SimpleXMLRPCServer((Address, Port)) as server:
    server.register_introspection_functions()
    server.register_multicall_functions()

    @server.register_function
    def fn_add(a, b):
        return a + b
    
    
    @server.register_function
    def fn_sub(a, b):
        return a - b
    
    @server.register_function
    def fn_mul(a, b):
        return a * b
    
    @server.register_function
    def fn_mul(a, b):
        return a * b
    
    @server.register_function
    def fn_div(a, b):
        return a / b
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
        