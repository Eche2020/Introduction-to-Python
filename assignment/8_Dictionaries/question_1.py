# Beginner Level:
# Create a Python dictionary with keys as the names of three countries and values as their 
# capitals. Print the capital of the second country.


countries = {
    "Nigeria" : "abuja",
    "india" : "bangladesh",
    "nairobi" : "kenya"
}

# get the list of key and find the capital of second country
second_country = list(countries.keys())[1]
capital_of_second_country = countries[second_country]

print("The capital of", second_country, "is:", capital_of_second_country )