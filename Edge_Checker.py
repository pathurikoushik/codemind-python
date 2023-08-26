a,b=map(int,input().split())
if abs(a-b)==9 or a+1==b or b+1==a:
    print('Yes')
else:
    print('No')