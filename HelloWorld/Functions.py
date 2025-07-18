# # Learn all about functions by answering the questions below.
#
#
# <details>
# <summary>
# 1. Basic Function Syntax
# </summary>
# Problem: Write a function to calculate and return the square of a number.
# </details>
#
# def calculate_square(number):
#     return number**2
#
#
# print(calculate_square(5))
import math

#
# <details>
# <summary>
# 2. Function with Multiple Parameters
# </summary>
# Problem: Create a function that takes two numbers as parameters and returns their sum.
# </details>
#
#


# def addition_number(one, two):
#     return one + two
#
#
# print(addition_number(1, 2))


# <details>
# <summary>
# 3. Polymorphism in Functions
# </summary>
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.
# </details>
#


# def multiply(one, two):
#     return one * two
#
#
# print(multiply("h", 2))

#
# <details>
# <summary>
# 4. Function Returning Multiple Values
# </summary>
# Problem: Create a function that returns both the area and circumference of a circle given its radius.
# </details>

#
# radius = int(input("Enter the radius of the circle: "))
#
#
# def area_circumference(radius):
#     area = math.pi * radius**2
#     circumference = 2 * math.pi * radius
#
#     print("The area of the circumference is", round(area, 2))
#     print("The circumference is", round(circumference, 2))
#
#
# area_circumference(radius)


#
#
# <details>
# <summary>
# 5. Default Parameter Value
# </summary>
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.
# </details>
#

#
# name = input("Enter your name: ")
#
#
# def greeting(name):
#     if name == "":
#         return print("Hello default name")
#     else:
#         return print("Hello " + name)
#
#
# greeting(name)

#
# <details>
# <summary>
# 6. Lambda Function
# </summary>
# Problem: Create a lambda function to compute the cube of a number.
# </details>
#


# IN lambda function after lambda x(if  you are accepting any parameter) : write function
# cube = lambda x: x**3
# print(cube(5))

# first_name = lambda name: print("hello ", name)
# first_name("sunny")


#
# <details>
# <summary>
# 7. Function with *args
# </summary>
# Problem: Write a function that takes variable number of arguments and returns their sum.
# </details>
#


# def sum_all(*args):
#     print(args)
#     return sum(args)


# print(sum_all(1, 2, 3, 4, 5))


# <details>
# <summary>
# 8. Function with **kwargs
# </summary>
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.
# </details>
#
#
# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# 	*args captures the positional arguments (1, 2, 3) as a tuple.
# 	•	**kwargs captures the keyword arguments {'name': 'John', 'age': 30} as a dictionary.

# <details>
# <summary>
# 9. Generator Function with yield
# </summary>
# Problem: Write a generator function that yields even numbers up to a specified limit.
# </details>
#


# def even_generator(limit):
#     for i in range(2, limit + 1, 2):
#         yield i


# for num in even_generator(10):
#     print(num)


#
# <details>
# <summary>
# 10. Recursive Function
# </summary>
# Problem: Create a recursive function to calculate the factorial of a number.
# </details>


def factorial(limit):
    if limit == 0:
        return 1
    else:
        return limit * factorial(limit - 1)


factorial(5)
