my_list = []
while True:
   print("1. Append Elements to a list")
   print("2. Insert an Element at a specified index")
   print("3. Remove an Element from the list")
   print("4. Pop an element")
   print("5. Sort the List")
   print("6. Reverse the list")
   print("7. Find the Specified Element")
   print("8. Display the List Elements")
   print("9. Exit")
   choice = int(input("Enter a Choice : "))

   if choice == 1:
      ele = input("Enter Element : ")
      my_list.append(ele)
      print("Element Appended Successfully!!")
   elif choice == 2:
      index = int(input("Enter Index : "))
      ele = input("Enter Element : ")
      my_list.append(index,ele)
      print("Element Inserted Successfully!!")
   elif choice == 3:
      ele = input("Enter an Element : ")
      if ele in my_list:
         my_list.remove(ele)
         print("Element Removed Successfully!!")
      else:
         print("Element Not Found!")
   elif choice == 4:
      print("Element Popped Successfully!")
      print("Popped Element :", my_list.pop())
   elif choice == 5:
      my_list.sort()
      print("Sorted List :", my_list)
   elif choice == 6:
      my_list.reverse()
      print("Reversed List :", my_list)
   elif choice == 7:
      ele = input("Enter Element : ")
      if ele in my_list:
         l = my_list.index(ele)
         print(f"Element Found At {l}")
      else:
         print("Element Not Found")
   elif choice == 8:
      print("List :",my_list)
   elif choice == 9:
      break
   else:
      print("Invalid Choice! Enter Between 1 - 8.")

