from datetime import date


class Book:
    def __init__(self, title, author, isbn, available_copies, total_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies
        self.total_copies = total_copies

    def __repr__(self):
        return "Title: " + self.title + ", Author: " + self.author + ", ISBN: " + \
            str(self.isbn) + ", Available Copies: " + str(self.available_copies)

    @staticmethod
    def check_availability(self, book, title, available_copies):
        if book in books and available_copies != 0:
            print(f"Book {title} is available for borrowing.")
        else:
            print(f"Sorry, {title} is not available.")


class Member(Book):
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def __repr__(self):
        return "Member ID: " + self.member_id + ", Name: " + self.name

    def borrow_book(self, book, isbn):
        Book.borrow_book(self, book, isbn)

    def return_book(self, book, isbn):
        Book.return_book(self, book, isbn)


class Transaction:
    def __init__(self, member, book, borrow_date):
        self.member = member
        self.book = book
        self.borrow_date = borrow_date(date.today())

    def __repr__(self):
        return "Member ID: " + self.member + ", Borrowed book/s: " + self.book + ", Date Borrowed: " + str(self.borrow_date)


def main():
    global books

    books = []
    members = []
    transactions = []

    while True:
        print("\nWelcome to the Library Management System!")
        print("[1] Add Book")
        print("[2] Add Member")
        print("[3] Borrow Book")
        print("[4] Return Book")
        print("[5] Display Books")
        print("[6] Display Members")
        print("[7] Display Member Transactions")
        print("[8] Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author of book: ")
            isbn = input("Enter ISBN of book: ")
            total_copies = int(input("Enter total copies: "))
            available_copies = int(input("Enter available copies: "))
            book = Book(title, author, isbn, available_copies, total_copies)
            print("Book added successfully. Thank you!")
            books.append(book)

        elif choice == '2':
            member_id = input("Enter library member ID: ")
            name = input("Enter member name: ")
            member = Member(member_id, name)
            print("Member added successfully. Thank you!")
            members.append(member)

        elif choice == '3':
            member_id = input("Enter member ID: ")
            # credits po to aidan for this code :D
            member = next((member for member in members if member.member_id == member_id), None)
            if member:
                isbn = input("Enter ISBN of the book to borrow: ")
                # credits po to aidan for this code :D
                book = next((book for book in books if book.isbn == isbn), None)
                if book:
                    print(f"You have borrowed {isbn}. \n"
                          f"Your due date for borrowing is 3 days from {date.today()}. \n"
                          f"Thank you!")
                else:
                    print(f"Sorry, {isbn} is not available.")
            else:
                print("Please register as a member first, before borrowing a book.")

        elif choice == '4':
            member_id = input("Enter member ID: ")
            # credits po to aidan for this code :D
            member = next((member for member in members if member.member_id == member_id), None)
            if member:
                isbn = input("Enter ISBN of the book to return: ")
                # credits po to aidan for this code :D
                book = next((book for book in books if book.isbn == isbn), None)
                if book:
                    print(f"You have returned {isbn}. \n"
                          f"Thank you!")
                else:
                    print("Sorry, invalid input.")
            else:
                print("Please register as a member first, before returning a book.")

        elif choice == '5':
            print(str(books))

        elif choice == '6':
            print(str(members))

        elif choice == '7':
            for transactions in transactions:
                print(str(transactions))

        elif choice == '8':
            print("Exiting the program... \n"
                  "Thank you for using the Library Management System!")
            break

        else:
            print("Invalid input, \n"
                  "Please try again!")


if __name__ == "__main__":
    main()
