def dectohex(n):
    if n<=9:
        print(n, end='')
    elif n==10:
        print('A', end='')
    elif n==11:
        print('B', end='')
    elif n==12:
        print('C', end='')
    elif n==13:
        print('D', end='')   
    elif n==14:
        print('E', end='')
    elif n==15:
        print('F', end='')
    else:
        dectohex(n//16)
        if n%16<=9:
            print(n%16, end='')
        elif n%16==10:
            print('A', end='')
        elif n%16==11:
            print('B', end='')
        elif n%16==12:
            print('C', end='')
        elif n%16==13:
            print('D', end='')   
        elif n%16==14:
            print('E', end='')
        elif n%16==15:
            print('F', end='')

if __name__=='__main__':
    n=int(input())
    dectohex(n)