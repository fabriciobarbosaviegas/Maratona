N = int(input())

if N > 5:
    print(f'{"I"*5}\n{"I"*(N-5)}')

else:
    print(f'{"I"*N if N > 0 else "*"}\n*')