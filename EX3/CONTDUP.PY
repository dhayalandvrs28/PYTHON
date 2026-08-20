input_string=input("Enter string: ")
def remove_consecutive_duplicates(s):
    result = ""
    for char in s:
        if not result or char != result[-1]:
            result += char
    return result
modified_string = remove_consecutive_duplicates(input_string)
print(modified_string)
