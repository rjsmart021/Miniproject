from library_management_system.library_database import LibraryDataBase
from library_management_system.users_table import User
from mysql.connector import Error
from library_management_system.books_table import Book


class BorrowedBooks(LibraryDataBase):
    def borrow_book(self, user_id, book_id, borrow_date):
        """
        This method will add entry fot the borrowed book. And update the availability to 0.
        Handles necessary exceptions which violated database integrity.
        :param user_id: user id who borrows book from library
        :param book_id: ID of the book which is borrowed
        :param borrow_date: Date of borrowing
        :return: None
        """
        print("Borrowed book: ", user_id, book_id)
        try:

            if User().get_user_by_id(user_id) is None:
                print(f"No User found with ID: {user_id}")
                return
            elif Book().get_book_by_id(book_id) is None:
                print(f"No book found with ID: {book_id}")
                return
            update_query = "UPDATE books SET availability = 0 WHERE id = %s"
            self.execute_query(update_query, (book_id,))

            insert_query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
            borrowed_data = (user_id, book_id, borrow_date)
            self.execute_query(insert_query, borrowed_data)

            self.connection.commit()
            print("Book borrowed successfully!")
        except Error as e:
            print(f"Error occurred while borrowing the book. Error Message: {e}")

    def return_book(self, user_id, book_id, return_date):
        """
        This method will update the availability of returned book to 1 and add entry of date of return.
        Handles necessary exceptions which violated database integrity.
        :param user_id: ID of the user who returns the book
        :param book_id: ID of the book which is returned
        :param return_date: Date of return
        :return:
        """
        try:
            if User().get_user_by_id(user_id) is None:
                print(f"No User found with ID: {user_id}")
                return
            elif Book().get_book_by_id(book_id) is None:
                print(f"No book found with ID: {book_id}")
                return
            update_query = "UPDATE books SET availability = 1 WHERE id = %s"
            self.execute_query(update_query, (book_id,))

            update_query = "UPDATE borrowed_books SET return_date = %s WHERE user_id = %s AND book_id = %s"
            return_data = (return_date, user_id, book_id)
            self.execute_query(update_query, return_data)

            self.connection.commit()
            print("Book returned successfully!")
        except Error as e:
            print(f"Error occurred while borrowing the book. Error Message: {e}")

