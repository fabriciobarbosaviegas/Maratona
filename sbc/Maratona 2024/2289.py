xy = []

while True:
    xy.append([int(i) for i in input().split()])

    if sum(xy[len(xy)-1]) == 0:
        break

for i in xy[:len(xy)-1]:
    print(bin(i[0] ^ i[1]).count('1'))