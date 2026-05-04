def calcular( operando_1 , operacao , operando_2):

    if operacao== '+':
        return operando_1 + operando_2
    
    elif operacao == '-':
        return operando_1 - operando_2
    
    elif operacao == 'x' :
        return operando_1 * operando_2
    
    elif operacao == '/':
        if operando_2 != 0:
            return operando_1 / operando_2



def calculadora():
    memoria = None  

    while True:
        if memoria is None:
            operando_1 = float(input('Operando 1: '))
            memoria = operando_1

        else:
            operacao = input('Operação: ').lower()

            if operacao == 'c':
                memoria = None
                print('Memória limpa!\n')

            else:
                operando_2 = float(input('Operando 2: '))
                memoria = calcular(memoria, operacao, operando_2)

                print(f'Resultado: {memoria}')

# BP

calculadora()