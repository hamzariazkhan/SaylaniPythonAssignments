# CLasess
# 1) Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

def main():
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
    
    print(f"Area of the circle: {circle.area():.2f}")
    print(f"Perimeter of the circle: {circle.perimeter():.2f}")

# 2) Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

    def age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

def main():
    name = input("Enter the person's name: ")
    country = input("Enter the person's country: ")
    date_of_birth = input("Enter the person's date of birth (YYYY-MM-DD): ")
    
    person = Person(name, country, date_of_birth)
    
    print(f"Name: {person.name}")
    print(f"Country: {person.country}")
    print(f"Age: {person.age()} years")
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

def main():
    calc = Calculator()
    
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Choose an operation (1-5): ")
        
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if choice == '1':
                result = calc.add(a, b)
                print(f"Result: {result}")
            elif choice == '2':
                result = calc.subtract(a, b)
                print(f"Result: {result}")
            elif choice == '3':
                result = calc.multiply(a, b)
                print(f"Result: {result}")
            elif choice == '4':
                result = calc.divide(a, b)
                print(f"Result: {result}")
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()
