m = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E"}
output = []

n = int(input())

while n != 0:
    for i in range(n):
        r = [int(j) for j in input().split()]
        c = 0
        for x, y in enumerate(r):
            if y <= 127:
                c += 1
                temp = m[x]
            if c > 1:
                output.append('*')
                break

        if c == 1:
            output.append(temp)
        elif c == 0:
            output.append('*')

    n = int(input())

[print(i) for i in output]