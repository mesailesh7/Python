def chai_flavour(flavour="masala"):
    """
    :param flavour:
    :return: return the flavour of chai
    """

    return flavour


print(chai_flavour.__doc__)
print(chai_flavour.__name__)


def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa
    :param chai: Number of chai cups
    :param samosa: Number of samosa
    :return:(total amount, thank you message)
    """
    total = chai * 10 + samosa * 15
    return total, "Thank you"


print(generate_bill())
