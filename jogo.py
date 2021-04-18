import interface
import leitura
import re


def limpa_letra(letra):  # A função limpa_letra remove os acentos da letra recebida e retorna-a
  letra = re.sub(u"[àáâã]", 'a', letra)
  letra = re.sub(u"[èéê]", 'e', letra)
  letra = re.sub(u"[ìí]", 'i', letra)
  letra = re.sub(u"[òóôõ]", 'o', letra)
  letra = re.sub(u"[ùúû]", 'u', letra)
  #letra = re.sub(u"[ç]",'c',letra)
  return letra  


def limpa_palavra(texto):  # Limpa os acentos da palavra
	texto = list(texto)
	novoTexto = ""
	for letra in texto:
		novoTexto += limpa_letra(letra)
	return novoTexto


def verifica_tentativa(letra, palavra):  # Retorna se a letra está na palavra ou não (sendo a palavra com ou sem acentos)
	return (letra in palavra or letra in limpa_palavra(palavra))


def jogo():  # Função que define as iterações do jogo (tentativas)

	palavra = leitura.escolhe_palavra()  
	maximoErros = 6  # Define um valor máximo de erros (6)
	numeroErros = 0
	perdeu = True  # Variavel que armazena se o usuario perdeu ou não, é inicializada como True
	acertos = []
	erros = []
	interface.inicia(palavra)
	while (numeroErros < maximoErros and perdeu == True):  # Enquanto o número máximo de erros não for excedido e o jogador não tiver ganho
		letra = input("Advinhe uma letra: ")
		letra = letra.lower()
		if ((not letra.isalpha() or len(letra) != 1) and letra != "-"):  # Se não for uma letra ou se o tamanho não for 1 e se a letra não for um hífen
			interface.nao_letra()  # Não é uma letra
			continue  # Próxima iteração
		if (limpa_letra(letra) in erros or limpa_letra(letra)
		    in acertos or letra in erros or letra in acertos):  # Se o jogador já tiver digitado a letra
			interface.letra_repetida()  # Letra é repetida
			continue  # Próxima iteração

		if (verifica_tentativa(letra, palavra)):  # Se o jogador acertou
			perdeu = interface.acerto(letra, palavra, numeroErros)  # Altero a variável perdeu para caso todas as letras já tiverem sido encontradas
			acertos.append(letra)  # Adiciono o acerto na lista de acertos

		else:  # Se o jogador errou
			numeroErros += 1
			interface.erro(numeroErros, letra)
			erros.append(letra)  # Adiciono o erro na lista de erros
	if (perdeu == False):  #Se ao final, o jogador tiver preenchido todas as letras
		interface.venceu(palavra)
	else:  # Se ao final, o jogador não venceu
		interface.perdeu(palavra)
