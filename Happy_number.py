a=int(input())
while a>9:
    t=a
    a=0
    while t!=0:
        k=t%10
        t=t//10
        a=a+k*k
if a==1 or a==7:
    print('True')
else:
    print('False')