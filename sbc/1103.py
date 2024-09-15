output = []
while True:
    a = [int(i) for i in input().split()]
    if a == [0, 0, 0, 0]: break
    f = 24*60+a[3] if a[2] == 0 else a[2]*60+a[3]
    i = 24*60+a[1] if a[0] == 0 else a[0]*60+a[1]
    output.append(f - i) if i < f else output.append((f+1440)- i)

[print(i) for i in output]