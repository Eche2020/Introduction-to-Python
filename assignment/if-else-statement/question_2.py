# Write a Python program that checks if a number entered by the user is positive, negative, or zero, and prints the appropriate message.

input_number = float(input("enter a number: "))

if input_number > 0:
    print("your number is positive")
elif input_number < 0:
    print("your number is negative")
else:
    print("your number is zero")
