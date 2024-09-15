N = int(input())
fi = input().split()

M = int(input())
fd = input().split()

for i in fd:
    fi.remove(i)

print(' '.join(fi))