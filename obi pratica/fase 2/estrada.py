#A vizinhança da estrada de uma cidade A é definida como todos os pontos da estrada que são mais próximos do centro
#da cidade A do que do centro de qualquer outra cidade.

#Dados o comprimento total da estrada, de fronteira a fronteira, e as distâncias da fronteira oeste
#até os centros de cada cidade ao longo da nova estrada, escreva um programa para determinar qual a menor vizinhança
#de estrada entre as cidades pelas quais a estrada vai passar.

T = int(input())
N = int(input())
X = []

for i in range(N):
    X.append(int(input()))

X.sort()
print(X)