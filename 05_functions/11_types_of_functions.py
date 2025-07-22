def pure_chai(cups):
    return cups * 10

total_chai = 0

#not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups

# Recursive functions
def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n - 1)

print(pour_chai(5))


#lambda functions
chai_types = ["Light", "Kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda c: c != "Kadak", chai_types))

print(strong_chai)