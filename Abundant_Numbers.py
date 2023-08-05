k=int(input())
s=0
for i in range(1,(k//2)+1):
    if k%i==0:
        s=s+i
if s>k:
    print('True')
else:
    print('False')