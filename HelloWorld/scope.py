# username = "chaiaurcode"
#
#
# def func():
#     # username = "chai"
#     print(username)
#
#
# print(username)
# func()
#
#


# x = 99
#
#
# def func2(y):
#     z = x + y
#     return z
#
#
# result = func2(1)
# print(result)


# eg 2******
# x = 99
#
#
# def func3():
#     global x
#     x = 88
#
#
# func3()
# print(x)


# *****question 3

# x = 99
#
#
# def f1():
#     x = 88
#
#     def f2():
#         print(x)
#
#     return f2()
#
#
# myResult = f1()


# ************question4


# factory function or closeures
def chaiCoder(num):
    def actual(x):
        return x**num

    return actual


f = chaiCoder(2)
g = chaiCoder(3)

print(f(3))
print(g(3))
