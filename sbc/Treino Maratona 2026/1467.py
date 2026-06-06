while True:
    try:
        A, B, C = [int(i) for i in input().split()]

        if A == B == C:
            print('*')

        if A == B != C:
            print('C')

        if A != B == C:
            print('A')

        if A == C != B:
            print('B')
    except EOFError:
        break