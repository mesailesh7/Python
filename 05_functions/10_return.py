# def make_chai():
#     # return "Here is your masala chai"
#     print("Here is your masala chai")
# return_value = make_chai()
#
#
# print(return_value)


def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"





print(chai_status(0))


def chai_report():
    return 100,20

sold , remaining = chai_report()

print(sold)
print(remaining)