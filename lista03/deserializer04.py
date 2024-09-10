import CalcIMC_pb2 as CalcIMC

data = b'\n\x06Marcos\x11\x00\x00\x00\x00\x00\xe0Z@\x19{\x14\xaeG\xe1z\xfc?'
request = CalcIMC.CalculoIMCRequest()
request.ParseFromString(data)
print(f" Nome: {request.nome}")
print(f" Peso: {request.peso}")
print(f" Altura: {request.altura}")

def response():
    response = CalcIMC.CalculoIMCResponse()
    assert not response.HasField("imc")
    response.imc = request.peso/request.altura
    return 