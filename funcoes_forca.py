import random

def escolha_palavra() -> list:
    #lista de palavras
    tema = int(input("Qual tema você deseja?(1.Animais, 2.Frutas, 3.Paises, 4.Pokemon, 5.Steven Universe ou 6.Geral)"))
    #selecionando uma palavra aleatoria da lista que el selecionou
    if tema == 1:
        lista = open("palavras_animais.txt","r")
        lista_total = lista.readlines()
        palavra = random.choice(lista_total)
        palavra = palavra.strip()
    if tema == 2:
        lista = open("palavras_frutas.txt","r")
        lista_total = lista.readlines()
        palavra = random.choice(lista_total)
        palavra = palavra.strip()
    if tema == 3:
        lista = open("palavras_paises.txt","r")
        lista_total = lista.readlines()
        palavra = random.choice(lista_total)
        palavra = palavra.strip()
    if tema == 4:
        lista = open("palavras_pk.txt","r")
        lista_total = lista.readlines()
        palavra = random.choice(lista_total)
        palavra = palavra.strip()
    if tema == 5:
        lista = open("palavras_su.txt","r")
        lista_total = lista.readlines()
        palavra = random.choice(lista_total)
        palavra = palavra.strip()
    if tema == 6:
        lista = open("palavras.txt","r")
        lista_total = lista.readlines()
        palavra = random.choice(lista_total)
        palavra = palavra.strip()
    return palavra

def mascara(palavra:str) -> list:
    qnt = len(palavra)
    letras = []
    for x in range(qnt):
        letras.append("_")
    return letras

def verificacao_mascara(palavra:str, chute:str, letras:str):
        y=0
        passar = 0
        #verificando onde esta a letra na palavra
        for x in palavra:
            if chute == x:
                #mudando a letra na lista
                letras[y] = chute
                #verificando se tem outra em outro lugar
                if passar == 5:
                    break
                passar+=1
            y+=1
        return letras

def verificacao_vitoria(letras:str) -> bool:
    if "_" not in letras:
        print()
        print("você ganhou")
        return True
    return False