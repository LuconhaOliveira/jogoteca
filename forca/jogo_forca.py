from forca.funcoes_forca import *
def jogo_forca():
    #lista para ficar os underlines e as letras colocadas
    letras = []
    #quantidade de erros possiveis
    vida = ["", "\ ", "\O", "\O/", """\O/
    \ """, """\O/
    \ 
    /""", """\O/
    \ 
    / \ """]
    cont_vida = 0
    #variavel para conseguir entrar a mesma letra mais de um vez, caso ela se repita na palavra
    passar = 0
    #guardar letras que ja foram
    letras_usadas = []
    #selecionando uma palavra aleatoria da lista que el selecionou
    palavra = escolha_palavra()
    #adicionando a qntd de letras na lista
    letras = mascara(palavra)
    #mostrando letras e vidas
    print(*letras)
    print("você tem 6 tentativas")
    while True:
        #chutando um letra
        chute = input("coloque a letra: ").upper()
        letras_usadas.append(chute)
        if chute == palavra:
            print()
            print("você ganhou")
            break
        if len(chute) >=2:
            cont_vida+=1
        #verificando se existe essa letra na palavra
        if chute in palavra:
            verificacao_mascara(palavra,chute,letras)
        #diminuindo a vida caso erre
        else:
            cont_vida +=1
        #mostrando como esta a palavra e as vidas
        print(*letras)
        print(*vida[cont_vida])
        print(f"ja foram as letras {letras_usadas}")
        print()
        #verificando se ele ganhou
        if verificacao_vitoria(letras) == True:
            break
        #se acabar a vida, perdeu
        if cont_vida >= 6:
            print("você perdeu")
            break
        passar = 0
    #fim do jogo e qual era a palavra
    print("fim de jogo!!!")
    print(f"a palavra era {palavra}")
if "__main__"==__name__:
    jogo_forca()