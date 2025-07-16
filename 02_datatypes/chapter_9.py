essential_spices = {"cardamom", "ginger"}
optional_spices = {"cardamom", "garlic"}

# Union which removes duplicates
all_spices = essential_spices | optional_spices
print(all_spices)


# intersection means which is common
common_spices = essential_spices & optional_spices
print(common_spices)

# checks both and remove
only_in_essential = essential_spices - optional_spices
print(only_in_essential)


# membership test
print(f"Is ginger is in essential {"ginger" in essential_spices} ")
