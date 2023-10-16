my_list = input("Enter numbers, separated by '/': ")
my_list = my_list.split("/")


def find_largest_number():
    num_list = [int(x) for x in my_list]  # Convert strings to integers
    largest_number = max(num_list)
    print(f"The largest number in the list is {largest_number}")


find_largest_number()
