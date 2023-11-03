a,b=map(int,input().split())
s=0
m=0
for i in range(0,a):
    d=list(map(int,input().split()))
    if i%2==0:
        s+=sum(d)
    else:
        m+=sum(d)
print(s,m)