import random
def jogo_adivinhacao():
    vidas = 5
    dificuldade = int(input("""selecione a dificuldade:
    1. 1 a 10
    2. 1 a 50
    3. 1 a 100
    """))
    if dificuldade == 1:    
        numero_aleatorio = random.randint(1,10)
    if dificuldade == 2:    
        numero_aleatorio = random.randint(1,50)
    if dificuldade == 3:    
        numero_aleatorio = random.randint(1,100)
    print(f"voce tem {vidas} vidas")
    while True:
        chute = int(input("chute um numero: "))
        if chute == numero_aleatorio:
            print("acertou")
            break
        else:
            if chute > numero_aleatorio:
                print("menor")
            elif chute < numero_aleatorio:
                print("maior")
            vidas-=1
            print(f"você tem {vidas} vidas")
if "__main__"==__name__:
    jogo_adivinhacao()