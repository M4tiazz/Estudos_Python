n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(n1, n2, média))

if média >= 7:
    print('O aluno está APROVADO!')

#elif média 7 > média >= 5: (PODE SER USADO PARA DEMONSTRAR O "ENTRE X E Y")
elif média >= 5 and média < 7:
    print('O aluno está em RECUPERAÇÃO!')

elif média < 5:
    print('O aluno está REPROVADO!')
