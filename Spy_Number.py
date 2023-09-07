a=int(input())
s=0
p=1
while a!=0:
    b=a%10
    a=a//10
    s+=b
    p*=b
if(p==s):
    print('Spy Number')
else:
    print('Not Spy Number')