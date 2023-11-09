a,b=map(int,input().split())
c=[]
for i in range(0,a):
    d=list(map(int,input().split()))
    c.append(d)
for i in range(0,b):
    s=0
    for j in range(0,a):
       s+=c[j][i]
    print(s,end=' ')