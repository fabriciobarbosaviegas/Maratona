N = int(input())
s = input().split('b')
print(sum([i.count('a') if 'aa' in i else 0 for i in s])) if N >= 2 else print(0)