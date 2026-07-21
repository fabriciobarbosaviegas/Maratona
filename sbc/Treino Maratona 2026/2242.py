vogais = ['a', 'e', 'i', 'o', 'u']

r = input()
r = [i for i in r if i in vogais]

if r == list(reversed(r)):
    print('S')
else:
    print('N')