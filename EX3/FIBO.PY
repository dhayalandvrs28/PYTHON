def fibonacci(n):
    if n <= 0:
        return "Invalid input! Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        return b
position = int(input("Enter the position of the Fibonacci number you want to find: "))
result = fibonacci(position)
print(f"The Fibonacci number at position {position} is: {result}")
