N = int(input())
ehPar = N % 2 == 0
times = N
c = 1
meio = round(N/2+0.1)

while c <= meio:

    print(f'{"".join(str(i)+" " for i in list(range(1, c)))}{(str(c)+" ")*times}{" ".join(str(i) for i in list(range(c-1, 0, -1)))}')
    times = times - 2 if times-2 > 0 else 0
    c += 1

c -= 1 if not ehPar else 0
times += 1 if not ehPar else 0

while c > 1:

    c -= 1
    times += 2
    print(f'{"".join(str(i)+" " for i in list(range(1, c)))}{(str(c)+" ")*times}{" ".join(str(i) for i in list(range(c-1, 0, -1)))}')

