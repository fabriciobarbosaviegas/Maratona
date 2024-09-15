d = int(input())

d -= 3

d /= 8

d = d - int(str(d).split('.')[0])

if(d == 0.5):
    print(2)

elif(d > 0.5):
    print(3)

else:
    print(1)