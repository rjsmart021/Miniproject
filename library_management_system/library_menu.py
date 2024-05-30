import re

from library_management_system.books_table import Book
from library_management_system.users_table import User
from library_management_system.borrowed_books import BorrowedBooks


class BookOperation:
    def __init__(self):
        self.book_item = Book()
        self.borrowed_book = BorrowedBooks()

    def add_new_book(self):
        """
        This method will read title, isbn and publication date and validates the data and add into book table.
        :return: None
        """
        while True:
            title = input("Enter the title of the book: ")
            isbn = input("Enter the ISBN of the book (must be 13 characters): ")
            if len(isbn) != 13:
                print("ISBN must be 13 characters long. Please try again.")
            else:
                publication_date = input("Enter the publication date of the book: ")
                self.book_item.add_book(title, isbn, publication_date)
                break

    def borrow_a_book(self):
        """
        Add borrowed book entry into BorrowedBooks table.
        Read user id and book id and date of borrowing from the user input.
        :return:
        """
        user_id = input("Enter the user ID: ")
        book_id = input("Enter the book ID: ")
        borrow_date = input("Enter the borrow date: ")
        self.borrowed_book.borrow_book(user_id, book_id, borrow_date)

    def return_a_book(self):
        """
        This will return a book borrowed by the user
        Read ID of the user who returned the book, ID of the book returned and date of return
        :return: None
        """
        user_id = input("Enter the user ID: ")
        book_id = input("Enter the book ID: ")
        return_date = input("Enter the return date: ")
        self.borrowed_book.return_book(user_id, book_id, return_date)

    def search_for_a_book(self):
        """
        This method will search for a book by reading title from the user input.
        :return: None
        """
        title = input("Enter the title of the book: ")
        self.book_item.search_book_by_tittle(title)

    def display_all_books(self):
        """
        Display all the book entries in the books table
        :return: None
        """
        self.book_item.show_all_books()


class UserOperation:
    def __init__(self):
        self.user_item = User()

    def add_new_user(self):
        """
        Add new user entry into user table.
        Read the following user inputs:
        1. username
        2. email in the format email_name@daomain.com. if incorrect email format is entered user is
        asked to enter again
        :return: None
        """
        name = input("Enter user name: ")
        email = input("Enter user email: ")

        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        while not re.match(email_pattern, email):
            print("Invalid email format.")
            email = input("Enter a valid user email: ")
        self.user_item.register_user(name, email)

    def view_user_details(self):
        """
        This method is used to view the details fo a user based on the user_id.
        :return: None
        """
        user_id = input("Enter user ID: ")
        user_details = self.user_item.get_user_by_id(user_id)[0]
        if user_details:
            print("User details:")
            print(f"ID: {user_details[0]}")
            print(f"Name: {user_details[1]}")
            print(f"Email: {user_details[2]}")

    def display_all_users(self):
        """
        Display all the user entries in the user table.
        :return: None
        """
        self.user_item.show_all_users()


def get_main_menu():
    print("Welcome to library Management system main Menu: ")
    main_menu = """
        Main Menu:
        1. Book Operations
        2. User Operations
        3. Quit
        """
    return main_menu


def get_book_operation_menu():
    print("********************************************************************************")
    print("                        Welcome to Book operations Menu:                        ")
    print("********************************************************************************")
    book_operations_menu = """
        Book Operations:
        1. Add a new book
        2. Borrow a book
        3. Return a book
        4. Search for a book
        5. Display all books
        6. Return to Main Menu
        """
    return book_operations_menu


def get_user_operation_menu():
    print("********************************************************************************")
    print("                        Welcome to User operations Menu:                        ")
    print("********************************************************************************")
    user_operations_menu = """
        User Operations:
        1. Add a new user
        2. View user details
        3. Display all users
        4. Return to main menu
        """
    return user_operations_menu


# Main program loop
if __name__ == "__main__":
    menu_option = -1

    while menu_option != 3:
        print(get_main_menu())
        try:
            menu_option = int(input("Enter Main Menu Option (enter numbers between 1 to 3: "))
            if not 1 <= menu_option <= 3:
                print("Invalid menu option. Please enter number between 1 to 3.")
        except ValueError:
            print("Incorrect value provided. Please enter numbers between 1 to 3.")

        if menu_option == 1:
            book_operation = BookOperation()
            book_menu_option = -1

            while book_menu_option != 6:
                print(get_book_operation_menu())
                try:
                    book_menu_option = int(
                        input("Enter Book Menu Option (enter numbers between 1 to 6: "))
                    if not 1 <= book_menu_option <= 6:
                        print("Invalid menu option. Please enter number between 1 to 6.")

                    if book_menu_option == 1:
                        book_operation.add_new_book()
                    elif book_menu_option == 2:
                        book_operation.borrow_a_book()
                    elif book_menu_option == 3:
                        book_operation.return_a_book()
                    elif book_menu_option == 4:
                        book_operation.search_for_a_book()
                    elif book_menu_option == 5:
                        book_operation.display_all_books()

                except ValueError:
                    print("Incorrect value provided. Please enter numbers between 1 to 3.")

        elif menu_option == 2:
            user_operation = UserOperation()
            user_menu_option = -1

            while user_menu_option != 4:
                print(get_user_operation_menu())
                try:
                    user_menu_option = int(
                        input("Enter Book Menu Option (enter numbers between 1 to 4: "))
                    if not 1 <= user_menu_option <= 4:
                        print("Invalid menu option. Please enter number between 1 to 6.")

                    if user_menu_option == 1:
                        user_operation.add_new_user()
                    elif user_menu_option == 2:
                        user_operation.view_user_details()
                    elif user_menu_option == 3:
                        user_operation.display_all_users()

                except ValueError:
                    print("Incorrect value provided. Please enter numbers between 1 to 3.")
