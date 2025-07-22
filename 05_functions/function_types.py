def pure_add(a,b):
    return a+b

counter = 0
def impure_increment():
    global counter
    counter += 1


def factorial_recursive(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)


def square_list(nums: list[int]):
    square = list(map(lambda x: x ** 2, nums))
    return square

print(square_list([2,4,8,10,12,13,14,15]))