a,b=map(int,input().split())
s=0
m=0
c=[]
for i in range(0,a):
    d=list(map(int,input().split()))
    c.append(d)
for i in range(0,a):
    for j in range(0,b):
        if c[i][j]%2==0:
            s+=c[i][j]
        else:
            m+=c[i][j]
print(s,m)
