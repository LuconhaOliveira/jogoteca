campos = [1,2,3,4,5,6,7,8,9]
velha = (1,2,3,4,5,6,7,8,9)
jogador = "X"
shadow = '''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⣶⣶⣶⣶⣦⣤⣀⣴⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠈⢿⣤⣀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⣘⣿⣿⣿⡒⠿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⢿⣿⣿⣿⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣦⣽⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠙⠛⠿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣰⠘⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢰⣿⡇⠘⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠋⠘⠛⠠⠤⠼⢿⣯⣴⣶⡄⣤⢳⡦⠄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠘⠳⢦⡀⠀⢀⡼⠏⣿⣿⣿⣿⡎⡇⠀⠀⠀⢀
⠀⣤⣤⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣾⣟⡛⠉⠀⠀⢹⣿⠿⢿⡿⠃⠀⠀⣰⠏
⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣅⠀⠀⣸⡏⠠⣤⣀⠀⢀⡞⠁⠀
⠀⠀⠀⠀⠈⠙⠛⠻⠿⠿⣿⣿⣿⡿⠿⠿⠛⠉⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⣰⣿⣿⣷⣦⡉⣷⠞⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⢿⣿⣿⡿⠻⣿⣿⣿⣿⣿⡏⠹⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣷⣰⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⡟⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⢤⣭⡿⣿⣿⣿⡿⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⣠⠶⢟⣿⣿⣿⠇⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠏⠀⢀⣼⣿⣿⡏⣠⠇⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⠳⠋⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣶⠀⠀⠀⣿⣿⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠿⣿⣿⣿⣿⣿⡃⠀⢠⣤⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣤⣀⣈⣉⣭⣽⡗⢦⣸⡿⠿⢿⢿⠿⠿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣷⠈⣯⣤⣤⣤⣤⣤⣴⠾⠅⠀⠀⠀⠀⢀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠁⡴⠀⠉⠻⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠈⠙⣶⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠂⣁⠀⠀⠇⣿⣿⡟⣿⠛⠍⡻⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⣸⢿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠳⠶⠾⠿⠿⠿⠋⢰⡏⠀⢀⡄⠀⠉⠛⠿⣿⠻⣿⡶⠷⠞⠛⣁⣾⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣾⣁⣤⣤⣄⣼⡿⠀⠈⠙⠛⠛⠛⠉⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''
#mostrando campos
print(f'{campos[0]} | {campos[1]} | {campos[2]}')
print('---------')
print(f'{campos[3]} | {campos[4]} | {campos[5]}')
print('---------')
print(f'{campos[6]} | {campos[7]} | {campos[8]}')
while True:
    #jogada
    print(f'o proximo a jogar é {jogador}')
    n = int(input('escolha a posição: '))
    while True:
        #colocando num lugar vazio
        if campos[n-1] == "X" or campos[n-1] == "O":
            n = int(input('escolha um campo vazio: '))
        else:
            break
    #colocando no campo e mostrando
    campos[n-1] = jogador
    print(f'{campos[0]} | {campos[1]} | {campos[2]}')
    print('---------')
    print(f'{campos[3]} | {campos[4]} | {campos[5]}')
    print('---------')
    print(f'{campos[6]} | {campos[7]} | {campos[8]}')
    #verificando vitória
    if campos[0] == jogador and campos[1] == jogador and campos[2] == jogador:
        print(f'o {jogador} venceu')
        break
    if campos[3] == jogador and campos[4] == jogador and campos[5] == jogador:
        print(f'o {jogador} venceu')
        break
    if campos[6] == jogador and campos[7] == jogador and campos[8] == jogador:
        print(f'o {jogador} venceu')
        break
    if campos[0] == jogador and campos[3] == jogador and campos[6] == jogador:
        print(f'o {jogador} venceu')
        break
    if campos[1] == jogador and campos[4] == jogador and campos[7] == jogador:
        print(f'o {jogador} venceu')
        break
    if campos[2] == jogador and campos[5] == jogador and campos[8] == jogador:
        print(f'o {jogador} venceu')
        break
    if campos[0] == jogador and campos[4] == jogador and campos[8] == jogador:
        print(f'o {jogador} venceu')
        break
    if campos[2] == jogador and campos[4] == jogador and campos[6] == jogador:
        print(f'o {jogador} venceu')
        break
    #verificando se deu velha
    if campos[0] != velha[0] and campos[1] != velha[1] and campos[2] != velha[2] and campos[3] != velha[3] and campos[4] != velha[4] and\
          campos[5] != velha[5] and campos[6] != velha[6] and campos[7] != velha[7] and campos[8] != velha[8]:
        print('deu velha')
        print(shadow)
        break
    #modificando jogador
    if jogador == "X":
        jogador ="O"
    else: 
        jogador = "X"