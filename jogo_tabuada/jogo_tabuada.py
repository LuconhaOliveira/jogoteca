import random

pontos = 0
while True:
    n1 = random.randint(0,10)
    n2 = random.randint(0,10)
    resp = int(input(f"qual o resultado de {n1} X {n2} "))
    if resp == n1*n2:
        print("acertou")
        pontos+=1
    else:
        print("errou")
        break
print(f"parabens você fez {pontos} pontos")