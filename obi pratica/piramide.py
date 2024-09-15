def printNTimes(string, times=1, termination=''):
    print(str(string)*times, end=termination)

N = int(input())
times = 0
for i in range(round(N/2)):
    printNTimes(i+1, N-times)
    times += 2
    print('\n', end='')