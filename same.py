a=int(input())
l=[]
b=[]
k=0
for i in range(0,a):
    l.append(list(input()))

for j in range(0,min(len(l[0]),len(l[1]))):
    if l[0][j]==l[1][j]:
        b.append(l[0][j])
def min(a,b):
     if(a>b):
       k=b
     else:
       k=a
     return k


for i in range(1,a):
    for j in range(0,min(len(b),len(l[i]))):
        if b[j]!=l[i][j]:
            b.remove(b[j])

for i in range(0,len(b)):
    print(b[i])

