a,b=map(int,input().split())
c=max(a,b)
i=1
while 1:
    if (c*i)%a==0 and (c*i)%b==0:
        print(c*i)
        break
    i+=1