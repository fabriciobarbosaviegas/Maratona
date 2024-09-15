A = int(input())
B = int(input())

L = round(A/4+0.5)

if B != ((L+1)-2)*(L-2):
    print('-1 -1')

else:
    H = round((B+A)/L)

    print(f'{L} {H}')