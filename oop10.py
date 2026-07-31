class CoffeeMachine:
    def __init__(self):
        self.water_level = 100
        self.coffee_beans = 50

    def make_coffee(self):
        if self.water_level >= 20 and self.coffee_beans >= 10:
            self.water_level -= 20
            self.coffee_beans -= 10
            print("Coffee is ready!")
        else:
            print("Please refill.")

    def refill(self):
        self.water_level = 100
        self.coffee_beans = 50
        print("Machine refilled.")

cm = CoffeeMachine()
cm.make_coffee()
cm.make_coffee()
cm.refill()