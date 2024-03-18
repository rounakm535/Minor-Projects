MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 20,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 30,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 50,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource_suff(ingredients):

    for item in ingredients:
        if ingredients[item] >= resources[item] :
            print(f"Sorry there is not enough {item}")
            return False

    return True


def payment_success(amount_received , drink_cost):

    if amount_received >= drink_cost:
        change = amount_received - drink_cost
        print(f"Here is the amount ₹{change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money!")
        return False


def make_coffee(drink_name, ingtedients):

        for item in ingtedients:
            resources[item] -= ingtedients[item]
        print(f"Here is your {drink_name}. :) ")


p_espresso = 20
p_latte = 30
p_cappuccino = 50

is_on = True

while is_on:

    print(f"The price for espresso is ₹{p_espresso}")
    print(f"The price for latte is ₹{p_latte}")
    print(f"The price for cappuccino is ₹{p_cappuccino}")
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f" Water: {resources['water']} ml")
        print(f" Milk: {resources['milk']} ml")
        print(f" Coffee: {resources['coffee']} g")
        print(f" Money: ₹{profit}")
    else:
        drink = MENU[choice]
        if resource_suff(drink["ingredients"]) :
            payment = int(input("Enter the total amount: ₹"))
            if payment_success(payment , drink["cost"]):
                make_coffee(choice, drink["ingredients"])




