a,b,c=map(int,input().split())
if a==b and b==c and c==a:
    print("Equilateral triangle")
elif a==b or b==c or c==a:
    print("Isosceles triangle")
else:
    print("Scalene triangle")