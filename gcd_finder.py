def find_gcd(a, b):
    """
    Find the Greatest Common Divisor (GCD) of two numbers using Euclidean algorithm.
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        The GCD of a and b
    """
    a, b = abs(a), abs(b)
    
    while b != 0:
        a, b = b, a % b
    
    return a


def main():
    """Main function to get user input and display GCD."""
    print("=" * 40)
    print("   GCD (Greatest Common Divisor)")
    print("=" * 40)
    
    try:
        # Get user input
        num1 = int(input("\nEnter first number: "))
        num2 = int(input("Enter second number: "))
        
        # Calculate GCD
        result = find_gcd(num1, num2)
        
        # Display result
        print(f"\nThe GCD of {num1} and {num2} is: {result}")
        
    except ValueError:
        print("Error: Please enter valid integers.")


if __name__ == "__main__":
    main()
