class Book:
    """
    Represents a book in the library with a title, author, and availability status.
    The _is_checked_out attribute uses the Python convention for a "private" attribute.
    """
    def __init__(self, title: str, author: str):
        # Public attributes
        self.title = title
        self.author = author
        # Private-convention attribute to track availability
        self._is_checked_out = False

    def is_available(self) -> bool:
        """Returns True if the book is not checked out."""
        return not self._is_checked_out

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False # Already checked out

    def return_book(self):
        """Marks the book as available (returned)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False # Already returned

    def __str__(self):
        """A simple string representation for printing."""
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects and provides methods for library operations.
    The _books attribute uses the Python convention for a "private" list.
    """
    def __init__(self):
        # Private-convention attribute to store the list of Book objects
        self._books = []

    def add_book(self, book: Book):
        """Adds a Book object to the library's collection."""
        self._books.append(book)
        print(f"Added book: {book.title}")

    def _find_book(self, title: str) -> Book | None:
        """Helper method to find a book by its title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title: str):
        """Finds a book by title and attempts to check it out."""
        book = self._find_book(title)
        if book:
            if book.check_out():
                print(f"SUCCESS: '{title}' has been checked out.")
            else:
                print(f"NOTE: '{title}' is already checked out.")
        else:
            print(f"ERROR: Book with title '{title}' not found in the library.")

    def return_book(self, title: str):
        """Finds a book by title and attempts to return it."""
        book = self._find_book(title)
        if book:
            if book.return_book():
                print(f"SUCCESS: '{title}' has been returned.")
            else:
                print(f"NOTE: '{title}' was already available.")
        else:
            print(f"ERROR: Book with title '{title}' not found in the library.")

    def list_available_books(self):
        """Prints the title and author of all books that are currently available."""
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(book)
                available_count += 1
        
        if available_count == 0:
            print("No books are currently available.")

# The user-provided main.py will use these classes for testing.