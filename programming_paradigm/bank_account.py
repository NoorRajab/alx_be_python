class BankAccount:
    """
    A simple class to represent a bank account with deposit, 
    withdraw, and display balance functionalities.
    """
    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount with an optional initial balance, 
        defaulting to 0.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._account_balance = initial_balance  # Using underscore for convention of a protected/internal attribute

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.
        """
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deducts the amount from the account balance if funds are sufficient.

        Returns:
            bool: True if withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
            
        if self._account_balance >= amount:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")



