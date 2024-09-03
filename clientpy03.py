import xmlrpc.client

with xmlrpc.client.ServerProxy('http://192.168.56.1:50000/') as proxy:
    print(proxy.fn_div(4, 5))