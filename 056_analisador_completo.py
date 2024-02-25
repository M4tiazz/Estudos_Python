totidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'{" {}ª PESSOA ":=^20}'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    totidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if idade <= 20 and sexo in 'Ff':
        totmulher20 += 1
médiaidade = totidade / p
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho é {} com {} anos'.format(nomevelho, maioridadehomem))
print('Ao todo são {} mulher(es) com menos de 20 anos'.format(totmulher20))
