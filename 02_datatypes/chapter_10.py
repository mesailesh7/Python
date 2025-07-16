chai_order = dict(type="Masala Chai", size="large", sugar=2)
print(f"{chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f" Recipe base{ chai_recipe['base']}")
del chai_recipe["liquid"]


print(f"Recipe: {chai_recipe}")

print(f"Order details (keys) {chai_order.keys()}")
print(f"Order details (keys) {chai_order.values()}")
print(f"Order details (keys) {chai_order.items()}")


chai_size = chai_order["size"]

print(f"chai size is {chai_size}")


# Tasks:

# Create a dictionary named customer with the following fields:

# "name": "John Doe"

# "age": 32

# "city": "New York"
customer = {}
customer["name"] = "John Doe"
customer["age"] = 32
customer["city"] = "New York"


# Print the dictionary.
print(customer)

# Add "email" and "phone" to the dictionary.
customer["email"] = "email.com"
customer["phone"] = 123456

# Print the updated dictionary.
print(customer)
# Print the customer’s "name" and "city" values.
print(f"{customer["name"]} {customer["city"]}")

# Check whether the key "email" exists in the dictionary and print the result.
print(f"{"email" in customer}")


# Delete the "age" field from the dictionary.
del customer["age"]

# Print the updated dictionary.

print(customer)
# Print all dictionary keys, values, and items.
print(f"keys: {customer.keys()}")
print(f"values: {customer.values()}")
print(f"Items: {customer.items()}")
# Remove and print the last inserted key-value pair.
last_item = customer.popitem()
print(f"Last removed item {last_item}")

# Use .get() to access the key "membership" (which doesn’t exist).
customer_membership = customer.get("membership", "No Membership")

# Print the result.
print(f"{customer_membership}")

# Update the dictionary with a new field "address" set to "221B Baker Street".
customer.update({"address": "2218 Baker Street"})


# Print the final dictionary.
print(customer)
