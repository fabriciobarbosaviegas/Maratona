while True:
    ts = []
    tc = 0

    try:
        N = int(input())
        for i in range(N):
            t, c = [int(i) for i in input().split(' ')]

            if(N == 1):
                ts.append(0)
                break
            else:
                if(t <= c):
                    tc += c
        ts.append(tc)
    except EOFError:
        [print(i) for i in ts]
        break