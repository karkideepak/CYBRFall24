class Car:
    # Creating a class Car
    def __init__(self, brand, model, year, rental_price):
        # Defining the initializer and passing the arguments
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_price = rental_price

    def display_details(self):
        # Method to display car details
        print(self.brand, self.model, self.year, self.rental_price)

    def calculate_rental(self, days):
        # Method to calculate the rental cost based on the passed number of days
        invoice = self.rental_price * days
        return invoice

# Creating car1 object
print("Test Case: 1")
car1 = Car("Toyota", "Camry", 2020, 40)
# Accessing car attributes using display_details methods
car1.display_details()
# Rental cost for 5 days, passing the days argument to calculate_rental function
days = 5
car1.calculate_rental(days)
print(f"Total rental cost for {days} days is ${car1.calculate_rental(days)}")
print("- "*20)

# Creating car2 object
print("Test Case: 2")
car2 = Car("Honda", "Civic", 2019, 35)
car2.display_details()
# Rental cost for 7 days,
days = 7
car2.calculate_rental(days)
print(f"Total rental cost for {days} days is ${car2.calculate_rental(days)}")
print("- "*20)

# Similarly
print("Test Case: 3")
car3 = Car("Tesla", "Model Y", 2024, 100)
car3.display_details()
days = 10
car3.calculate_rental(days)
print(f"Total rental cost for {days} days is ${car3.calculate_rental(days)}")
print("- "*20)
