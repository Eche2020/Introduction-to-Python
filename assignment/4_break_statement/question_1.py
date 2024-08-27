# Write a Python program that asks the user to enter numbers. If the user enters a number greater than 100, stop the loop using a break statement and print "Loop stopped.


# using a while loop to iterate through the code 
while True:
    number_input = float(input("enter a number greater than 100: "))

    # if input is greater than 100
    if number_input < 100:
        break

print("Loop Stopped ")