coffeeMachine = {
    "Water": 300,
    "Milk":200,
    "Coffee":100,
    "Money": 0

}
moneyCollector = {
    "quarters":{
        "quantity":0,
        "value" : 0.25
    },
    "dimes":{
        "quantity":0,
        "value" : 0.10
    },
    "nickles":{
        "quantity":0,
        "value" : 0.05
    },
    "pennies":{
        "quantity":0.01,
        "value" : 0.01
    }
}

material = {
    "expresso": {
        "Water" : 50,
        "Coffee" : 18,
        "Money" : 1.5
    },
    "latte":{
        "Water": 200,
        "Coffee": 24,
        "Milk": 150,
        "Money": 2.50
    },
    "Cappuccino":{
        "Water": 250,
        "Coffee": 24,
        "Milk": 100,
        "Money": 3.00
    }

}

def coffeeMachineF():
    while True:
        user = input("What would you like? (expresso/latte/cappuccino): ")
        if user == "report":
            for key in coffeeMachine:
                print(key + ": " + coffeeMachine[key])
        elif user == "expresso" or user == "latte" or user =="cappuccino" :
            for key in moneyCollector:
                moneyCollector[key]["quantity"] = input("How many " + key)
                coffeeMachine["Money"] += float(moneyCollector[key]["quantity"]) * moneyCollector[key]["value"]
            for key in material[user]:
                coffeeMachine[key] -= material[user][key]
                coffeeMachine[key] = abs(coffeeMachine[key])

            print(moneyCollector)
            print(coffeeMachine)








