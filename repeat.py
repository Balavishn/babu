a= int(input("input:"))
l=[]
b=[]
for i in range(1,a+1):
    l.append(int(input()))
for i in range(0,a+1):
    for j in range(i+1,a):
        if l[i]==l[j]:
            b.append(l[i])
b.sort()
print(b)
        
