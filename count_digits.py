a=int(input())
c=list(map(int,input().split()))
for i in range(0,a):
    if c[i]<0:
        c[i]=-c[i]
    print(len(str(c[i])),end=' ')