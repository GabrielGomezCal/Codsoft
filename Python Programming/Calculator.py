import math

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        return a ** b
    
    def modulus(self, a, b):
        return a % b
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        elif n == 0:
            return 1
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result
    
    def square_root(self, n):
        if n < 0:
            raise ValueError("Cannot take square root of negative number")
        return n ** 0.5
    
    def logarithm(self, a, base=10):
        if a <= 0:
            raise ValueError("Logarithm is not defined for non-positive numbers")
        if base <= 1:
            raise ValueError("Base must be greater than 1")
        return math.log(a, base)
    
    def percentage(self, total, part):
        if total == 0:
            raise ValueError("Total cannot be zero for percentage calculation")
        return (part / total) * 100

class Menu:
    def __init__(self):
        self.calculator = Calculator()
        self.operations = {
            '1': ('Add', self.calculator.add),
            '2': ('Subtract', self.calculator.subtract),
            '3': ('Multiply', self.calculator.multiply),
            '4': ('Divide', self.calculator.divide),
            '5': ('Power', self.calculator.power),
            '6': ('Modulus', self.calculator.modulus),
            '7': ('Factorial', self.calculator.factorial),
            '8': ('Square Root', self.calculator.square_root),
            '9': ('Logarithm', self.calculator.logarithm),
            '10': ('Percentage', self.calculator.percentage)
        }
    
    def show_menu(self):
        print("\nCalculator Menu:")
        for key, (name, _) in self.operations.items():
            print(f"{key}. {name}")
    
    def get_choice(self):
        choice = input("Select an operation (1-10): ")
        if choice not in self.operations:
            print("Invalid choice. Please try again.")
            return self.get_choice()
        return choice
    
    def get_numbers(self, op_name):
        try:
            if op_name in ['Factorial', 'Square Root']:
                num = float(input(f"Enter the number for {op_name}: "))
                return (num,)
            
            a = float(input("Enter the first number: "))
            if op_name == 'Percentage':
                total = float(input("Enter the total: "))
                return (total, a)
            
            b = float(input("Enter the second number: "))
            return (a, b)
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return self.get_numbers(op_name)
    
    def run(self):
        while True:
            self.show_menu()
            choice = self.get_choice()
            operation_name, operation_func = self.operations[choice]
            args = self.get_numbers(operation_name)
            
            try:
                result = operation_func(*args)
                print(f"\nResult of {operation_name}: {result}")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")
            
            another = input("\nDo you want to perform another operation? (y/n): ").lower()
            if another != 'y':
                print("\nThank you for using the calculator. Goodbye!")
                break

menu = Menu()
menu.run()
