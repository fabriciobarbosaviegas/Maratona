from collections import Counter

ladrilhos = []
h, l = [int (i) for i in input().split()]

for i in range(h):
    ladrilhos.append([int(i) for i in input()])

print([list(Counter(i)) for i in ladrilhos])