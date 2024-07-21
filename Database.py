# import pymssql
from pymssql import connect

class Database:
    __connection = None
    # def __init__(self):
    #     self.__names = [
    #         {"name": "John", "year": 1915, "gender": "M", "count": 47577},
    #         {"name": "John", "year": 1916, "gender": "M", "count": 50046},
    #         {"name": "John", "year": 1917, "gender": "M", "count": 51851},
    #         {"name": "John", "year": 1918, "gender": "M", "count": 56599},
    #         {"name": "John", "year": 1919, "gender": "M", "count": 53532},
    #     ]


    @classmethod
    def connect(cls):
        if cls.__connection == None:
            cls.__connection = connect(
                server='cisdbss.pcc.edu', 
                user='275student', 
                password='275student', 
                database='NAMES'
            )


    @classmethod
    def readNames(cls, year, gender):
        Database.connect()
        cursor = cls.__connection.cursor()
        sql = """
        SELECT TOP 20 Name, Gender, Year, NameCount
        FROM all_data
        WHERE Year = %s AND Gender = %s;
        """
        cursor.execute(sql, (year, gender))
        rows = cursor.fetchall()
        cls.__connection.close()
        return rows
        
        