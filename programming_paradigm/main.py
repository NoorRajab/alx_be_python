# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    """
    Interfaces with the command line, validates the number of arguments,
    and calls safe_divide with the provided numerator and denominator.
    """
    # 1. Check for the correct number of arguments. sys.argv[0] is the script name.
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        # Exit with a non-zero status code to indicate an error
        sys.exit(1)

    # 2. Extract the arguments (which are strings from the command line)
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # 3. Call the robust division function
    result = safe_divide(numerator, denominator)
    
    # 4. Print the final result or error message
    print(result)

if __name__ == "__main__":
    main()