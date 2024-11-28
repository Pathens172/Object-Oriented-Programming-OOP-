# A simple class for a Book
class Book:
    # Constructor to initialize the book's details
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # A method to describe the book
    def describe(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."

    # A method to read the book
    def read(self):
        return f"Enjoy reading '{self.title}'!"

# Create an object of the Book class
my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)

# Print the details of the book
print(my_book.describe())

# Read the book
print(my_book.read())
