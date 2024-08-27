total_num = 0

while True:
    # ask the user to enter a number
    number_input = float(input("Enter a random number(a negative number to stop): "))

    # check if the number is negative
    if number_input < 0:
        break

        # add the number to the total sum
    total_num += number_input

print("the sum of total numbers entered is:", int(total_num))