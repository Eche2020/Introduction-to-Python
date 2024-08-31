# Advanced Level:
# Write a Python program that takes a tuple of strings and returns a 
# new tuple containing only the strings that start with a vowel.
# Consider both uppercase and lowercase vowels.


def filter_string_with_vowel(strings):
    strings_starting_with_vowel = []
    vowels = ('a','e','i','o','u','A','E','I','O','U')

    for x in strings:
        if x[0] in (vowels):
            strings_starting_with_vowel.append(x)
    return tuple(strings_starting_with_vowel)


tuple_of_str = ("apple","mango","kiwi","Banana", "Orange")            
result = filter_string_with_vowel(tuple_of_str)

print("the strings with vowel:", result)
print("The main tuples:", tuple_of_str)
