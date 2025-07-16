# Tasks:

# Write a function named multiplication_table that takes a single integer argument number.

# Using a for loop and range(), generate the multiplication table for number from 1 to 10.

# Return a list of strings in the following format:

# "number x i = result"

# (Example: "3 x 4 = 12")


# def multiplication_table(number):
#     for multiplication in range(1, 11):
#         print(f"{number} x {multiplication} = {number * multiplication}")




def multiplication_tables(number):
    result = []
    for i in range(1, 11):
        result.append(f"{number} x {i} = {number * i}")
    return result


print(multiplication_tables(5))


# def multiplication_table(number: int) -> list[str]:
#     result = []
#     for i in range(1, 11):
#         result.append(f"{number} x {i} = {number * i}")
#     return result


# print(multiplication_table(2))
