ingresso = float(input('Qual o valor do ingresso:? '))

print('''
[1] - inteira (sem desconto)
[2] - meia entrada (50% de desconto)
[3] - promoção (30% de desconto )

''')

desconto = 0

opcao = int(input('Escolha uma opção acima:'))

match opcao:
    case 1:
        print('------ inteira ------')
        print(f'O valor do seu ingresso é: {ingresso}')

    case 2:
        print('------ meia entrada ------')
        desconto = ingresso * 0.50
        valor_fi = ingresso - desconto
        print(f'O valor do seu ingresso é: {valor_fi}')

    case 3:
        print('------ promoção ------')
        desconto = ingresso * 0.30
        valor_fi = ingresso - desconto
        print(f'O valor do seu ingresso é: {valor_fi}')

    case _:
        print('Opção invalida!!!!!!')  

        