import random

vidas = 5
numero_aleatorio = random.randint(0,100)
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
        print("tente de novo")
        vidas-=1
        print(f"você tem {vidas} vidas")