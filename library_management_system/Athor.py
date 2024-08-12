from mysql.connector import Error

from library_management_system.library_database import LibraryDataBase
from tabulate import tabulate


class Authors(LibraryDataBase):

    def add_author(Name, writing_genre, Age):

        try:
            select_query = "select count(*) from Authors where Name=%s"
            self.execute_query(select_query, (Name))
            count = self._database_cursor.fetchone()[0]
            # Books writen availability = int(availability)
            if count > 0:
                print("Authors  already existed.")
            else:
                insert_query = "INSERT INTO Authors (Name, writing_genre, Age) VALUES (%s, %s, %s, %s)"
                Author_data = (Name, writing_genre, Age)
                self.execute_query(insert_query, Author_data)
                self.connection.commit()
                print("Athor added successfully!")
        except Error as e:
            print(f"Error While adding athor. Error Message: {e}")

    def search_Author_by_Name(Name, writing_genre, Age: str):

        try:
            search_query = f'select * from Athors where Name=%s'
            self.execute_query(search_query, (Name,))

            results = self._database_cursor.fetchall()

            print(results)

        except Error as e:
            print(f"Error in searching Athor with Name {Name}. Please refer the error: {e}")

    def get_Athor_by_Name(Writing_genre, Name):
        try:
            search_query = "SELECT * FROM Athor WHERE Name = %s"
            self.execute_query(search_query, (Name,))
            result = self._database_cursor.fetchone()

            if result is None:
                print(f"No Athor found with the Name: {Name}")
                return None
            else:
                return result
        except Error as e:
            print(f"Error while getting Athor by Name: {Name}")
            print(f"Error message: {e}")

    def show_all_Athor(self):

        try:
            search_query = f'select * from Athor'
            self.execute_query(search_query, ())
            results = self._database_cursor.fetchall()
            if len(results) == 0:
                print("No books are present in Athor table")
            else:
                headers = ['Name', 'writing_genre', 'Age']
                print(tabulate(results, headers))

        except Error as e:
            print(f"Error in fetching all athor. Error message: {e}")