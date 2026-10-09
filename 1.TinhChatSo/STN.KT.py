def palindrome(n):
    tmp=n
    ln=0
    while n!=0:
        ln=ln*10+n%10
        n//=10
    return ln==tmp

if __name__=='__main__':
    n=int(input())
    if palindrome(n)==True:
        print('YES')
    else:
        print('NO')