a=int(input())
c=1
while c!=0:
    c=0
    if a%2==0:
        a=a//2
        c=1
    elif a%3==0:
        a=a//3
        c=1
    elif a%5==0:
        a=a//5
        c=1
if a==1:
    print('Ugly Number')
else:
    print('Not Ugly Number')
    