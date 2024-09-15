VOGAIS = ['a', 'e', 'i', 'o', 'u']
ALFABETO = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']

def vogaisProximas(letra, posicao):
    direita = 0
    esquerda = 0

    while(not ALFABETO[posicao] in VOGAIS):
        posicao -= 1
        direita += 1

    posicao = ALFABETO.index(letra)
    
    while(not ALFABETO[posicao] in VOGAIS):
        posicao += 1
        esquerda += 1

    return direita, esquerda

def proximaConsoante(posicao):
    posicao += 1
    while(ALFABETO[posicao] in VOGAIS):
        posicao += 1
    
    return ALFABETO[posicao]

palavra = input()
novapalavra = ''

for letra in palavra:
    if not letra in VOGAIS:
        novapalavra += letra

        posicao = ALFABETO.index(letra)
        direita, esquerda = vogaisProximas(letra, posicao)

        if(direita < esquerda):
            novapalavra += ALFABETO[posicao-direita]
        elif(esquerda < direita):
            novapalavra += ALFABETO[posicao+esquerda]
        else:
            novapalavra += ALFABETO[posicao-direita]
        
        novapalavra += proximaConsoante(posicao)

    else:
        novapalavra += letra

print(novapalavra)