def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_non_prime_pair(N):
    for x in range(N//2, -1, -1):
        y = N - x
        if not is_prime(x) and not is_prime(y):
            return f"{x} {y}"
    return -1

res = []

for i in range(int(input())):
    n = int(input())
    res.append(find_non_prime_pair(n))

for i in res:
    print(i)