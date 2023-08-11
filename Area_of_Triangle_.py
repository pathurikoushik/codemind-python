a,b,c=map(int,input().split())
s=(a+b+c)/2
s=(s*(s-a)*(s-b)*(s-c))**0.5
print(f'{s:.2f}')