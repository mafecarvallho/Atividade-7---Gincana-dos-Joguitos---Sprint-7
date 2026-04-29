
from random import randint

variacao = input('Quem tentará adivinhar: o Usuário ou o Computador? ')
if variacao == 'Computador':
     numero = int(input('Qual o numero? '))
     numero_adivinhado = randint(1, 1023)
     print(numero_adivinhado)

     tentativas =1

     if numero_adivinhado > numero:
        print('-1')
     elif numero_adivinhado < numero:
        print('1')

     while numero_adivinhado != numero:
        numero_adivinhado = randint(1,1023)
     if numero_adivinhado > numero:
        print('-1')
     elif numero_adivinhado < numero:
        print('1')
        tentativas +=1
    

     print('0')
     print('\nO computador acertou o numero!')
     print(f'Numero de tentativas: {tentativas}')

else: 
    numero = randint(1 , 1023)
    print(numero)
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
        tentativas +=1

    
    print('0')
    print('\nVoce acertou o numero!')
    print(f'Numero de tentativas: {tentativas}')



