def construir_posfixa(prefixa, infixa):
    if not prefixa or not infixa:
        return ""

    raiz = prefixa[0]

    indice_raiz = infixa.index(raiz)

    esquerda_infixa = infixa[:indice_raiz]
    direita_infixa = infixa[indice_raiz + 1:]

    esquerda_prefixa = prefixa[1:1 + len(esquerda_infixa)]
    direita_prefixa = prefixa[1 + len(esquerda_infixa):]

    posfixa_esquerda = construir_posfixa(esquerda_prefixa, esquerda_infixa)
    posfixa_direita = construir_posfixa(direita_prefixa, direita_infixa)

    return posfixa_esquerda + posfixa_direita + raiz


C = int(input())
res = []

for _ in range(C):
    N, S1, S2 = input().split()
    posfixa = construir_posfixa(S1, S2)
    res.append(posfixa)

for r in res:
    print(r)
