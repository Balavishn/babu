a= int(input("input:"))
b= int(input("input:"))

for i in range(a, b + 1):
   o = len(str(i))
   s = 0
   t = i
   while t > 0:
       d = t % 10
       s += d ** o
       t //= 10

   if i == s:
       print(i)
