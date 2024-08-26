fruits = ["apples", "oranges", "mangos", "cherry", "kiwi"]
newlist = []
# newlist = [x for x in fruits if "a" in x]

# print(newlist)

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)