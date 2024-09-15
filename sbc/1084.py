output = []

while True:
    N, D = [int(i) for i in input().split()]
    if N == 0 and D == 0: break
    digi = [int(i) for i in input()]

    removeDigi = sorted(digi, reverse=True)[N-D:]

    [digi.remove(i) for i in removeDigi]
    output.append(''.join(map(str, digi)))

[print(i) for i in output]