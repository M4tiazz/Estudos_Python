print('=' * 30)
print(f'{"10 TERMOS DE UMA PA":^30}')
print('=' * 30)
p1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = p1 + (10 - 1) * razão
for c in range(p1, décimo + razão, razão):
    print('{} '.format(c), end='→ ')
print('ACABOU')
