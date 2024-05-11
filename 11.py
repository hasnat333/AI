def main():
    # Take a list of numbers as input from the user
    numbers_str = input("Enter a list of numbers separated by spaces: ")
    numbers_list = numbers_str.split()

    # Convert the list of numbers to a set to get unique numbers
    unique_numbers_set = set(numbers_list)

    # Print the set containing unique numbers
    print("Unique numbers:", unique_numbers_set)

if __name__ == "__main__":
    main()
