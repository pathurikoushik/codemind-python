n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
s=[]
for i in a:
    if i<b or i>c:
        s.append(i)
if len(s)==0:
    print('-1')
else:
    print(*s)