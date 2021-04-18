import random 
def le_arquivo(nomeArquivo):
    with open(nomeArquivo) as f: 
        palavras = f.readlines() # Lê o arquivo linha por linha e salva cada palavra em uma lista
    palavras = [x.strip().lower() for x in palavras] # Remove o \n do final de cada palavra e deixa as letras minúsculas
    return palavras

def escolhe_palavra(nomeArquivo="palavras.txt"):
    palavras = le_arquivo(nomeArquivo)
    return random.choice(palavras) # Retorna uma palavra aleatória

#escolhe a palavra do grupo frutas
def escolhe_comida(nomeArquivo="Frutas e Legumes.txt"):
    palavras = le_arquivo(nomeArquivo)
    return random.choice(palavras) # Retorna uma palavra aleatória