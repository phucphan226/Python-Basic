n=int(input())
for i in range(1, n+1, 1):
    for j in range(1, n+1, 1):
        if j<=i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()

for i in range(1, n+1, 1):
    for j in range(n, 0, -1):
        if i<=j:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()

for i in range(1, n+1, 1):
    for j in range(n, 0, -1):
        if j<=i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()

for i in range(1, n+1, 1):
    for j in range(1, n+1, 1):
        if j>=i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()

for i in range(1, n+1, 1):
    for j in range(1, n+1, 1):
        if j==1 or i==n or j==i:
            print('*', end='')
        else:
            print(' ', end='')
    print()