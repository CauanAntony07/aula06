for i in range(5):
    print(f'\nVENDA {i + 1}')
    venda = float(input('Valor da venda: '))

if venda >= 200:
    desconto = venda * 10
    valor_fi = venda - desconto
    print(f'valor: {valor_fi}')

elif venda < 200:
    desconto = 0 
    valor_fi = venda - desconto
    print(f'valor: {valor_fi}')
