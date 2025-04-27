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

class Menu:
    def __init__(self):
        self.calculator = Calculator()
        self.operations = {
            '1': ('Add', self.calculator.add),
            '2': ('Subtract', self.calculator.subtract),
            '3': ('Multiply', self.calculator.multiply),
            '4': ('Divide', self.calculator.divide),
            '5': ('Power', self.calculator.power),
            '6': ('Modulus', self.calculator.modulus)
        }
    
    def show_menu(self):
        print("\nCalculator Menu:")
        for key, (name, _) in self.operations.items():
            print(f"{key}. {name}")
    
    def get_choice(self):
        choice = input("Select an operation (1-6): ")
        if choice not in self.operations:
            print("Invalid choice. Please try again.")
            return self.get_choice()
        return choice
    
    def get_numbers(self):
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            return (a, b)
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return self.get_numbers()
    
    def run(self):
        while True:
            self.show_menu()
            choice = self.get_choice()
            operation_name, operation_func = self.operations[choice]
            a, b = self.get_numbers()
            
            try:
                result = operation_func(a, b)
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
