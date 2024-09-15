MOD = 998244353

def geraParentese(n):
    def rastreio(s='', left=0, right=0):
        if len(s) == n:
            if left == right:
                result.append(s)
            return
        if left < n // 2:
            rastreio(s + '(', left + 1, right)
        if right < left:
            rastreio(s + ')', left, right + 1)
    
    result = []
    rastreio()
    return result

def countSub(parentheses_list, substring):
    count = 0
    for p in parentheses_list:
        count += p.count(substring)
    return count

def valido(N, S):
    if N % 2 != 0:
        return 0
    
    parenteseValido = geraParentese(N)
    total = countSub(parenteseValido, S)
    return total % MOD

N = int(input())
S = input()
print(valido(N, S))