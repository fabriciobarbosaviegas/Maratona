from collections import Counter

p = {0:'A', 1:'B', 2:'C'}
r = input().split()
c = dict(Counter(r))
print(c.values())
print('*') if len(c) <= 1 else print(p[r.index(min(c))])