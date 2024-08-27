# Intermediate Level:
# Write a Python program that takes a list of numbers and returns a new list with only the even numbers from the original list.

def get_even_num(number):
    # use list comprehension to filter through the list
    even_numbers = [num for num in number if num % 2 == 0 ]
    return even_numbers

listItems = [1,2,3,4,5,6,7,8]
evenList = get_even_num(listItems)

print("original List:", listItems)
print("Even number List:", evenList)