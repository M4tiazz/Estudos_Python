from random import randint
computador = randint(0,10) #COMPUTADOR SORTEIA UM NÚMERO
print('''Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi ?''')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('\033[mQual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[31mUm pouco mais... Tente novamente.')
        elif jogador > computador:
            print('\033[31mUm pouco menos... Tente novamente.')
print('\033[32mAcertou com {} tentativas. Parabéns!'.format(palpites))
