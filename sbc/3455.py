A, B, C = [int(i) for i in input().split()]
m = input()

if(m == "A"):
    A += (C*5)/2
    A += (B*3)/2
    print(int(A))

elif(m == "B"):
    A += (C*5)/2
    B += (A*2)/3
    print(int(B))

else:
    A += (B*3)/2
    print(A)
    C += (A*2)/3
    print(C)