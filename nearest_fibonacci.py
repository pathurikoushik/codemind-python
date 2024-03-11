a=int(input())
f=0
s=1
while f<a:
    t=f
    f=s
    s=t+s
if(a-t)==(f-a):
    print(t,f)
elif (a-t)>(f-a):
    print(f)
else:
    print(t)