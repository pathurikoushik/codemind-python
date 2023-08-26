a=int(input())
b=a*a
s=0
while b!=0:
    c=b%10
    b=b//10
    s+=c
if(s==a):
    print('Neon Number')
else:
    print('Not Neon Number')