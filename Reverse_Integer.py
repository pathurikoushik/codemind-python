a=int(input())
c=0
if a<0:
    c=1
    a=-a
b=str(a)
b=b[::-1]
a=int(b)
if c==0:
    print(a)
else:
    print(-a)