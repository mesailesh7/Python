# # learn about Object Oriented Programming by answering these questions
#
#
# <details>
# <summary>
# 1. Basic Class and Object
# </summary>
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.
# </details>
#
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.__model = model
#
#
# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
#
# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)
#
#
# <details>
# <summary>
# 2. Class Method and Self
# </summary>
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).
# </details>
#


class Cars:

    total_car = 0

    def __init__(self, brand, model):
        # Before encapsulation
        # self.brand = brand

        # After encapsulation
        # if after variable if you insert __ it will make the variable private and can only be accessed inside the class
        self.__brand = brand
        self.__model = model
        Cars.total_car += 1

    # Encapsulation
    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    # it will create a static method from which method can only accessed by the class but can't be accessed by the instances
    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model


# my_car = Cars("Toyota", "Corolla")
# print(my_car.full_name())


#
# <details>
# <summary>
# 3. Inheritance
# </summary>
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
# </details>


class ElectricCar(Cars):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


my_tesla = ElectricCar("Tesla", "Model S", "85Kwh")
print(my_tesla.full_name())
# print(my_tesla.get_brand())
print(my_tesla.get_brand())
print(my_tesla.fuel_type())
print(isinstance(my_tesla, Cars))
print(isinstance(my_tesla, ElectricCar))


# Created another instance of Cars
safari = Cars("Tata", "Safari")
print(safari.fuel_type())


my_car = Cars("Nissan", "Versa")
print(my_car.general_description())


print(Cars.total_car)


class Battery:
    def battery_info(self):
        return "this is a battery"


class Engine:
    def engine_info(self):
        return "this is a engine"


class ElectricCarTwo(Battery, Engine, Cars):
    pass


my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())

#
#
#
# <details>
# <summary>
# 4. Encapsulation
# </summary>
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
# </details>
#


# <details>
# <summary>
# 5. Polymorphism
# </summary>
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
# </details>


# <details>
# <summary>
# 6. Class Variables
# </summary>
# Problem: Add a class variable to Car that keeps track of the number of cars created.
# </details>


#
#
#
#
# <details>
# <summary>
# 7. Static Method
# </summary>
# Problem: Add a static method to the Car class that returns a general description of a car.
# </details>
#


#
# <details>
# <summary>
# 8. Property Decorators
# </summary>
# Problem: Use a property decorator in the Car class to make the model attribute read-only.
# </details>
#
#


#
# <details>
# <summary>
# 9. Class Inheritance and isinstance() Function
# </summary>
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.
# </details>
#
#
#
# <details>
# <summary>
# 10. Multiple Inheritance
# </summary>
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
# </details>
#
