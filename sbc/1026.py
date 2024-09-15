r = []
while True:
  try:
    A, B =  [int(i) for i in input().split()]
    r.append(int(bin(A^B),2))
  except EOFError:
    for i in r:
       print(i)