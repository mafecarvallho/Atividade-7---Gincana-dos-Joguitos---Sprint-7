import random

# Funções 

def palavra():
    lista_palavras = ['cachorro', 'gato', 'pato', 'passaro', 'tigre', 'leao', 'elefante', 'girafa', 'zebra', 'macaco' ]
    indice = random.randint(0, 9)
    return lista_palavras[indice]


def validade_letras(texto):
    cont = 0
    while cont < len(texto):
        if not (texto[cont] >= 'a' and texto[cont] <= 'z'):
            return False
        cont += 1
    return True
            



def letra_na_palavra(palavra_escolhida, letra):
    cont = 0
    while cont < len(palavra_escolhida):
        if palavra_escolhida[cont] == letra:
            return True
        cont += 1
    return False 
        

def letra_na_lista(letra, lista):
    cont = 0
    while cont < len(lista):
        if lista[cont] == letra:
            return True
        cont += 1
    return False


def letras_adivinhadas(palavra_escolhida, letras_descobertas):
    cont = 0
    while cont < len(palavra_escolhida):
        if letra_na_lista(palavra_escolhida[cont], letras_descobertas):
            print(palavra_escolhida[cont], end=' ')
        else:
            print('-', end=' ')
        cont += 1
    


#BP

jogar = 'sim'
while jogar == 'sim':

    palavra_escolhida = palavra()
    vidas = 6
    letras_descobertas = []
    vitoria = False

    while vidas > 0 and vitoria == False:

        print(f'Vidas: {vidas}')
        letras_adivinhadas(palavra_escolhida, letras_descobertas)

        chute = input('Digite uma letra ou palavra: ')

        if len(chute) == 0:
            print('Digite algo')

        elif validade_letras(chute) == False:
            print('Digite apenas letras')

        elif len(chute) == 1:

            if letra_na_lista(chute, letras_descobertas):
                print('Letra ja chutada')

            elif letra_na_palavra(palavra_escolhida, chute):
                letras_descobertas.append(chute)
                print('Acertou')

            else:
                vidas -= 1
                print('Errou')

        elif len(chute) > 1:

            if chute == palavra_escolhida:
                vitoria = True
            else:
                vidas -= 1
                print('Errou')

        ganhar = True
        cont = 0

        while cont < len(palavra_escolhida):
            if letra_na_lista(palavra_escolhida[cont], letras_descobertas) == False:
                ganhar = False
            cont += 1

        if ganhar:
            vitoria = True

    if vitoria:
        print(f'Você venceu! Palavra: {palavra_escolhida}')
    else:
        print(f'Você perdeu! Palavra: {palavra_escolhida}')

    jogar = input('Quer jogar de novo?: ')