d = int(input())
a = int(input())
n = int(input())

if(n==1):
    print(31*d)
elif(n==2):
    print((31-(n-1))*(d + a))
elif(n >= 3 and n <= 15):
    print((31-(n-1))*(d + (n-1) * a))
else:
    print((31-(n-1))*(d + 14 * a))