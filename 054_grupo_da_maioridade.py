from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('''Ao todo tivemos {} pessoas maiores de idade
E também tivemos {} pessoas menores de idade.'''.format(totmaior, totmenor))
