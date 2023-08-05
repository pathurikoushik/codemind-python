a=int(input())
s=0
p=1
temp=0
while(a):
    temp=a%10
    p=p*temp
    s=s+temp
    a//=10
if(s==p):
    print("Spy Number")
else:
    print("Not Spy Number")