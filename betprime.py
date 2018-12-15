a=int(input("Input:"))
b=int(input("Input:"))
for i in range(a,b-1):
   a=a+1
   for j in range(2,a):
       if(a%j==0):
           break
   else:
    print(a)
    

