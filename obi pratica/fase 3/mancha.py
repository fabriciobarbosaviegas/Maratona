M = []

for i in range(int(input())):
    M.append(input().split('.'))

r = 'S'

for i in M:
    if len(i) - i.count("") > 1:
        r = 'N'
        break
    
print(r)