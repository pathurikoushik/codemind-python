a=input()
b=int(a)**2
c=a[::-1]
d=int(c)**2
e=str(d)[::-1]
if str(b)==e:
    print(True)
else:
    print(False)