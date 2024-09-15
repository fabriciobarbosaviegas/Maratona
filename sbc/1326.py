output = []

while True:
    R = []
    results = []

    n = int(input())

    if n == 0: break

    c = 0

    for i in range(n):
        a = input().replace('->', '+').split(' + ')
        R += a
        results.append(a[2])

    for i in results: c += 1 if R.count(i) > 1 else 0
        
    output.append(f'{R[n*3-1]} requires {int(c/2) if c != 0 else 1} containers')

[print(i) for i in output]