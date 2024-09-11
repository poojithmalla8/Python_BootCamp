MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 500,
    "money": 5.0
}

cash_register = {
    "quarters": 10,  # Number of quarters available
    "dimes": 13,     # Number of dimes available
    "nickles": 20,   # Number of nickles available
    "pennies": 20    # Number of pennies available
}

coin_value = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

def calculate_change(change):
    """Calculate the change to return using available coins."""
    change_distribution = {"quarters": 0, "dimes": 0, "nickles": 0, "pennies": 0}
    for coin, value in coin_value.items():
        while change >= value and cash_register[coin] > 0:
            change = round(change - value, 2)
            change_distribution[coin] += 1
            cash_register[coin] -= 1
    return change_distribution, change

def display_change(change_distribution):
    """Display the coins returned as change."""
    print("Returning Change: ")
    for coin, count in change_distribution.items():
        if count > 0:
            print(f"{count} {coin.capitalize()}")

off = True

while off:
    print("What would you like? (espresso/latte/cappuccino)")
    print("A.  Espresso - $1.50")
    print("B.  Latte - $2.50")
    print("C.  Cappuccino - $3.00")

    coffeechoice = input("Your choice of Coffee   ☕ : ")

    if coffeechoice.lower() == 'off':
        off = False
        print("Thank you for your business! ☕ :)")
        break

    if coffeechoice.lower() == 'report':
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${resources['money']}")
        print(f"Quarters: {cash_register['quarters']}")
        print(f"Dimes: {cash_register['dimes']}")
        print(f"Nickles: {cash_register['nickles']}")
        print(f"Pennies: {cash_register['pennies']}")
        continue

    print("Pay money in coins: ")
    print("Accepted coins: Quarters, Dimes, Nickles, and Pennies")
    quarters = int(input("Insert Quarters x$0.25: "))
    dimes = int(input("Insert Dimes x$0.10: "))
    nickles = int(input("Insert Nickles x$0.05: "))
    pennies = int(input("Insert Pennies x$0.01: "))
    moneygiven = float((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01))
    print(f"Total Money given: ${moneygiven:.2f}")

    # Update the cash register with the inserted coins
    cash_register["quarters"] += quarters
    cash_register["dimes"] += dimes
    cash_register["nickles"] += nickles
    cash_register["pennies"] += pennies

    if coffeechoice.lower() == 'a':  # Espresso
        cost = 1.5
        if resources['water'] >= 50 and resources['coffee'] >= 18 and moneygiven >= cost:
            resources['water'] -= 50
            resources["coffee"] -= 18
            resources["money"] += cost
            change = round(moneygiven - cost, 2)
            change_distribution, remaining_change = calculate_change(change)
            if remaining_change > 0:
                print("Sorry, unable to provide exact change. Returning your money.")
                # Revert the cash register update
                cash_register["quarters"] -= quarters
                cash_register["dimes"] -= dimes
                cash_register["nickles"] -= nickles
                cash_register["pennies"] -= pennies
                continue
            print("Here is your Espresso. Enjoy!")
            display_change(change_distribution)
        else:
            print("Sorry, not enough resources or money. Returning your money.")
            continue

    elif coffeechoice.lower() == 'b':  # Latte
        cost = 2.5
        if resources['water'] >= 200 and resources['coffee'] >= 24 and moneygiven >= cost and resources["milk"] >= 150:
            resources['water'] -= 200
            resources["coffee"] -= 24
            resources["milk"] -= 150
            resources["money"] += cost
            change = round(moneygiven - cost, 2)
            change_distribution, remaining_change = calculate_change(change)
            if remaining_change > 0:
                print("Sorry, unable to provide exact change. Returning your money.")
                # Revert the cash register update
                cash_register["quarters"] -= quarters
                cash_register["dimes"] -= dimes
                cash_register["nickles"] -= nickles
                cash_register["pennies"] -= pennies
                continue
            print("Here is your Latte. Enjoy!")
            display_change(change_distribution)
        else:
            print("Sorry, not enough resources or money. Returning your money.")
            continue

    elif coffeechoice.lower() == 'c':  # Cappuccino
        cost = 3.0
        if resources['water'] >= 250 and resources['coffee'] >= 24 and moneygiven >= cost and resources["milk"] >= 100:
            resources['water'] -= 250
            resources["coffee"] -= 24
            resources["milk"] -= 100
            resources["money"] += cost
            change = round(moneygiven - cost, 2)
            change_distribution, remaining_change = calculate_change(change)
            if remaining_change > 0:
                print("Sorry, unable to provide exact change. Returning your money.")
                # Revert the cash register update
                cash_register["quarters"] -= quarters
                cash_register["dimes"] -= dimes
                cash_register["nickles"] -= nickles
                cash_register["pennies"] -= pennies
                continue
            print("Here is your Cappuccino. Enjoy!")
            display_change(change_distribution)
        else:
            print("Sorry, not enough resources or money. Returning your money.")
            continue

    else:
        print("Invalid choice. Please try again.")
        continue

    # Reset inputs for the next round
    moneygiven = 0
    pennies = 0
    dimes = 0
    nickles = 0
    quarters = 0
