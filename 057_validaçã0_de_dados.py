sexo = str(input('Informe seu sexo [M/F] : ')).strip().upper()[0] #REMOVE OS ESPAÇOS E PEGA SÓ A 1ª LETRA DA RESPOSTA
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]

#PODE SER USADO
#print('Sexo {} registrado com sucesso!'.format(sexo))

if sexo == 'M':
        print('Sexo Masculino registrado com sucesso!')
if sexo == 'F':
        print('Sexo Feminino registrado com sucesso!')
