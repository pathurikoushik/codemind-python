#maximum sum of row wise sum of a matrix
a,b=map(int,input().split())
m=0
for i in range(0,a):
    d=list(map(int,input().split()))
    if sum(d)>m:
        m=sum(d)
print(m)