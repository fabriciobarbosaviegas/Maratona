while True:
    K = int(input())

    if K == 0:
        break

    divisa = [int(i) for i in input().split()]

    for _ in range(K):
        # x = leste/oeste | y = norte/sul
        x, y = [int(i) for i in input().split()]

        if x in divisa or y in divisa:
            print('divisa')

        if x > divisa[0] and y > divisa[1]:
            print('NE')
        if x < divisa[0] and y > divisa[1]:
            print('NO')
        if x > divisa[0] and y < divisa[1]:
            print('SE')
        if x < divisa[0] and y < divisa[1]:
            print('SO')