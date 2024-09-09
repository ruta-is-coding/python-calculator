from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(logo)

number1 = float(input("What's the first number? "))

while True:
    for key in operations:
        print(key)

    operator = input("Pick an operation: ")

    # Restart the loop if invalid operator
    if operator not in operations:
        print("Invalid operation! Try again!")
        continue

    # Ask for number2 again if division by zero
    while True:
        try:
            number2 = float(input("What's the second number? "))
            result = operations[operator](number1, number2)
            break
        except ZeroDivisionError:
            print("Division by zero is not allowed!")

    print(f"{number1} {operator} {number2} = {result}")

    choice = input(f"Type 'y' to continue calculating with {result}, "
                             f"or type 'n' to start a new calculation: ").lower()

    if choice == 'y':
        number1 = result
    elif choice == 'n':
        print("\n" * 100)
        number1 = float(input("What's the first number? "))
        number2 = 0
        result = 0
        continue
    # Break the loop if invalid input
    else:
        print("Invalid input!")
        break
