#Exercise 1

# Variables, Strings, Ints and Print Exercise

# Given two variables - name and age.
# Use the format() function to create a sentence that reads:
# "Hi my name is Julie and I am 42 years old"
# Set that equal to the variable called sentence

name = "Julie"
age = "42"
sentence = "Hi my name is {} and I am {} years old.".format(name,age)
print(sentence)

#Exercise 2

# If Statements and Comments Exercise

# Make an if-else statement if year is between 2000 and 2100
# (including both numbers), then print out:
# "Welcome to the 21st century"
# Else print out:
# "You are before or after the 21st century"

year = 1830
if year >= 2000 and year <= 2100:
    print("Welcome to the 21st century")
else:
    print("You are before or after the 21st century")

#Exercise 3

# Challenge - Functions Exercise

# Create a function named tripleprint that takes a string as a parameter
# and prints that string 3 times in a row.
# So if I passed in the string "hello",
# it would print "hellohellohello"

def tripleprint(str):
     print(str*3)
     
tripleprint("hello")


#Exercise 4
# Challenge - Lists Exercise

# Create a variable named shoes that is a
# list of the following items, in order:
# Spizikes
# Air Force 1
# Curry 2
# Melo 5

shoes = ["Spizikes", "Air Force 1", "Curry 2", "Melo 5"]
print(shoes)

#Exercise 5

# Challenge - Loops Exercise

# Given a list of ints below called numbers.
# Print every number that is greater than 90.

numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52,
    32, 17, 58, 54, 79, 72, 55, 50, 81, 74,
    45, 33, 38, 10, 40, 44, 70, 81, 79, 28,
    83, 41, 14, 16, 27, 38, 20, 84, 24, 50,
    59, 71, 1, 13, 56, 91, 29, 54, 65, 23,
    60, 57, 13, 39, 58, 94, 94, 42, 46, 58,
    59, 29, 69, 60, 83, 9, 83, 5, 64, 70,
    55, 89, 67, 89, 70, 8, 90, 17, 48, 17,
    94, 18, 98, 72, 96, 26, 13, 7, 58, 67,
    38, 48, 43, 98, 65, 8, 74, 44, 92]

for number in numbers:
     if number>90:
        print(number)

#Exercise 6

# Challenge - Dictionaries Exercise
#
# Given two lists - words and definitions,
# Create a dictionary called cooldictionary where you
# use words for keys and definitions for values


words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

cooldictionary = {"PoGo":"Slang for Pokemon Go", "Spange":"To collect spare change, either from couches, passerbys on the street or any numerous other ways and means", "Lie-fie":"When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"}
print(cooldictionary)

#Exercise 7

# Challenge - Classes Exercise

# Add a method to the Car class called age
# that returns how old the car is (2019 - year)

# *Be sure to return the age, not print it

class Car:

    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model

mycar = Car(2019,"Toyota","Toyota Corolla Altis")
print(mycar)
print(mycar.year)

