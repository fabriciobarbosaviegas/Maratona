while True:
    D, N = input().split()
    
    if D == N == '0':
        break
    
    r = N.replace(D, '')
    if r == '':
        print('0')
    elif '0' in r:
        print(int(r))
    else:
        print(r)

