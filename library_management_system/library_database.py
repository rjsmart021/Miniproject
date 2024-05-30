import os
from mysql.connector import Error, cursor

import mysql.connector


class LibraryDataBase:

    def __init__(self, port=3306):
        self.connection = None
        self.host = os.environ.get("db_host", default="localhost")
        self.user = os.environ.get("db_user")
        self.port = port
        self.database = os.environ.get("database")
        self.password = os.environ.get("db_password")
        self._database_cursor: cursor = None
        self.connect_to_database()
        print(self.host, self.user, self.password, self.database)

    def set_database_cursor(self):
        """
        Set the database cursor which will execute commands
        :return:
        """
        self._database_cursor = self.connection.cursor()

    def get_database_cursor(self) -> cursor:
        """
        :return: data base cursor
        """
        return self._database_cursor

    def connect_to_database(self):
        """
        establishes the database connection.
        :return: None
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )

            if self.connection.is_connected():
                print("Connected to MYSQl server")
                self.set_database_cursor()

        except mysql.connector.Error as e:
            print("Error Connecting to Data base. Please verify correctly.")
            print(f"Error message: {e.msg}")
            exit(0)

    def execute_query(self, query: str, data):
        """
        This method will execute the sql Query.
        :param query: MySQl query in string format
        :param data: Data for Query
        :return: None
        """
        self._database_cursor.execute(query, data)



