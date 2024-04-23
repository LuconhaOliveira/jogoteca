import os

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
        print("""Selecione o jogo:
> 1. Jogo da forca
> 2. Jogo da velha
> 3. Jogo da adivinhação
> 4. Jogo da tabuada
""")
        break
