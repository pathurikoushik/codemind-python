a,b=map(int,input().split())
c=[]
ma=0
for i in range(0,a):
    d=list(map(int,input().split()))
    if sum(d)>ma:
        ma=sum(d)
    c.append(d)
m=0
for i in range(0,b):
    s=0
    for j in range(0,a):
        s+=c[j][i]
    if s>m:
        m=s
if ma>m:
    print(ma)
else:
    print(m)