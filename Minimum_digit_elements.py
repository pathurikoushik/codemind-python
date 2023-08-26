n=int(input())
a=list(map(int,input().split()))
b=min(a)
b=len(str(b))
c=0
for i in a:
    if len(str(i))==b:
        c=c+1
print(c)