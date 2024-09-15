H, P = [int(i) for i in input().split()]
r = round(H/P, 2)
print(f'{r}0') if len(str(r).split('.')[1]) < 2 else print(f'{r}')
