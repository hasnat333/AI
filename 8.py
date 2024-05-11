def main():
    # Create a list of favorite movies
    favorite_movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction"]

    # Print the original list of favorite movies
    print("Original list of favorite movies:")
    print(favorite_movies)

    # Add a new movie to the list
    new_movie = input("Enter a new favorite movie: ")
    favorite_movies.append(new_movie)

    # Print the updated list of favorite movies
    print("\nUpdated list of favorite movies:")
    print(favorite_movies)

if __name__ == "__main__":
    main()
