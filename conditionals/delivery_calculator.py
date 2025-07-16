distance = int(input("Please enter the delivery distance"))

if distance <= 2:
    print("No delivery charge")
elif distance > 2 and distance <= 5:
    print("Delivery charge: 30")
elif distance > 5 and distance <= 10:
    print("Delivery charge: 50")
elif distance > 10:
    print("Delivery not availabel for your location")
else:
    print("please enter a valid distance")


def calculate_delivery_charge(distance: float) -> str:
    # Write your code below this line
    if distance <= 2:
        return "Delivery charge: 0"
    elif distance <= 5:
        return "Delivery charge: 30"
    elif distance <= 10:
        return "Delivery charge: 50"
    else:
        return "Delivery not available for your location."
    pass
