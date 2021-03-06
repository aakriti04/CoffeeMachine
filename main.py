from Menu import MENU
from Resources import resources

money=0


def print_report():
    """Prints Report of quantity of Resources left in the Machine"""
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")


def check_resources(coffee_type):
    """"Validates the actual amount of resources left to the amount of resources required"""
    for ingredient in MENU[coffee_type]["ingredients"]:
        if resources[ingredient] < MENU[coffee_type]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def calculate_coin_amount():
    """"Calculates total cash given by customer"""
    print("Please Insert Coins: ")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_cash = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    return round(total_cash, 2)


def process_transaction(given_cash, coffee_type):
    """"Validates actual cash with expected cost"""
    expected_cash = MENU[coffee_type]["cost"]
    if given_cash < expected_cash:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global money
        money += expected_cash
        if given_cash > expected_cash:
            refund = round(given_cash - expected_cash ,2)
            print(f"Cash Given: ${given_cash}")
            print(f"Cash Expected: ${expected_cash}")
            print(f"Here is ${refund} dollars in change.")
        return True


def dispense_coffee(coffee_type):
    """"Serves Coffee to Customer and updates Machine resources """
    for ingredient in MENU[coffee_type]["ingredients"]:
        resources[ingredient] -= MENU[coffee_type]["ingredients"][ingredient]
    print(f"Here is your {user_input}. Enjoy!")


if __name__ == '__main__':
    print("Welcome to Coffee Machine")
    isMachineOn = True
    while isMachineOn:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == "off":
            isMachineOn = False
        elif user_input == "report":
            print_report()
        elif user_input in MENU:
            print(f"coffee type: {user_input}")
            enoughResources = check_resources(user_input)
            if enoughResources:
                actual_cash = calculate_coin_amount()
                transactionSuccess = process_transaction(actual_cash, user_input)
                if transactionSuccess:
                    dispense_coffee(user_input)
        else:
            print("Please Enter Valid input")





