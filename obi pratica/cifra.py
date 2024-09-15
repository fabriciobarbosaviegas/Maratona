def cifraDeNlogonia(palavra):

    alfabeto = 'a b c d e f g h i j k l m n o p q r s t u v x z'.split()

    vogais = ['a', 'e', 'i', 'o', 'u']

    palavraCifrada = ''

    for i in palavra:
        if i in alfabeto and not i in vogais:
            palavraCifrada += i + pegarVogalMaisProxima(i, alfabeto) + pegarProximaConsoante(i, alfabeto, vogais)

        else:
            palavraCifrada += i

    return palavraCifrada



def pegarVogalMaisProxima(consoante, alfabeto):

    posicaoVogais = [alfabeto.index('a'), alfabeto.index('e'), alfabeto.index('i'), alfabeto.index('o'), alfabeto.index('u')]
    posicaoConsoante = alfabeto.index(consoante)
    menorPoisacaoDeVogal = posicaoVogais[4]

    for i in posicaoVogais:
        posicaoVogal = posicaoConsoante - i + 2

        if posicaoVogal < menorPoisacaoDeVogal and posicaoVogal > 0:
            menorPoisacaoDeVogal = posicaoVogal
            indiceMenorPosicaoVogal = i


    return alfabeto[indiceMenorPosicaoVogal]



def pegarProximaConsoante(consoante, alfabeto, vogais):
    if consoante != "z":
        contador = 1
        proximaConsoante = alfabeto[alfabeto.index(consoante) + contador]

        while True:
            if not proximaConsoante in vogais:
                break

            else:
                contador += 1
                proximaConsoante = alfabeto[alfabeto.index(consoante) + contador]

        return proximaConsoante

    else:
        return "z"



p = input()

print(cifraDeNlogonia(p))