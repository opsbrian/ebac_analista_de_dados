continuar = True
print('-----------CALCULADORA V1.0-----------')

while continuar:
    try:
        num1 = float(input('Digite um valor: '))
        num2 = float(input('Digite outro valor: '))
    except ValueError:
        print('Digite um valor valido')
        continue

    opc = ['[1] SOMA', '[2] SUBTRAI', '[3] MULTIPLICACA', '[4] DIVIDE', '[5] - SAIR']
    print('============ MENU ============')
    print(*opc, sep='\n')
    try:
        opc_usuario = int(input('Digite a opção: '))
        if opc_usuario < 1 or opc_usuario > 5:
            raise ValueError
    except ValueError:
        print('Digite um valor valido, de 1 à 5.')
        continue

    if opc_usuario == 1:
        soma = num1 + num2  
        print(f'{num1} + {num2} = {soma} ')
    elif opc_usuario == 2:
        sub = num1 - num2
        print(f'{num1} - {num2} = {sub} ')
    elif opc_usuario == 3:
        multiplicacao = num1 * num2
        print(f'{num1} * {num2} = {multiplicacao} ')

    elif opc_usuario == 4:
        divisao = num1 / num2
        print(f'{num1} / {num2} = {divisao} ')
    else:
        continuar = False
        print('SAINDO....')