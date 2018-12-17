a=int(input("input:"))
b=a
r=0
while(a):
     remainder = a%10
     r += remainder*remainder*remainder
     a //= 10
if(r==b):
    print("yes")
else: print("No")
