valor = float(input('valor da venda: '))

print('''
[1] - pix (12% de desconto)
[2] - debito (8% de desconto)
[3] - credito (5% de desconto)
[4] - dinheiro (15% de desconto)
''')
# operacao = True
desconto = 0 
opcao = int(input('informe a opção escolhida: '))

match opcao:
    case 1:
        print('---pix---')
        desconto = valor * 0.12
        print(f'Desconto de R$: {desconto:.2f}')

    case 2:
        print('---debito---')
        desconto = valor * 0.08
        print(f'Desconto de R$: {desconto:.2f}')

    case 3:
        print('---credito---')
        desconto = valor * 0.05
        print(f'Desconto de R$: {desconto:.2f}')

    case 4:
        print('---dinheiro---')
        desconto = valor * 0.15
        print(f'Desconto de R$: {desconto:.2f}')


    case _:
        # operacao = False
        print('opção invalida')

# if operacao == True
if opcao in [1, 2, 3, 4]:
#  if desconto != 0:
    valor_final = valor - desconto 
    print(f'\npreço: {valor}')
    print(f'desconto: {desconto}')
    print(f'Total a pagar: {valor_final}')

else:
    print('escolha uma opção acima')
