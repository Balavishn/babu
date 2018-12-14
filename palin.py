n=int(input("input"))
a=n
c=0
while(n):
    d=n%10;
    c=(c*10)+(d%10)
    n //=10
if(a==c):
    print("yes")
else:
    print("not")
