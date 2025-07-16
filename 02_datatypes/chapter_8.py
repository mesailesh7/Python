ingredients = ["water", "milk", "black tea"]


ingredients.append("sugar")

print(f"{ingredients}")


ingredients.remove("water")
print(ingredients)


spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]


chai_ingredients.extend(spice_options)
print(chai_ingredients)
chai_ingredients.insert(2, "Black tea")
print(chai_ingredients)


last_added = chai_ingredients.pop()
print(last_added)

chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")

chai_ingredients.sort()


base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(full_liquid_mix)


# Shopping List
# Instructions
# You’re building a shopping list feature in a grocery app. You need to support various list operations such as adding items, removing them, merging with others, and handling user inputs from text.

# Tasks:

# Create a grocery list named my_cart with the items: "apples", "bananas", and "milk"
my_cart = ["apples", "bananas", "milk"]


# Print the grocery list.
print(my_cart)

# Add "bread" to the end of the list.
my_cart.append("bread")


# Print the updated grocery list.
print(my_cart)
# Insert "ketchup" at the beginning of the list.
my_cart.insert(0, "ketchup")
# Print the updated grocery list.
print(my_cart)

# Remove "bananas" from the list.
# my_cart.pop(2)
my_cart.remove("bananas")
# Print the updated grocery list.
print(my_cart)

# Remove the last item from the list and store it in a variable named removed_item.
removed_item = my_cart.pop()
# Print the value of removed_item.
removed_item
# Extend the grocery list by adding "rice" and "butter".
new_items = ["rice", "butter"]
my_cart.extend(new_items)
# Print the updated grocery list.
print(my_cart)

# Sort the grocery list in alphabetical order.
my_cart.sort()
# Print the updated grocery list.
print(my_cart)

# Reverse the order of the grocery list.
my_cart.reverse()
# Print the updated grocery list.
print(my_cart)

# Concatenate the grocery list with another list containing "juice" and "jam".
new_list = ["juice", "jam"]
my_cart = my_cart + new_list
# Print the resulting list.
print(my_cart)

# Duplicate the grocery list twice.
my_cart = my_cart * 3
# Print the resulting list.
print(my_cart)

# Define a string with the value "tomato cucumber spinach" and convert it into a list.
veggie = "tomato cucumber spinach"
list = veggie.split()
# Print the converted list.
print(list)
