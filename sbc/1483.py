output = []
grupos = [i for i in range(1, 100)]
grupos.append(0)
N = 3
while True:
    v, m, n = [float(i) if index == 0 else int(i) for index, i in enumerate(input().split())]

    if v == 0 and m == 0 and n == 0: break
 
    if m % 10000 == n % 10000: output.append(v * 3000)
    elif m % 1000 == n % 1000: output.append(v * 500)
    elif m % 100 == n % 100: output.append(v * 50)
    else:
        temp = 0

        for i in range(0, 100, 4): temp += 16 if m % 100 in grupos[i:i+4] and n % 100 in grupos[i:i+4] else 0
        output.append(0.00 if v*temp == 0 else v*temp) 

[print("{:.2f}".format(i)) for i in output]