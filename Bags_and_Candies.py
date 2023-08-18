n,k,m=map(int,input().split())
cbp=k*m
if n%cbp==0:
    print(n//cbp)
else:
    print(n//cbp+1)