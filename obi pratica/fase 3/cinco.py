def ehDivisivel(n):
    if n % 5 == 0:
        return True
    else:
        return False

N = int(input())
D = input().split(' ')
Do = sorted(list(set(D)), reverse=True)
#print(Do)
temp = 0
max = -1

for i in range(N):
    temp = D[i]
    for j in range(len(Do)):
#        print(temp)
        D[i] = Do[j]
        concat = int(''.join(D))

        if concat == 732105697540:
            print(concat)

        if ehDivisivel(concat) and concat > max:
            max = concat
    
    D[i] = temp

print(max)