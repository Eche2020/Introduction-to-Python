# Write a Python program that checks if a number entered by the user is either divisible by 3 or divisible by 5, and prints the appropriate message.

number = int(input("input is your number: "))

if number % 3 == 0 or number % 5 == 0:
    print("this number is divisible by 3 or divisible by 5")
else:
    print("this number is not divisible by 3 or divisible by 5")