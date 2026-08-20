d={}
while True:
   print("1.add")
   print("2.delete")
   print("3.search")
   print("4.dislay")
   print("5.clear")
   print("6.popitem")
   print("7.key")
   print("8.value")
   print("9.length")
   print("10.exit")
   choice=int(input("choice :"))
   if choice==1:
      key=input("enter key :")
      value=input("value")
      d[key]=value
      print("added")
   elif choice==2:
      key=input("key to delete :")
      if key in d:
         del d[key]
         print("deleted")
      else:
         print("key not found")
   elif choice==3:
      key=input("search key:")
      if key in d:
         print(f"key found:{key}->d{[key]}")
      else :
         print("key not found")
   elif choice==4:
      for key,value in d.items():
         print(key,"-",value)
   elif c hoice==5:
      d.clear()
      print("cleard all ele")
      print(d)
   elif choice==6:
      print(d.popitem())
      print(d)
   elif choice==7:
      key=int(input("enter the key to find :"))
      print(d.get(key))
   elif choice==8:
      for i in d.values():
         print(i)
   elif choice==9:
      print("total length",len(d))
   elif choice==10:
      print("exiting")
      break
   else:
      print("invalid")
