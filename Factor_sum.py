def fact(a):
    s=0
    for i in range(1,a//2+1):
        if a%i==0:
            s+=i
    return s+a
a=input()
a=a.split(',')
b=[]
for i in a:
    d=int(i)
    if d not in b:
        b.append(d)
c=0
b.sort()
for i in b:
    if fact(i) in b:
        print(i,end=' ')
        c=1
if c==0:
    print('-1')