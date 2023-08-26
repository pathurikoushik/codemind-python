p=int(input())
c=0
for i in range(1,p+1):
    if p%i==0:
        c=c+1
if c==2:
    print('Prime')
else:
    print('Not Prime')