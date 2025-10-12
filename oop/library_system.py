class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_details(self) -> str:
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size 

    def get_details(self) -> str:
        base_details = super().get_details().replace("Book: ", "EBook: ")
        return f"{base_details}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count 

    def get_details(self) -> str:
        base_details = super().get_details().replace("Book: ", "PrintBook: ")
        return f"{base_details}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def list_books(self):
        print("\n--- Library Collection ---")
        for book in self.books:
            print(book.get_details())
        print("--------------------------")