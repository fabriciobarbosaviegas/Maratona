xyz = []

while True:
    xyz.append([int(i) for i in input().split()])

    if sum(xyz[len(xyz)-1]) == 0:
        break

for x in xyz[:len(xyz)-1]:
    if(x[0] == x[2] and x[1] == x[3]):
        print(0)
    elif(x[0] == x[2] or x[1] == x[3] or abs(x[0] - x[2]) == abs(x[1] - x[3])):
        print(1)
    else:
        print(2)