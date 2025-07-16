seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()


match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds are available")
    case "ac":
        print("AC - air conditioned, comfy ride")
    case "general":
        print("General ward")
    case "luxury":
        print("luxury")
    case _:
        print("Invalid seat type")
