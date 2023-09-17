def prime(a):
    if a==1:
        return 1
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 0
    else:
        return 1
a=int(input())
if prime(a):
    print('prime')
else:
    print('not a prime')