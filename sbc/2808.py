index = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

possiveis = []

inicial, final = [i for i in input().split()]

possiveis.append(f'{index[inicial[0]]-1}{int(inicial[1])-2}')
possiveis.append(f'{index[inicial[0]]-2}{int(inicial[1])-1}')
possiveis.append(f'{index[inicial[0]]-1}{int(inicial[1])+2}')
possiveis.append(f'{index[inicial[0]]-2}{int(inicial[1])+1}')

possiveis.append(f'{index[inicial[0]]+1}{int(inicial[1])+2}')
possiveis.append(f'{index[inicial[0]]+2}{int(inicial[1])+1}')
possiveis.append(f'{index[inicial[0]]+1}{int(inicial[1])-2}')
possiveis.append(f'{index[inicial[0]]+2}{int(inicial[1])-1}')

if f'{index[final[0]]}{final[1]}' in possiveis:
    print('VALIDO')
else:
    print('INVALIDO')