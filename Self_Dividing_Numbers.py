def se(a):
    t=a
    while t!=0:
        b=t%10
        t=t//10
        if b==0 or a%b != 0:
            return 0
    return 1
a=int(input())
b=int(input())
for i in range(a,b+1):
    if se(i):
        print(i,end=' ')