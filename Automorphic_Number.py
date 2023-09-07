num = int(input())
sqr = num**2
n = len(str(num))
last = sqr%pow(10,n)
if last == num:
   print("Automorphic Number")
else:
   print("Not an Automorphic Number")