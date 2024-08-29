# Intermediate Level:
# Write a Python program that takes a tuple of numbers and returns a new tuple with each element squared.

def squard_tuple_number(number) :

    # using list comprehension to multiply the list by 2 and the casting it using tuple()
    new_tuple = tuple(x**2 for x in number)
    return new_tuple

numbers =  (1,2,3,4,5,6,10)   
new_numbers = squard_tuple_number(numbers)
print(numbers)
print(new_numbers)



# using the append method to also solve the code
numbers = (1,2,3,4,5,10)
new_numbers = []

for x in numbers :
    new_numbers.append(x ** 2)

new_numbers = tuple(new_numbers)

print(numbers)
print(new_numbers)
