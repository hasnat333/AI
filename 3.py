def main():
    # Ask the user to input a grade
    grade = input("Enter your grade (A, B, C, D, or F): ").upper()

    # Assign messages based on the grade
    if grade == 'A':
        print("Excellent")
    elif grade == 'B':
        print("Good")
    elif grade == 'C':
        print("Average")
    elif grade == 'D':
        print("Pass")
    elif grade == 'F':
        print("Fail")
    else:
        print("Invalid grade entered. Please enter A, B, C, D, or F.")

if __name__ == "__main__":
    main()
