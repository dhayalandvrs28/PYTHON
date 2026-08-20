employee={}
n=int(input("enter the number opf employee :"))
for i in range(n):
   name=input("NAME :")
   sal=int(input("enter the salary :"))
   employee[name]=sal
for name,sal in employee.items():
   if sal>50000:
      print(name)
