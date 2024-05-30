from mysql.connector import Error

from library_management_system.library_database import LibraryDataBase
from tabulate import tabulate


class Book(LibraryDataBase):

    def add_book(self, title, isbn, publication_date, availability=True):

        try:
            select_query = "select count(*) from books where isbn=%s"
            self.execute_query(select_query, (isbn,))
            count = self._database_cursor.fetchone()[0]
            # availability = int(availability)
            if count > 0:
                print("Book already existed.")
            else:
                insert_query = "INSERT INTO books (title, isbn, publication_date, availability) VALUES (%s, %s, %s, %s)"
                book_data = (title, isbn, publication_date, availability)
                self.execute_query(insert_query, book_data)
                self.connection.commit()
                print("Book added successfully!")
        except Error as e:
            print(f"Error While adding book. Error Message: {e}")

    def search_book_by_tittle(self, title: str):

        try:
            search_query = f'select * from books where title=%s'
            self.execute_query(search_query, (title,))

            results = self._database_cursor.fetchall()

            print(results)

        except Error as e:
            print(f"Error in searching books with title {title}. Please refer the error: {e}")

    def get_book_by_id(self, book_id):
        try:
            search_query = "SELECT * FROM books WHERE id = %s"
            self.execute_query(search_query, (book_id,))
            result = self._database_cursor.fetchone()

            if result is None:
                print(f"No book found with the ID: {book_id}")
                return None
            else:
                return result
        except Error as e:
            print(f"Error while getting book by ID: {book_id}")
            print(f"Error message: {e}")

    def show_all_books(self):

        try:
            search_query = f'select * from books'
            self.execute_query(search_query, ())
            results = self._database_cursor.fetchall()
            if len(results) == 0:
                print("No books are present in books table")
            else:
                headers = ['id', 'title', 'publication date', 'isbn', 'availability']
                print(tabulate(results, headers))

        except Error as e:
            print(f"Error in fetching all books. Error message: {e}")
