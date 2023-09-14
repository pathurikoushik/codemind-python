a,b=map(int,input().split())
c=min(a,b)
while c>0:
    if a%c==0 and b%c==0:
        print(c)
        break
    c=c-1