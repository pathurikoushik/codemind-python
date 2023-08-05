k1,k2=input().split()
a,b=int(k1),int(k2)
if abs(a-b)==9 or a==b+1 or a+1==b:
    print('Yes')
else:
    print('No')