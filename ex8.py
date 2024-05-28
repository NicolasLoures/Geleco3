import re

def dados(texto):
    padrao = r'(.+?) possui (\d+) anos e mora em (.+?)-(\w{2})'

    correspondencia = re.search(padrao, texto)

    nome = correspondencia.group(1)
    idade = int(correspondencia.group(2))
    cidade = correspondencia.group(3)
    estado = correspondencia.group(4)

    return (nome, idade, cidade, estado)

texto = 'Andre Smaira possui 33 anos e mora em São Carlos-SP'
print(dados(texto))  
