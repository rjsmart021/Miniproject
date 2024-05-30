from tabulate import tabulate
from mysql.connector import Error
from library_management_system.library_database import LibraryDataBase


class User(LibraryDataBase):
    def register_user(self, name, email):
        """
        This method will register a user based on inputs.
        :param name: username to add
        :param email: user email address to register
        :return:
        """
        try:
            select_query = "SELECT COUNT(*) FROM users WHERE email=%s"
            self.execute_query(select_query, (email,))
            count = self._database_cursor.fetchone()[0]

            if count > 0:
                print("User already exists with the email:", email)
            else:
                insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
                user_data = (name, email)
                self.execute_query(insert_query, user_data)
                self.connection.commit()
                print("User registered successfully!")
        except Error as e:
            print(f"Error While registering user. Error message: {e}")

    def show_all_users(self):
        """
        This method will display all the users registered in the library.
        :return: None
        """
        try:
            search_query = "SELECT * FROM users"
            self.execute_query(search_query, ())
            results = self._database_cursor.fetchall()
            if len(results) == 0:
                print("No users are present in the users table")
            else:
                headers = ['id', 'name', 'email']
                print(tabulate(results, headers))
        except Error as e:
            print(f"Error in fetching all users. Error message: {e}")

    def get_user_by_id(self, user_id):
        """
        It will search for a user with giver user_id in users table.
        Display No users if user not found
        :param user_id: ID of the user to search
        :return: User details. List of tuples. Each tuple will have user_id,name and email
        """
        try:
            search_query = "SELECT * FROM users where id=%s"
            user_data = (user_id,)

            self.execute_query(search_query, user_data)

            results = self._database_cursor.fetchall()
            if len(results) == 0:
                print(
                    f"No users are present in the users table with given user id: {user_id}")
                return None
            else:
                return results

        except Error as e:
            print(f"Error while searching for user with ID: {user_id}.", end=' ')
            print(f"Error message: {e}")

    def get_user_by_name(self, name):
        try:
            search_query = "SELECT * FROM users where name=%s"
            user_data = (name,)

            self.execute_query(search_query, user_data)

            results = self._database_cursor.fetchall()
            if len(results) == 0:
                print(
                    f"No users are present in the users table with given user name: {name}")
                return None
            else:
                return results

        except Error as e:
            print("Error while searching for user", end=" ")
            print(f"Error message: {e}")


