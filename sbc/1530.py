from collections import Counter

n = 'abczbd'
s = 0

temp = []
for i in range(len(n)+1):
    for j in range(len(n)+1):
        s+=1   
        if n[i:j] != '':
            temp.append(n[i:j])
print(s)
print(len(temp))
print(len(set(temp)))
print(len(temp) - 3)
print(Counter(n))