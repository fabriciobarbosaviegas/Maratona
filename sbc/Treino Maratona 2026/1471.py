while True:
    try:
        N, R = [int(i) for i in input().split()]
        retornou = [int(i) for i in input().split()]
        retornou.sort()
        print(' '.join(sorted(set(range(1, N)) - set(retornou))) if N > R else '*')
    except EOFError:
        break