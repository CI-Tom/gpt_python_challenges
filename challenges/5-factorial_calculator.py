# 5. Factorial Calculator
# Create a function that calculates the factorial of a given number.

def factorial_iterative(n):
    """
    Calculate the factorial of a given non-negative integer using an iterative approach.

    Args:
    n (int): The non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the input integer 'n'.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


while True:
    try:
        # Step 1: User Input
        n = int(input("Enter a non-negative integer to calculate its factorial: "))

        # Step 2: Input Validation
        if n < 0:
            print("Factorial is undefined for negative numbers.")
        else:
            # Step 3: Calculate and Display Factorial
            result = factorial_iterative(n)
            print(f"{n}! = {result}")

            # Exit the loop if valid input and calculation are successful
            break

    except ValueError:
        # Handle invalid input and continue the loop to allow the user to re-enter input
        print("Invalid input. Please enter a non-negative integer.")
