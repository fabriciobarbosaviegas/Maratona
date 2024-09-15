count = 0

def posicionar(t, x, y):
    tab = t.copy()
    print(id(tab))
    print(id(t))
    for i in range(len(tab[0])):
        tab[x][i] = '*'
        tab[i][y] = '*'
        
        if y+abs(x-i) < len(tab[0]):
            tab[i][y+abs(x-i)] = '*'

        if y-abs(x-i) >= 0:
            tab[i][y-abs(x-i)] = '*'
    
    return tab
      
def montar(tab, pos, n):
    #print(id(tab))
    for i in range(len(tab)):
        #print(pos, i)
        #if pos == 0:
            #for ii in tab: print(ii)
            #print('\n\n')

        if tab[pos][i] == '.':
            if(pos + 1 == n):
                global count
                count += 1
            else:
                temp = posicionar(tab, pos, i)
                montar(temp, pos+1, n)

caso = 0
while True:
    caso += 1
    count = 0
    a = int(input())
    if a == 0: break

    tabuleiro = []
    for i in range(a):
        tabuleiro.append(list(input()))

    montar(tabuleiro, 0, a)

    print("Case "+str(caso)+": "+ str(count))