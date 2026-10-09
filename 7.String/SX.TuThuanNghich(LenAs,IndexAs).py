def palindrome(s):
    t=s[::-1]
    return s==t;

if __name__=='__main__':
    s=input()
    s=s.split()
    a=set()
    for item in s:
        if palindrome(item)==True:
            a.add(item)
    a=list(a)
    a.sort(key=lambda x: (len(x), s.index(x)))
    a=' '.join(a)
    print(a)