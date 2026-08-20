x=int(input("enter the number of student :"))
d={}
for i in range(x):
   n=input("enter the name :")
   m=input("enter the marks :")
   d[n]=m
while True:
   n=input("enter the name to find marks :")
   m=d.get(n,-1)
   if m==1:
      print("not found ")
   else :
      print(n,"===>",m)
   opt=input("do you want to find any other ?[yes/no]")
   if opt=="no":
      break
   print("thankyou")
