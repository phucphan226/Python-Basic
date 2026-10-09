n=int(input())
dem1=1
for i in range(1, n+1, 1):
    for j in range(1, n+1, 1):
        print(dem1, end=' ')
        dem1+=1
    print()
print()

for i in range(1, n+1, 1):
    dem2=i
    for j in range(1, n+1, 1):
        print(dem2, end=' ')
        dem2+=1
    print()
print()

for i in range(1, n+1, 1):
    for j in range(n, 0, -1):
        if j>i:
            print('~', end='')
        else:
            print(i, end='')
    print()
print()

for i in range(1, n+1, 1):
    dem=n-1
    gt=i
    for j in range(1, n+1, 1):
        if j<=i:
            if j==1:
                print(i, end=' ')
            else:
                gt+=dem
                print(gt, end=' ')
                dem-=1
    print()
print()