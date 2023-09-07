a=int(input())
t=a
r=0
while t!=0:
    b=t%10
    t=t//10
    r=r*10+b
rev=0
c=0
while r!=0:
    b=r%10
    r=r//10
    if b==6 and c==0:
        b=9
        c=1
    rev=rev*10+b
print(rev)