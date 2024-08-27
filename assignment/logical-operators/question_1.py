# Question 1:
# Write a Python program that asks the user to enter a number. If the number is both greater than 10 and even, print "The number is greater than 10 and even." Otherwise, print "The number does not meet both conditions.

number = int(input("Enter a number: "))

if number > 10 and number % 2 == 0:
    print("This number is greater than 10 or even.")
else:
    print ("This number does not meet both conditions")
