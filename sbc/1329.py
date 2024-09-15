while True:
    n = int(input())

    john = 0
    mary = 0

    if n == 0:
        break

    for j in [int(i) for i in input().split()]:
        if j == 0:
            mary += 1
        else:
            john += 1
        
    print(f"Mary won {mary} times and John won {john} times")
