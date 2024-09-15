N = int(input())

M = []

for i in range(N):
    M.append(int(input()))

M.sort(reverse=True)

fl = 0

for i in M:
    if i > fl:
        fl += 1

print(fl)