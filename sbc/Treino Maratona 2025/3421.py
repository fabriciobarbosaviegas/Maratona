K = int(input())
L, R = map(int, input().split())

buffer = []      
pos = 0          
n = 0            

while pos <= R:
    s = str(n)
    len_s = len(s)

    if pos + len_s >= L:
        start = max(0, L - pos)
        end = min(len_s, R - pos + 1)
        buffer.append(s[start:end])

    pos += len_s
    n += 1

s = ''.join(buffer)

max_val = 0
n = len(s)
for i in range(n):
    for d in range(1, K+1):
        if i + d > n:
            break
        num = int(s[i:i+d])
        if num > max_val:
            max_val = num

print(max_val)
