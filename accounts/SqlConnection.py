import mysql.connector
from mysql.connector import errorcode


class SqlConnetion:
    config = {'user': 'root',
              'password': '1234',
              'host': '127.0.0.1',
              'port': 3307,
              'autocommit': True}

    def __init__(self, database='accounts'):
        self.config['database'] = database
        self.connector = self.connection()

    def connection(self):
        try:
            connector = mysql.connector.connect(**self.config)
            if connector.is_connected():
                return connector
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        # else:
        #     self.connector.close()

    def select(self):
        cursor = self.connector.cursor()
        query = "SELECT * FROM accounts.accounts"
        cursor.execute(query)
        for id in cursor:
            print(id)
        cursor.close()

    def execute(self, add_account, date_account=None):
        cursor = self.connector.cursor()
        cursor.execute(add_account, date_account)
        result = cursor
        # cursor.close()
        return result
