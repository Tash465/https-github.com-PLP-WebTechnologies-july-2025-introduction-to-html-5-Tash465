"""
Simple Calculator Program
Performs basic math operations on two numbers
"""

def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number")

def main():
    print("Simple Calculator\n" + "=" * 20)
    
    # Get user input
    num1 = get_number("First number: ")
    num2 = get_number("Second number: ")    
    
    # Calculate results
    calculations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
    }
    
    # Handle division safely
    try:
        calculations['/'] = num1 / num2
    except ZeroDivisionError:
        calculations['/'] = "Undefined (can't divide by zero)"
    
    # Display results nicely
    print("\nResults:")
    for operation, result in calculations.items():
        print(f"{operation}: {result}".ljust(20))  # Left aligns for nicer formatting

if __name__ == "__main__":
    main()
