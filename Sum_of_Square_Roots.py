a,b=map(int,input().split())
c=0
for i in range(a,b+1):
    c=c+(i**0.5)
print(f'{c:.2f}')