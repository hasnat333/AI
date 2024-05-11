def calculate_rectangle_area(length, width):
    return length * width

def main():
    # Ask the user to input the length and width of the rectangle
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate the area of the rectangle
    area = calculate_rectangle_area(length, width)

    # Print the result
    print("The area of the rectangle is:", area)

if __name__ == "__main__":
    main()



