# módulo de interface do grupo 12, constituido por Carlos Eduardo (B39050), Daniel Kajiya (B44481), Gabriel Pastori (B43641), Leticia Helena (B43986) e Wendell Oliveira (B43619).
import re
import os
estadoForca = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
# A lista estadoForca armazena os possíveis estados do jogo, encontrada em pesquisa no google por nós.
resultadoPalavra = [] # A lista resultadoPalavra armazena as letras da palavra substituidas por '*', alteradas quando o jogador acerta
letrasTentadas = [] # A lista letrasTentadas armazena as letras que já foram chutadas (erros e acertos)
def limpa_console(): #limpa o console para a proxima etapa do jogo.
    os.system('cls' if os.name=='nt' else 'clear')

def limpa_letra(letra):  # A função limpa_letra remove os acentos da letra recebida e retorna-a
  letra = re.sub(u"[àáâã]", 'a', letra)
  letra = re.sub(u"[èéê]", 'e', letra)
  letra = re.sub(u"[ìí]", 'i', letra)
  letra = re.sub(u"[òóôõ]", 'o', letra)
  letra = re.sub(u"[ùúû]", 'u', letra)
  return letra

def codifica_palavra(palavra): # A função codifica_palavra codifica a palavra, isto é, substitui as letras por '*'
    res=[]
    for letra in palavra:
        if(letra==" "):
            res.append(" ")
        else:
            res.append("*")
    return res

def substitui_palavra(letra,resultadoPalavra,palavra): # A função substitui_palavra substitui a letra acertada na palavra.
    for i in range(0,len(palavra)):
        if(letra==limpa_letra(palavra[i])):
            resultadoPalavra[i]=palavra[i]

    return resultadoPalavra

def inicia(palavra): # A função inicia exibe o estado inicial da forca para o jogador.
    print("*****************************************************")
    print("******* Acerte a palavra ou morra tentando!!! *******")
    print("*****************************************************")
    print("Boa sorte!")
    print(estadoForca[0])
    global resultadoPalavra
    resultadoPalavra = codifica_palavra(palavra)
    print("\n")
    print(''.join(resultadoPalavra))
    print("\n\n")

def erro(numeroErros,letra): # A função erro altera as informações da interface para caso o jogador tenha errado a letra, ela deve ser chamada em um outro módulo em caso de erro.
    global letrasTentadas
    letrasTentadas.append(letra)
    limpa_console()
    print(estadoForca[numeroErros])
    print("\n")
    print("Palavra: ",''.join(resultadoPalavra))
    print("\n")
    print("Letras Tentadas: ",', '.join(letrasTentadas))
    print(55*"=")
    print("\n")

def acerto(letra,palavra,numeroErros): # A função acerto altera as informações da interface para caso o jogador tenha acertado a letra, ela deve ser chamada em um outro módulo em caso de acerto.
    global letrasTentadas
    letrasTentadas.append(letra)
    global resultadoPalavra
    resultadoPalavra=substitui_palavra(letra,resultadoPalavra,palavra)
    limpa_console()
    print(estadoForca[numeroErros])
    print("\n")
    print("Palavra: ",''.join(resultadoPalavra))
    print("\n")
    print("Letras Tentadas: ",', '.join(letrasTentadas))
    print(55*"=")
    print("\n")
    return '*' in resultadoPalavra

def letra_repetida(): # A função letra_repetida exibe uma mensagem informando que o jogador já digitou a letra antes.
    print("Você já tentou essa letra")

def nao_letra(): # A função nao_letra deve ser chamada em um outro módulo para caso a entrada não seja uma letra.
    print("Texto inserido não é uma letra ou hífen")
def venceu(palavra): # A função venceu exibe na interface a palavra da forca e um texto indicando o sucesso na forca
    limpa_console()
    print("A palavra era:", palavra)
    print('''
 \ \ / /  ___   __   ___    __ __  ___   _ _    __   ___   _  _ 
  \ V /  / _ \ / _| / -_)   \ V / / -_) | ' \  / _| / -_) | || |
   \_/   \___/ \__| \___|    \_/  \___| |_||_| \__| \___|  \_,_|
    ''')

    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def perdeu(palavra): # A função perdeu exibe na interface a palavra da forca e um texto indicando o fracasso na forca
    limpa_console()
    print("A palavra era:", palavra)
    print('''
 \ \ / /  ___   __   ___     _ __    ___   _ _   _ _   ___   _  _ 
  \ V /  / _ \ / _| / -_)   | '  \  / _ \ | '_| | '_| / -_) | || |
   \_/   \___/ \__| \___|   |_|_|_| \___/ |_|   |_|   \___|  \_,_|
    ''')
    print("     _______________         ")
    print("    /               \       ")
    print("   /                 \      ")
    print("/\/                   \/\  ")
    print("\ |   XXXX     XXXX   | /   ")
    print(" \|   XXXX     XXXX   |/     ")
    print("  |   XXX       XXX   |      ")
    print("  |                   |      ")
    print("  \__      XXX      __/     ")
    print("    |\     XXX     /|       ")
    print("    | |           | |        ")
    print("    | I I I I I I I |        ")
    print("    |  I I I I I I  |        ")
    print("    \_             _/       ")
    print("      \_         _/         ")
    print("        \_______/           ")
    



'''

A ideia, de modo geral, é que vocês chamem as funções do módulo interface através do módulo responsável pelas iterações do jogo em cada um dos possíveis casos:
- inicia(palavra): Função que vai  receber a palavra a ser advinhada e iniciar o jogo da forca no console, deve ser chamada após a palavra ser escolhida e antes do início das iterações da forca.
- erro(numeroErros, letra): Função que vai receber o número acumulado de erros do jogador e a letra digitada (errada) e exibir no console o jogo da forca com um passo mais perto da morte, além das outras informações.
- acerto(letra, palavra, numeroErros): Recebe a letra digitada (correta), a palavra a ser advinhada e o número acumulado de erros do jogador e exibe no console a forca no mesmo estado, mas as letras preenchidas na palavra codificada(Ex:"****a*").
- letra_repetida() : Função que deve ser chamada em caso do jogador já ter digitado a letra.
- nao_letra(): Função que deve ser chamada em caso do jogador ter digitado um texto que não corresponde a uma letra ("aa","1","25",etc). Uma possível ideia é verificar se não é uma letra por meio da seguinte condição: (not letra.isalpha() or len(letra) != 1) and letra != "-")
- venceu(): Função que deve ser chamada em caso do jogador ter vencido o jogo.
- perdeu(): Função que deve ser chamada em caso do jogador ter perdido o jogo (morrido).

Obs1: a lista estadoForca possui 7 estados (inicial+6), ou seja, se o jogador errar 6 vezes, ele perdeu.

Obs2: Se o usuário digitar 'a' e houver uma ocorrência de 'ã', por exemplo, e a função acerto(paramêtros) for chamada, a palavra codificada será preenchida corretamento nas posições com ou sem acento no 'a', mas o controle, por exemplo, da verificação se 'a' está em "corrupção", deve ser feito antes. É uma possibilidade verificar se a letra está na palavra com ou sem acentos, ou seja, se 'a' está em 'corrupção' ou 'a' está 'corrupçao', por exemplo.

Alguns casos para interface podem ser vistos no link: https://imgur.com/a/Ml7gw2y

'''