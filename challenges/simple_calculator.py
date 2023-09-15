# Define the arithmetic functions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed."
    return x / y


# Use a while loop to repeatedly prompt for input until valid input is provided
while True:
    try:
        # Prompt the user for the first number
        num1 = float(input("Choose your first number: "))
        num2 = float(input("Choose your second number: "))
        operator = input("Choose add(+), subtract(-), multiply(*) or divide(/): ")

        # Perform the requested operation based on user input
        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            result = "Invalid operator"

        # Print the result
        print("Result:", result)

    except ValueError:
        # Handle invalid input (non-numeric)
        print("Invalid input. Please enter a valid number.")
        continue  # Continue the loop to allow the user to retry
    else:
        # Exit the loop if valid input is provided
        break
