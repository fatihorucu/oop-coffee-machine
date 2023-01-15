from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
customer_answer = input(f"What would you like?({menu.get_items()})")
while customer_answer != "off":
    if customer_answer == "report":
        coffee_maker.report()
        money_machine.report()
    elif customer_answer == "espresso":
        if coffee_maker.is_resource_sufficient(menu.find_drink(customer_answer)):
            money_machine.make_payment(float(menu.find_drink(customer_answer).cost))
            coffee_maker.make_coffee(menu.find_drink(customer_answer))

    elif customer_answer == "latte":
        if coffee_maker.is_resource_sufficient(menu.find_drink(customer_answer)):
            money_machine.make_payment(float(menu.find_drink(customer_answer).cost))
            coffee_maker.make_coffee(menu.find_drink(customer_answer))
    elif customer_answer == "cappucino":
        if coffee_maker.is_resource_sufficient(menu.find_drink(customer_answer)):
            money_machine.make_payment(float(menu.find_drink(customer_answer).cost))
            coffee_maker.make_coffee(menu.find_drink(customer_answer))
    customer_answer = input(f"What would you like?({menu.get_items()})")
print("Machine is off.")
