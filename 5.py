def print_multiplication_table():
    print("Multiplication Table (up to 10):")
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end="\t")
        print()

def main():
    print_multiplication_table()

if __name__ == "__main__":
    main()
