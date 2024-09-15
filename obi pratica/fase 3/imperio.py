from collections import defaultdict

N =  int(input())
arestas = defaultdict(list)
print(arestas)
#AB = []

for i in range(N-1):
    AB = [int(i) for i in input().split()]
    arestas[AB[0]].append(AB[1])
    #AB.append([int(i) for i in input().split()])

print(arestas)