# # Loops in Python
#
# <details>
# <summary>
# 1. Counting Positive Numbers
# </summary>
# Problem: Given a list of numbers, count how many are positive.
#
# ```python
from nbformat.sign import trust_flags
from sqlalchemy import false

# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# counter = 0
# # ```
# for number in numbers:
#     if number > 0:
#         counter += 1
#
# print(counter)


# </details>
#
#
# <details>
# <summary>
# 2. Sum of Even Numbers
# </summary>
# Problem: Calculate the sum of even numbers up to a given number n.
#
# </details>

# **********
# number = int(input("Enter a number: "))
# count = 0
#
# for x in range(1, number + 1):
#     if x % 2 == 0:
#         count += x
#         print(x)
#
# print(count)


#
# <details>
# <summary>
# 3. Multiplication Table Printer
# </summary>
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
#
# </details>
#

# number = int(input("Enter a number: "))
# math_count = 0
#
# for x in range(1, 11):
#     if x != 5:
#         math_count = number * x
#         print(math_count)


#
# <details>
# <summary>
# 4. Reverse a String
# </summary>
# Problem: Reverse a string using a loop.
#
# </details>
# text = input("Enter a sentence: ")
# reversed_string = ""
#
# for char in text:
#     reversed_string = char + reversed_string
#     print(reversed_string)
#
# print(reversed_string)

#
#
# <details>
# <summary>
# 5. Find the First Non-Repeated Character
# </summary>
# Problem: Given a string, find the first non-repeated character.
#
# </details>
# user_input = input("Enter a name: ").lower()
#
# duplicated_input = ""
#
# for letter in user_input:
#     if user_input.count(letter) > 1:
#         duplicated_input += letter
#         print(duplicated_input)
#
# print(duplicated_input)


#
#
# <details>
# <summary>
# 6. Factorial Calculator
# </summary>
# Problem: Compute the factorial of a number using a while loop.
#
# </details>
# user_input = int(input("Enter a number: "))
# factorial = 1
#
# for i in range(1, user_input + 1):
#     factorial = factorial * i
#     print(factorial)
#
# print(factorial)
#
# Anotherway of doing
# number = int(input("Enter a number: "))
# factorial = 1
#
# while number > 0:
#     factorial = factorial * number
#     number = number - 1
#
# print(factorial)

# <details>
# <summary>
# 7. Validate Input
# </summary>
# Problem: Keep asking the user for input until they enter a number between 1 and 10.
#

#
# while True:
#     number = int(input("Enter a number between 1 and 10: "))
#     if 1 <= number <= 10:
#         print("Thanks")
#         break
#     else:
#         print("invalid input try again")

# </details>
#
#
# <details>
# <summary>
# 8. Prime Number Checker
# </summary>
# Problem: Check if a number is prime.
#
# </details>
#
#
#
# num = int(input("Enter a number "))
#
# is_prime = false
#
# if num == 0 or num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             is_prime = True
#             break
#
#     if is_prime:
#         print(num, "is a prime number")
#     else:
#         print(num, "is not a prime number")
#

# <details>
# <summary>
# 9. List Uniqueness Checker
# </summary>
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
#
# ```python
# items = ["apple", "banana", "orange", "mango", "mango", "apple"]
# # ```
# unique_items = set(items)
#
# for item in items:
#     if item in unique_items:
#         print("Duplicate item:", item)
#         break
#     unique_items.add(item)
#
#
# print(unique_items)
# </details>
#
#
# <details>
# <summary>
# 10. Exponential Backoff
# </summary>
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.
# </details>
# import time
#
# wait_time = 1
# max_retries = 5
# attempts = 0
#
#
# while attempts < max_retries:
#     print(attempts + 1, "wait time", wait_time)
#     time.sleep(wait_time)
#     wait_time *= 2
#     attempts += 1


import time

print("Chai is here")

user = "hitesh"
print(user)
