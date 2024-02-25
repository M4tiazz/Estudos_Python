from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''\033[m[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa''')
    opção = int(input('\033[mQual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('\033[32mA soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        multi = n1 * n2
        print('\033[32mO resultado entre {} x {} é {}'.format(n1, n2, multi))
    elif opção == 3:
        if n1 > n2:
            print('\033[32mO maior valor entre {} e {} é {}'.format(n1, n2, n1))
        elif n2 > n1:
            print('\033[32mO maior valor entre {} e {} é {}'.format(n1, n2, n2))
        elif n1 == n2:
            print('\033[32mOs números são iguais.')
    elif opção == 4:
        print('\033[mInforme os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('\033[31mFINALIZANDO...')
    else:
        print('\033[31mOpção inválida. Tente novamente!')
    print('\033[33m=-=' * 10)
    sleep(2)
print('\033[34mFim do programa! Volte sempre!')
