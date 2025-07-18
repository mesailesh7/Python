# # questions on conditionals

# <details>
# <summary>1. Age Group Categorization
# </summary>
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

# Answer ***************
# age = int(input("Please enter your age "))

# if age <= 13:
#     print("Child")
# elif age >= 13 and age <= 19:
#     print("Teenager")
# elif age >= 20 and age <= 59:
#     print("Adult")
# elif age >= 60:
#     print("senior")
# else:
#     print("Please enter a valid number")


# </details>

# <details>
# <summary>2. Movie Ticket Pricing
# </summary>
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

# </details>


# ***Answer
# age = int(input("What is your age"))
# day = input("What day is today").lower()
#
#
# if day == "wednesday":
#     if age >= 18:
#         ticketPrice = 10
#         print(ticketPrice)
#     else:
#         ticketPrice = 6
#         print(ticketPrice)
# else:
#     if age >= 18:
#         ticketPrice = 12
#         print(ticketPrice)
#     else:
#         ticketPrice = 8
#         print(ticketPrice)


# <details>
# <summary>3. Grade Calculator
# </summary>
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).


# score = int(input("Enter your score: "))
# def student_score(score):
#     match score:
#         case score if score >= 90 and score <= 100:
#             return print("Student received grade A")
#         case score if score <= 89 and score >= 80:
#             return print("Student received grade B")
#         case score if score <= 79 and score >= 70:
#             return print("Student received grade C")
#         case score if score <= 69 and score >= 60:
#             return print("Student received grade D")
#         case score if score <= 60:
#             return print("Student received grade F")
#         case _:
#             return print("Please enter a number")


# student_score("55")


# </details>

# <details>
# <summary>4. Fruit Ripeness Checker
# </summary>
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
#
# </details>

# fruit_color = input("What color is the fruit").lower()

# if fruit_color == "green":
#     print("Unripe")
# elif fruit_color == "yellow":
#     print("Ripe")
# elif fruit_color == "brown":
#     print("Overripe")
# else:
#     print("Please enter a valid color")


# <details>
# <summary>5. Weather Activity Suggestion
# </summary>
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

# </details>

# <details>
# <summary>6. Transportation Mode Selection
# </summary>
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

# </details>


# <details>
# <summary>7. Coffee Customization
# </summary>
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

# </details>


# <details>
# <summary>8. Password Strength Checker
# </summary>
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

# </details>


# <details>
# <summary>9. Leap Year Checker
# </summary>
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

# </details>
# year = int(input("Enter a year: "))
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("YES its a leap year")
# else:
#     print("NO, its not a leap year")

# <details>
# <summary>10. Pet Food Recommendation
# </summary>
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

# </details>

pet = input("What is your pet's type?").lower()
age = int(input(f"What is your {pet} age?"))

if pet == "dog" and age < 2:
    print("Puppy food")
elif pet == "cat" and age > 5:
    print("Senior cat food")
else:
    print("You are not cat or dog")
