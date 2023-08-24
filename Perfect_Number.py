n=int(input())
ram=0
for i in range(1,n):
    if n%i==0:
        ram+=i
if ram==n:
    print(True)
else:
    print(False)