l=int(input())
a=[l]
a=list(map(int,input().split()))
f=0
for i in range(0,l):
    if a[i]%2!=0:
        f=f+1
if f<=2:
    print('YES')
else:
    print('NO')