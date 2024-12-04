class Book:
    def __init__(self, title, author, ISBN, available_copies):
        self.title = title
        self.ISBN = ISBN
        self.author = author
        self.available_copies = available_copies

class Patron:
    def __init__(self, name, library_card_number):
        self.name = name
        self.library_card_number = library_card_number
        self.books_borrowed = {}

class Library:
    def __init__(self, name):
        self.name = name
        self.patrons = {}
        self.books = {}

    def new_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        ISBN = input("Enter the ISBN of the book: ")
        available_copies = int(input("Enter how many copies are available for the book: "))
        book = Book(title, author, ISBN, available_copies)
        self.books[ISBN] = book

    def remove_book(self):
        ISBN = input("Enter ISBN of book to remove from the system records: ")
        if ISBN in self.books:
            print(f"Understood. Book {ISBN} has been removed from the system records.")
            del self.books[ISBN]
        else:
            print("Invalid input. Book does not exist in system records.")

    def register_new_patron(self):
        name = input("Enter the name of the patron: ")
        library_card_number = input("Enter the library card number of the patron: ")
        patron = Patron(name, library_card_number)
        self.patrons[library_card_number] = patron

    def remove_patron(self):
        library_card_number = input("Enter the library card number of the patron to remove: ")
        if library_card_number in self.patrons:
            del self.patrons[library_card_number]
            print("Patron removed successfully.")
        else:
            print("Invalid input. Patron not found.")

    def borrow_book(self):
        library_card_number = input("Enter the library card number of the patron: ")
        ISBN = input("Enter the ISBN of the book to borrow: ")
        amount = int(input("Enter the number of copies to borrow: "))
        if library_card_number in self.patrons and ISBN in self.books:
            if self.books[ISBN].available_copies >= amount:
                self.books[ISBN].available_copies -= amount
                if ISBN in self.patrons[library_card_number].books_borrowed:
                    self.patrons[library_card_number].books_borrowed[ISBN] += amount
                else:
                    self.patrons[library_card_number].books_borrowed[ISBN] = amount
                print("Book(s) borrowed successfully.")
            else:
                print("Not enough copies available.")
        else:
            print("Invalid library card number or ISBN.")

    def return_book(self):
        library_card_number = input("Enter the library card number of the patron: ")
        ISBN = input("Enter the ISBN of the book to return: ")
        amount = int(input("Enter the number of copies to return: "))
        if library_card_number in self.patrons and ISBN in self.books:
            if ISBN in self.patrons[library_card_number].books_borrowed:
                if self.patrons[library_card_number].books_borrowed[ISBN] >= amount:
                    self.books[ISBN].available_copies += amount
                    self.patrons[library_card_number].books_borrowed[ISBN] -= amount
                    print("Book(s) returned successfully.")
                else:
                    print("You can't return more copies than borrowed.")
            else:
                print("This patron hasn't borrowed this book.")
        else:
            print("Invalid library card number or ISBN.")

    def display_list_of_books(self):
        print("List of Books:")
        for ISBN, book in self.books.items():
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {ISBN}, Available Copies: {book.available_copies}")

    def display_list_of_patrons(self):
        print("List of Patrons:")
        for library_card_number, patron in self.patrons.items():
            print(f"Name: {patron.name}, Library Card Number: {library_card_number}")

def main():
    library_name = input("Enter the name of the library: ")
    library = Library(library_name)

    while True:
        print("\nLibrary Management System Menu:")
        print("[1] Add a new book")
        print("[2] Remove a book")
        print("[3] Register new patron")
        print("[4] Remove a patron")
        print("[5] Borrow a book")
        print("[6] Return a book")
        print("[7] Display list of books available")
        print("[8] Display list of patrons registered")
        print("[9] Exit the program")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.new_book()
        elif choice == "2":
            library.remove_book()
        elif choice == "3":
            library.register_new_patron()
        elif choice == "4":
            library.remove_patron()
        elif choice == "5":
            library.borrow_book()
        elif choice == "6":
            library.return_book()
        elif choice == "7":
            library.display_list_of_books()
        elif choice == "8":
            library.display_list_of_patrons()
        elif choice == "9":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
