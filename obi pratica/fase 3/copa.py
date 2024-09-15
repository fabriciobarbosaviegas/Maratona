N, F, R = [int(i) for i in input().split()]

ferrovias = []

for i in range(F):
    ferrovias.append(input().split())

rodovias = []

for i in range(R):
    rodovias.append(input().split())

print(f'ferrovias: {ferrovias}\nrodovias: {rodovias}')