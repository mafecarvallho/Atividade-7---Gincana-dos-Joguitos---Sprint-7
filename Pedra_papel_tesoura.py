from random import randint 

def jogada_computador():
    numero = randint(1, 3)
    if numero == 1:
        return 'pedra'
    elif numero == 2:
        return 'papel'
    else:
        return 'tesoura'


total_rodadas = int(input('Rodadas jogadas: '))

pontuacao_total = 0
cont = 0

while cont < total_rodadas:
    cont += 1 

    escolha_usuario = input('Pedra, Papel ou Tesoura?: ')
    sorteio = jogada_computador()

    print(f'Computador: {sorteio}')

    if escolha_usuario == sorteio:
        print('Empate')

    elif escolha_usuario == 'pedra':
        if sorteio == 'papel':
            print('Derrota')
        else:
            print('Vitoria')
            pontuacao_total += 1

    elif escolha_usuario == 'papel':
        if sorteio == 'tesoura':
            print('Derrota')
        else:
            print('Vitoria')
            pontuacao_total += 1

    elif escolha_usuario == 'tesoura':
        if sorteio == 'pedra':
            print('Derrota')
        else:
            print('Vitoria')
            pontuacao_total += 1

    else:
        print('Jogada inválida!')

print('\nFIM DE JOGO')
print(f'Pontuação total: {pontuacao_total}')