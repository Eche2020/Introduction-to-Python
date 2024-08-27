

Nigeria = ("lagos", "abuja", "ibadan", "ogun", "oyo")

print (Nigeria)

# to determine the turple length

print (len(Nigeria))

# check a tuple type
print(type(Nigeria))

# add a tuple
Nigeria = ("lagos", "abuja", "ibadan", "ogun", "oyo")
y = list(Nigeria)
y.append("gee")
Nigeria = tuple(y)

# remove from a tuple
Nigeria = ("lagos", "abuja", "ibadan", "ogun", "oyo")
y = list(Nigeria)
y.remove("abuja")
Nigeria = tuple(y)

# unpacking a tuple
Nigeria = ("lagos", "abuja", "ibadan", "ogun", "oyo")
(white, blue, green, yellow, black) = Nigeria
print(white)
print(blue)
print(green)
print(yellow)
print(black)

# using asterisk
Nigeria = ("lagos", "abuja", "ibadan", "ogun", "oyo")
(white, *blue, green) = Nigeria
print(white)
print(blue)
print(green)

# loop in a tuple
Nigeria = ("lagos", "abuja", "ibadan", "ogun", "oyo")
for x in Nigeria:
    print(x)


# join two turple
Nigeria1 = ("a", "b", "c")
Nigeria2 = (1, 2, 3)
Nigeria3 = Nigeria1+Nigeria2
print(Nigeria3)


# multiply tuple
state = ("lagos", "ibadan", "ogun")
Nigeria *2


print(Nigeria)