import sys
import argparse
import xmlrpc.client
import xmlrpc.server

parser = argparse.ArgumentParser()
parser.add_argument('--server', action='store_true', help='suado para iniciar a aplicação como servidora')
parser.add_argument('--host', default='localhost', help='nome ou endereço do servidor')
parser.add_argument('--port', type=int, default=50000, help='porta do servidor')

args = parser.parse_args()

Address = args.host
Port = args.port

if args.server:
    with xmlrpc.server.DocXMLRPCServer((Address, Port)) as server:
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
else:
    with xmlrpc.client.ServerProxy('http://localhost:50000/', verbose=True) as proxy:
        print(proxy.fn_add(4, 5))
        """ 
        print(proxy.fn_sub(4, 5))
        print(proxy.fn_mul(4, 5))
        print(proxy.fn_div(4, 5)) """