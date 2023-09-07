p,r,t=map(int,input().split())
d=p*((1+r/100.00)**t)
print(f'{d:.2f}')