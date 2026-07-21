while True:
    D, N = input().split()
    
    if D == N == '0':
        break
    
    r = N.replace(D, '')
    if r == '':
        print('0')
    elif '0' in r:
        n = r.split('0')
        if n[0] == '':
            print('0')
    else:
        print(r)

