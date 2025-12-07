# This is linked to Chapt26.py

class Car:
    def __init__(self, model, year, color, for_sale): #Example of constucter method and init means intialize
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    # Methods
    def drive(self):
        print(f"Your drive the {self.color} {self.model}")
    
    def stop(self):
        print(f"You stop the {self.color} {self.model}")
    
    def describe(self):
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"For sale: {self.for_sale}")
        