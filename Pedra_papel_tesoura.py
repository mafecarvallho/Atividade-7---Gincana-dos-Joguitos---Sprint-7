

from random import randint 


total_rodadas = int(input('Rodadas jogadas: '))

pontuacao_total = 0
cont = 0

while cont < total_rodadas:
    cont +=1 

    escolha_usuario = input('Pedra, Papel ou Tesoura?: ')

    numero = randint(1,3)

    if numero == 1:
        sorteio = 'Pedra'
    elif numero == 2:
        sorteio = 'Papel'
    elif numero == 3:
        sorteio = 'Tesoura'

    print(sorteio)

    if escolha_usuario == 'Pedra':
        if sorteio == 'Pedra':
            print('Empate')
        elif sorteio == 'Papel':
            print('Derrota')
        else:
            print('Vitoria')
            pontuacao_total +=1

    if escolha_usuario == 'Papel':
        if sorteio == 'Papel':
            print('Empate')
        elif sorteio == 'Tesoura':
            print('Derrota')
        else:
            print('Vitoria')
            pontuacao_total +=1


    if escolha_usuario == 'Tesoura':
        if sorteio == 'Tesoura':
            print('Empate')
        elif sorteio == 'Pedra':
            print('Derrota')
        else:
            print('Vitoria')
            pontuacao_total +=1

print('\nFIM DE JOGO')
print(f'Pontuação total: {pontuacao_total}')