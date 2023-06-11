import re

def chars_valido(value):
    nome_sem_espaco = value.replace(" ", '')
    return nome_sem_espaco.isalpha()

def telefone_valido(telefone):
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(model, telefone)
    return resposta
