n=input("Enter digit: ")
def sum_of_digits(n):
   return sum(int(digit) for digit in str(n))
result = sum_of_digits(n)
print(f"The sum of the digits of {n} is: {result}")
