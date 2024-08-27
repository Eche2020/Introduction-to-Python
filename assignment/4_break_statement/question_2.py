# Write a Python program that uses a while loop to print numbers from 1 to 10. Use a break statement to stop the loop when the number 7 is reached.


number = 1

# the while loop to print from 1 to 10
while number < 10: 
    print(number)
    if (number == 7):  #if the loop has gotten to 7 it breaks
        break
    number += 1


