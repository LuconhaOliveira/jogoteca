import random

possibilidades = ["pedra", "papel", "tesoura"]
jogada_pc = random.choice(possibilidades)

print("""1.Pedra
2. Papel
3.Tesoura""")
print("Qual sua jogada?")
jogada = int(input())
if jogada_pc == "pedra" and jogada == 2:
    print("Você ganhou!!!")
if jogada_pc == "pedra" and jogada == 1:
    print("Empate!!!")
if jogada_pc == "pedra" and jogada == 3:
    print("Você perdeu!!!")
if jogada_pc == "papel" and jogada == 3:
    print("Você ganhou!!!")
if jogada_pc == "papel" and jogada == 2:
    print("Empate!!!")
if jogada_pc == "papel" and jogada == 1:
    print("Você perdeu!!!")
if jogada_pc == "tesoura" and jogada == 1:
    print("Você ganhou!!!")
if jogada_pc == "tesoura" and jogada == 3:
    print("Empate!!!")
if jogada_pc == "tesoura" and jogada == 2:
    print("Você perdeu!!!")