def calculate_sum(**kwargs):
    """
    Calculate the sum of numbers provided as keyword arguments.

    Args:
        **kwargs: Arbitrary number of keyword arguments representing numbers.

    Returns:
        float: The sum of the provided numbers.
    """
    return sum(kwargs.values())

# Example usage:
result = calculate_sum(num1=5, num2=10, num3=15)
print("Sum:", result)
