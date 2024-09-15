output = []
N, M = [int(i) for i in input().split()]

for i in range(N):
    a = input()
    output.append("F") if "not" in a else output.append("V")

print(output) 