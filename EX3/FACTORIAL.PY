num=int(input("Enter number: "))
def fact(num):
   r=1
   while num>=1:
      r=r*num
      num=num-1
   return r
for i in range(1,num+1):
   print("Factorial",i,":",fact(i))
