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


# Initialize the result variable
result = None

# Use a while loop to repeatedly prompt for input until valid input is provided
while True:
    try:
        # Prompt the user for the first number and convert it to a float
        num1 = float(input("Choose your first number: "))

        while True:
            try:
                # Prompt the user for the second number and convert it to a float
                num2 = float(input("Choose your second number: "))
                break  # Exit the inner loop if num2 is successfully obtained

            except ValueError:
                # Handle exceptions (invalid input for num2) and ask for re-entry
                print("Invalid input for num2. Please enter a valid number for num2.")

        while True:
            # Prompt the user for the operator
            operator = input("Choose add(+), subtract(-), multiply(*) or divide(/): ")

            # Check if the operator is valid, and exit the operator input loop if it is
            if operator in ["+", "-", "*", "/"]:
                break

            # Handle an invalid operator
            print("Invalid operator. Please choose a valid operator.")

        # Check for division by zero and raise an error if detected
        if operator == "/" and num2 == 0:
            raise ValueError("Division by zero is not allowed.")

        # Perform the requested operation based on the operator
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2

        # Display the result
        print("Result:", result)

        # Ask the user if they want to calculate again
        choice = input("Do you want to calculate again? (yes/y or no/n): ")

        # Check the user's choice to continue or exit the program
        if choice.lower() not in ["yes", "y"]:
            break

    except ValueError as e:
        # Handle exceptions (invalid input for num1, invalid operator, division by zero) and print error messages
        print(e)
