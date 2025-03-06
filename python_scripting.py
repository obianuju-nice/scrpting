# Pre-requisite: 
# download python from (https://www.python.org/downloads/) & install python extension on visual studio code extension

1. #  single line comment and multiple line comments

# 2. Variables (Local and Global variable ): variables are used to store data that can be referenced and manipulated during program execution. A variable is essentially a name that is assigned to a value
# Variable names can only contain letters, digits and underscores and cannot start with a digit and is also case-sensitive (myVar and myvar are different).
#.EX:
# age = 30
# color= "blue"
# total_score = 60
# print(age, color, total_score)

# 3.  Input (user input) & Output​
# Python input() function is used to take user input. By default, it returns the user input in form of a string while output function  function allows us to display text, variables and expressions on the console.

# first_name = input(" What is your first_name: ")    # Input() function
# print("My first name is " + first_name)            #  output() function

# 4. Operators: 
# +	Addition	a + b = 30
# -	Subtraction	a – b = -10
# *	Multiplication	a * b = 200
# /	Division	b / a = 2
# ex: a = 20
# b = 10
# c = a + b
# print (c)

# Comparison operator
# ==	Equal to	(a == b)
# !=	Not equal to	(a != b)
# >	Greater than	(a > b)
# <	Less than	(a < b)
# >=	Greater than or equal to	(a >= b)
# <=	Less than or equal to	(a <= b)

# Logical Operators
# and	Returns True if both conditions are true	(x and y)
# or	Returns True if at least one condition is true	(x or y)
# not	Reverses the condition	not x

# 4. Data types: Specifies the type of data a variable can hold and also specifies the type of values (integers, floats, characters the operations that can be performed on them.
# This value is represented by int class. It contains positive or negative whole numbers (without fractions or decimals)there is no limit to how long an integer value can be.
# ex: number = 50
# Float: =  This value is represented by the float class. It is a real number with a floating-point representation. It is specified by a decimal point. ex: float = 10.0
# Complex Numbers: A complex number is represented by a complex class. It is specified as (real part) + (imaginary part)j . For example – 2+3j
# Boolean: = Which is with one of the two built-in values which is either True or False
# # char = 'a'
# boolean = True

# 5. Data Structure: This allows storing of multiple values in an organized and efficient fashion.
# Purpose: Provides a structured format to store multiple data elements and perform operations efficiently.Example:List, Tuples, Dictonaries
# Strings = "string = A string is a sequence of characters and Python treats anything inside quotes as a string.
# name = "My name is Nice"
# print(name)

#  LIst = Lists are just like arrays, declared in other languages which is an ordered collection of data. It is very flexible as the items in a list do not need to be of the same type.
# items =  ["name", "city", "postcode", "color", 10, 15]
# print(items)
# print(items[0])


# my_array = [10, 20, 30, 40]  # Creating an array using a list
# print(my_array[0])  # Accessing elements: Output -> 1
# print(my_array[-1])  # Accessing last element: Output -> 5

# my_array.append(50)  # Adding an element
# print(my_array)

#  Tuples: Just like a list, a tuple is also an ordered collection of Python objects. The only difference between a tuple and a list is that tuples are immutable. Tuples cannot be modified after it is created.
# ex: my_tuples = ("name"."city", "postcode", "color")
# print(my_tuples[0])

# Dictionary holds a key & its value of a data. Key-value is provided in the dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon : , whereas each key is separated by a ‘comma’. ex: 
# dict = {1: 'school', 2: 'Training', 3: 'Modules'}
# dict2 =  {"name":1."age":2, "location":london, "origin":nigerai}
# print(dict)
# print(dict2)
# print(my_dictionary[0])

#  Sets =  Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements and  Cannot access elements using indexing.
# my_set = ("Nickos", "Devops", "Modules")
# print(my_set)

#  Arrays = (["Terraform", "Docker", "kubernetes"])
#  List Comprehension

# 6. Conditional statements in Python are used to execute certain blocks of code based on specific conditions.with (if, elif  and else statement) 
# Checking and executing conditions based on user input
# age = 10
# if age < 0:
#     print("Please enter a valid age.")
# elif age < 18:              #  elif allows to check for multiple conditions
#     print("You are a minor.")
# elif age >= 18 and age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")

# 7. Loops:  Loops in Python are used to repeat actions efficiently. The main types are (for loops) for counting through items and (While loop) to execute a block of statements repeatedly until a given condition is satisfied, 
# (continue statement in loop) is used to return the control to the beginning of the loop and (break statement in loop) brings control out of the loop
# 
# laptops= ['window', 'mac','nevo', 'dell']
# print(laptops)
# for computers in laptops:
#  print(computers)

# while example: 
# count = 1
# while count < 4:
#     print(count)
#     count += 1

# 8.  Python functions: is used to define a function, it is placed before a function name that is provided by the user to create a user-defined function
# def my_function1(z):
#   return 3 * z

# print(my_function1(5))

# 9. Object Oriented Programming (Classes and Objects, Polymorphism,Inheritance, AbstractEncapsulation, Iterators)

# GLOBaL VARIABLES intRE DECLintRED OUTSIDE int FUNCTION





