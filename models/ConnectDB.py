import mysql.connector
import colorama

colorama.init(autoreset=True)

class ConnectDB:
    def __init__(self) -> None:

        credentials = {}

        try:
            with open("Credentials","r") as f:
                lines = f.read().splitlines()
                for line in lines:
                    dkey, dvalue = line.split("=")
                    credentials.update({dkey: dvalue})
        except FileNotFoundError:
            exit(colorama.Back.RED+"arquivo 'Credentials' não exite!!")

        self.connection = mysql.connector.connect(**credentials)

        self.cursor = self.connection.cursor()

    def queryRaw(self, query, dataTuple=None):
        self.cursor.execute(query, dataTuple)
        self.connection.commit()

    def insert(self, table, **kwargs):
        if kwargs.__len__() > 0:
            query = f"INSERT INTO {table} ("
            for keyName in kwargs:
                query += keyName+","
            query = query[:-1] + ") VALUES ("
            
            for i in range(kwargs.__len__()):
                query += "%s,"
            query = query[:-1] + ");"
        else:
            print("Precisa de kwargs para fucionar")

        self.cursor.execute(query,tuple(kwargs.values()))
        self.connection.commit()

    def remove(self, table, **kwargs):
        if kwargs.__len__() > 0:
            query = f"DELETE FROM {table} WHERE "
            for keyName in kwargs:
                query += f"{keyName}=%s AND "
            query = query[:-5] + ";"
            
            self.cursor.execute(query,tuple(kwargs.values()))
            self.connection.commit()

        else:
            print("Precisa de kwargs para fucionar")

    def search(self, table, **kwargs):
        if kwargs.__len__() > 0:
            query = f"SELECT * FROM {table} WHERE "
            for keyName in kwargs:
                query += f"{keyName}=%s AND "
            query = query[:-5] + ";"
            
            self.cursor.execute(query,tuple(kwargs.values()))
            self.connection.commit()

            return self.cursor.fetchall()

        else:
            print("Precisa de kwargs para fucionar")
            return False

    def getAllAdded(self,table):
        query = f"SELECT * FROM {table} ORDER BY time"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getMostlyRecentAdded(self, table):
        query = f"SELECT * FROM {table} ORDER BY time DESC LIMIT 1;"
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def __del__(self) -> None:
        self.connection.close()
