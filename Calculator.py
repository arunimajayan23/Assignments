class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self,x, y):
        try:
            return x / y
        except ZeroDivisionError:
            print("Error: division by zero is undefinable")
            return None

def main():
    calculator = Calculator()
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            result = calculator.add(num1, num2)
            print(num1, "+", num2, "=", result)
        elif choice == '2':
            result = calculator.subtract(num1, num2)
            print(num1, "-", num2, "=", result)
        elif choice == '3':
            result = calculator.multiply(num1, num2)
            print(num1, "*", num2, "=", result)
        elif choice == '4':
            result = calculator.divide(num1, num2)
            if result is not None:
                print(num1, "/", num2, "=", result)
        elif choice =='5':
            break
        else:
            print("Invalid input")


if __name__ == '__main__':
    main()
