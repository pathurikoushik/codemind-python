def sum_d(l):
    b=str(l)
    s=0
    for i in b:
        s+=int(i)
    return s
l=int(input())
while 1:
    l=sum_d(l)
    if l<10:
        print(l)
        break