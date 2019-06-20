import atexit
import sqlite3


class Person:
    def __init__(self):
        self.conn = sqlite3.connect("my_test_database.db")
        atexit.register(self.cleanup)

    def cleanup(self):
        self.conn.close()

    def typename(self,x): 
        return type(x).__name__

    def create(self,insertDictionary):
        cur = self.conn.cursor()
        columns = [i[1] for i in cur.execute('PRAGMA table_info('+self.typename(self)+')')]
        
        insertString = ""
        valueString = ""
        for col in insertDictionary.keys():
            if col != "primary_key":
                insertString += col+","
                valueString += "'"+insertDictionary[col]+"',"
        
        insertString = insertString[:-1]
        valueString = valueString[:-1]

        finalString = "INSERT INTO "+self.typename(self)+ "("+insertString+") VALUES ("+valueString+")"
        print("finalString == "+finalString)
        cur.execute(finalString) 
        self.conn.commit() 
