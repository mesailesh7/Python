# value = 13
# remainder = value % 5
#
# if remainder:
#     print(f"Not divisible, remainder is {remainder}")


# value = 13
#
# if(remainder := value % 5):
#     print(f"Not divisible by {remainder}")


# available_sizes = ["small", "medium", "large"]
#
# if(requsted_size := input("Enter your chai cup size")) in available_sizes:
#     print(f"{requsted_size} is available")
# else:
#     print("Not available")

flavours = ["masala", "ginger", "lemon", "mint"]

print("Available Flavors: ", flavours)

while (flavour:= input("Which flavour do you wish to use?")) not in flavours:
    print(f"{flavour} is not available. Sorry")

print(f"you choose {flavour} chai.")