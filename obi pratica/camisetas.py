N = int(input())
T = str(input()).split()
P = int(input())
M = int(input())

totalP = 0
totalM = 0

for i in T:

    if int(i) == 1:
        totalP += 1
    
    else:
        totalM += 1

if totalP == P and totalM == M:
    print('S')

else:
    print('N')