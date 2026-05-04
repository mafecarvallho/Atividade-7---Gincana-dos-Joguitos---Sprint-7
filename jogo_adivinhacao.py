from random import randint

#Funções

def jogo_adivinhacao():
    variacao = input('Quem tentará adivinhar: o Usuário ou o Computador? ')

    if variacao == 'Computador':
        numero = int(input('Qual o numero? '))
        numero_adivinhado = randint(1, 1023)
        print(numero_adivinhado)

        tentativas = 1

        if numero_adivinhado > numero:
            print('-1')
        elif numero_adivinhado < numero:
            print('1')

        while numero_adivinhado != numero:
            numero_adivinhado = randint(1, 1023)
            print(numero_adivinhado)

            if numero_adivinhado > numero:
                print('-1')
            elif numero_adivinhado < numero:
                print('1')

            tentativas += 1

        print('0')
        print('\nO computador acertou o numero!')
        print(f'Numero de tentativas: {tentativas}')

    else:
        numero = randint(1, 1023)
        numero_adivinhado = int(input('Adivinhe o numero: '))

        if numero_adivinhado > numero:
            print('-1')
        elif numero_adivinhado < numero:
            print('1')

        tentativas = 1

        while numero_adivinhado != numero:
            numero_adivinhado = int(input('Adivinhe o numero: '))

            if numero_adivinhado > numero:
                print('-1')
            elif numero_adivinhado < numero:
                print('1')

            tentativas += 1

        print('0')
        print('\nVocê acertou o numero!')
        print(f'Numero de tentativas: {tentativas}')


# BP
jogo_adivinhacao()


