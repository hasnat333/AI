def main():
    # Create a dictionary containing the names of friends and their ages
    friends_age = {
        "Alice": 30,
        "Bob": 25,
        "Charlie": 28,
        "David": 35,
        "Emma": 27
    }

    # Print the age of a specific friend
    friend_name = input("Enter the name of your friend: ")
    if friend_name in friends_age:
        print(f"{friend_name}'s age is {friends_age[friend_name]}.")
    else:
        print(f"Sorry, {friend_name} is not in your friend list.")

if __name__ == "__main__":
    main()
