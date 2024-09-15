ML = []
c = 0

for i in range(int(input())):
    ML.append(input().split())

ML.sort() 

for i in range(len(ML)-1):
    if ML[i][0] == ML[i+1][0] and ML[i][1] != ML[i+1][1]:
        c += 1

print(c)