def divide():
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        res = a/b
        print("The result of a/b is",res,end='\n')
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please enter a non-zero number for the second number.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

def list_access():
    l = list(eval(input("enter the list of numbers( eg : 1,2,3,4,5,6 )")))
    try:
        i = int(input("Enter an index to access : "))
        print("The element at index ",i," is: ",l[i])
    except IndexError:
        print("Error: Index out of range. Please enter a valid index.")
    except ValueError:
        print("Error: Invalid input. Please enter an integer value.")

def dict_access():
    d = dict(eval(input("enter a dictionary of keys-values : ")))
    try:
        k = input("Enter a key to access : ")
        print("The value for ",k,"is:",d[k])
    except KeyError:
        print(f"Error: Key ",k," not found in the dictionary.")
    except TypeError:
        print("Error: Invalid input type. Please enter a string key.")
while True:
    print("\nException Handling Demonstration")
    print("1. Divide Numbers")
    print("2. Access List Element")
    print("3. Access Dictionary Value")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        divide()
    elif choice == '2':
        list_access()
    elif choice == '3':
        dict_access()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
