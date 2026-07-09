while True:
    num1 = input('Insira um número: ')
    num2 = input('Insira outro número: ')

    num1 = float(num1)
    num2 = float(num2)

    print('Escolha a operação')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')

    operacao = input('Insira a operação desejada: ')

    if operacao == "1":
        resultado = num1 + num2
        print(f"O resultado da soma é {resultado}")

    elif operacao == "2":
        resultado = num1 - num2
        print(f"O resultado da subtração é {resultado}")

    elif operacao == "3":
        resultado = num1 * num2
        print(f"O resultado da multiplicação é {resultado}")

    elif operacao == "4":
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado da divisão é {resultado}")
        else:
            print("Erro: divisão por zero")

    else:
        print("Operação impossível!")

    continuar = input("Continuar? (s/n): ").lower()

    if continuar != "s":
        print("Fim das operações")
        break
