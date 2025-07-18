chai = [1,2,3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)


def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)

make_chai("Darjeeling", "Yes", "Low")#positional
make_chai(tea="Green", sugar="Little", milk="Yes") #keywords



def special_chai(*ingredients, **extras):
    print("ingredients", ingredients)
    print("extras", extras)

special_chai("Cinnamon", "Cardamom", sweetner="Honey", foam="yes")

def chai_order(order=[]):
    order.append("Masala")
    print(order)

chai_order()