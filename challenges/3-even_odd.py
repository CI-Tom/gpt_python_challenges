# 3. Even or Odd
# Write a program that takes an integer as input and determines whether it's even or odd.

while True:
    try:
        # Get User Input
        num = int(input("Enter an integer: "))

        # Check for Even or Odd
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")

        # Exit the loop if valid input is provided
        break

    except ValueError:
        print("Invalid input. Please enter an integer.")
