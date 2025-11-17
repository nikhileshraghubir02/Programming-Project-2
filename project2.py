class Beverage:
    def __init__(self, beverage_type, beverage_cost):
        self.beverage_type = beverage_type
        self.beverage_cost = beverage_cost
class VendingMachine:
    def __init__(self):
        self.beverages = {
            "1": Beverage("Fanta", 2.00),
            "2": Beverage("Dr Pepper", 3.00),
            "3": Beverage("Coca Cola", 1.50),
            "4": Beverage("Mtn Dew", 2.50),
            "5": Beverage("Sprite", 1.75),
            "6": Beverage("Ginger Ale", 2.75)
        }
    def display_menu(self):
        print("\nWelcome to the Beverage Vending Machine!\n")
        for key, beverage in self.beverages.items():
            print(f"{key}. {beverage.beverage_type} - ${beverage.beverage_cost:.2f}")
    def vend(self):
        while True:
            self.display_menu()
            choice = input("\nWhich beverage would you like to purchase (1-6): ")
            if choice not in self.beverages:
                print("\nThat is not an option. Please choose from the list provided.")
                continue
            beverage = self.beverages[choice]
            print(f"\nYou chose {beverage.beverage_type}. Price: ${beverage.beverage_cost:.2f}")
            try:
                money = float(input("\nInsert money: $ "))
            except ValueError:
                print("\nThat is invalid. Please insert a valid number.")
                continue
            if money > beverage.beverage_cost:
                change = money - beverage.beverage_cost
                print(f"Dispensing {beverage.beverage_type}")
                print(f"Your change is: ${change:.2f}")
            elif money < beverage.beverage_cost:
                print(f"That is not enough money. You need to insert ${beverage.beverage_cost - money:.2f} more.")
            else:
                print(f"Dispensing {beverage.beverage_type}")
            print("Thank you for your purchase!\n")
machine = VendingMachine()
machine.vend()


