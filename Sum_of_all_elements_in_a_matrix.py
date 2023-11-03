r,c=map(int,input().split())
mat=[]
for i in range(r):
    inner_list=list(map(int,input().split()))[:c:]
    mat.append(inner_list)
s=0
for inner_list in mat:
    for every_value in inner_list:
        s=s+every_value
print(s)
