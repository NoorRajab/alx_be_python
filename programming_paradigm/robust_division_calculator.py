# robust_division_calculator.py

def safe_divide(numerator_str, denominator_str):
    """
    Performs division, robustly handling ZeroDivisionError and ValueError 
    for non-numeric inputs.

    Args:
        numerator_str (str): The numerator as a string.
        denominator_str (str): The denominator as a string.

    Returns:
        str: The division result or an appropriate error message.
    """
    try:
        # Attempt to convert the string arguments to floats.
        numerator = float(numerator_str)
        denominator = float(denominator_str)
        
    except ValueError:
        # Catches cases where one or both arguments cannot be converted to a float (non-numeric).
        return "Error: Please enter numeric values only."

    try:
        # Perform the division after successful conversion.
        result = numerator / denominator
        return f"The result of the division is {result}"
        
    except ZeroDivisionError:
        # Catches the specific case where the denominator is zero (e.g., float('0')).
        return "Error: Cannot divide by zero."

# You can optionally add test cases here to verify the function's logic
# without running it via main.py, though the task specifies using main.py 
# for final verification.

# Example self-tests (not strictly required by the prompt, but good practice):
# print(safe_divide('10', '5'))     # Expected: The result of the division is 2.0
# print(safe_divide('10', '0'))     # Expected: Error: Cannot divide by zero.
# print(safe_divide('ten', '5'))    # Expected: Error: Please enter numeric values only.