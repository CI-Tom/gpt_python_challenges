# 4. Fibonacci Sequence
# Write a function to generate the Fibonacci sequence up to a specified number of terms.

def generate_fibonacci(n):
    # Initialize variables
    fibonacci_sequence = []
    a, b = 0, 1  # Initialize the first two terms

    # Generate the sequence
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b  # Calculate the next term

    return fibonacci_sequence


while True:
    try:
        # Step 1: User Input
        user_input = int(input("Enter the number of Fibonacci terms to generate: "))

        # Step 2: Input Validation
        if user_input <= 0:
            raise ValueError("Input must be a positive integer.")

        # Step 3: Generate and Display Fibonacci Sequence
        result = generate_fibonacci(user_input)
        print(result)

        # Exit the loop if valid input and calculation are successful
        break

    except ValueError as e:
        # Handle input errors and continue the loop to allow the user to re-enter input
        print(e)
