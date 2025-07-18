# # learn about decorators
#
#
# <details>
# <summary>
# Problem 1: Timing Function Execution
# </summary>
# Problem: Write a decorator that measures the time a function takes to execute.
# </details>
#
# import time
#
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in {end-start} time")
#         return result
#
#     return wrapper
#
#
# @timer
# def example_function(n: object) -> object:
#     time.sleep(n)
#
#
# example_function(5)


#
# <details>
# <summary>
# Problem 2: Debugging Function Calls
# </summary>
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.
# </details>
#
#

#
# def debug(func):
#     def wrapper(*args, **kwargs):
#         args_value = ", ".join(str(arg) for arg in args)
#         kwargs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items())
#         print(
#             f"calling: {func.__name__} with args value({args_value}, kwargs value {kwargs_value})"
#         )
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @debug
# def hello():
#     print("hello")
#
#
# @debug
# def greet(name: object, greeting: object = "Hello") -> object:
#     print(f"Hello {greeting} {name}")
#
#
# hello()
# greet("chai", greeting="launus")


# <details>
# <summary>
# Problem 3: Cache Return Values
# </summary>
# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
# </details>
#

#
# import time
#
#
# def cache(func):
#     cache_value = {}
#     print(cache_value)
#
#     def wrapper(*args):
#         if args in cache_value:
#             return cache_value[args]
#         result = func(*args)
#         cache_value[args] = result
#         return result
#
#     return wrapper
#
#
# @cache
# def long_running_function(a, b):
#     time.sleep(4)
#     return a + b
#
#
# print(long_running_function(1, 2))
# print(long_running_function(2, 3))
# print(long_running_function(4, 3))
