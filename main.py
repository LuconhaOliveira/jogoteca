import os
from adivinhacao.jogo_adivinhacao import*
from forca.jogo_forca import*
from tabuada.jogo_tabuada import*
from velha.Jogo_da_Velha import*
from pedra_papel_tesoura.jogo_pedra_papel_tesoura import*

os.system("cls")
print("""-----------------
SEJA BEM-VINDE A
  🎮JOGOTECA🎮
-----------------
""")

while True:
    idade = int(input("qual sua idade "))
    if idade<18:
        print("some daqui meo")
        exit()
    elif idade > 120:
        print("não minta idade")
    else:
        break
while True:
    print("""
temos os jogos:
> 1. Jogo da adivinhação
> 2. Jogo da forca
> 3. Jogo da tabuada
> 4. Jogo da velha
> 5. Pedra, papel, tesoura
> 0. Sair
""")
    escolha = int(input("selecione o jogo:"))
    os.system("cls")
    if escolha == 1:
        jogo_adivinhacao()
    if escolha == 2:
        jogo_forca()
    if escolha == 3:
        jogo_tabuada()
    if escolha == 4:
        jogo_velha()
    if escolha == 5:
        jogo_ppt()
    if escolha == 0:
        break
input()