import random

possibilidades = ["pedra", "papel", "tesoura"]
jogada_pc = random.choice(possibilidades)

print("""1.Pedra
2. Papel
3.Tesoura""")
print("Qual sua jogada?")
jogada = int(input())
print(jogada)
print(jogada_pc)