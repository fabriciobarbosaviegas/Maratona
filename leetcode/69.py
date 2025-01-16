#Você não deve usar nenhuma função ou operador expoente integrado.

def mySqrt(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    
    min = 1
    max = x

    while min <= max:
        mid = (min + max) // 2
        guess = mid * mid

        if guess == x:
            return mid
        if guess < x:
            min = mid + 1
        else:
            max = mid - 1
    
    return max

x1 = 4
x2 = 8

print(mySqrt(x1))
print(mySqrt(x2))