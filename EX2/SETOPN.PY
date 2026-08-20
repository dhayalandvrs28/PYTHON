while True:
   print("1.union")
   print("2.intersection")
   print("3.difference")
   print("4.symmetric")
   print("5.exit")
   choice=int(input("enter the choice :"))
   if choice==5:
      break
   ele1=input("enter the element seperated by spaces")
   ele2=input("enter the element sepersted by spaces")
   l1=ele1.split()
   l2=ele2.split()
   setA=set(l1)
   setB=set(l2)
   if choice==1:
      print("union :",setA|setB)
   elif choice==2:
      print("inter section :",setA&setB)
   elif choice==3:
      print("difference :",setA-setB)
   elif choice==4:
      print("sd :",setA^setB)
   else :
      print("invalid input")
