output = []

while True:
    n = int(input())

    if n == 0:
        break

    contest = {}
    p = 0
    s = 0

    for i in range(n):
        t = input().split()

        if t[0] in contest:
            contest[t[0]][0] = t[1]
            contest[t[0]].append(t[2])
        else:
            contest[t[0]] = t[1:]
    
    for i in contest:
        if 'correct' in contest[i]:
            p += 1
            s += int(contest[i][0]) + (contest[i].count('incorrect')*20)

    output.append(f'{p} {s}')

for i in output:
    print(i)