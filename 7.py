# Define a global variable
global_var = "I am a global variable"

# Define a function
def test_scope():
    # Define a local variable
    local_var = "I am a local variable"
    # Print both global and local variables
    print("Inside the function:")
    print("global_var:", global_var)
    print("local_var:", local_var)

# Call the function
test_scope()

# Print only the global variable outside the function
print("\nOutside the function:")
print("global_var:", global_var)
