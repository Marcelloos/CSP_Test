import time
import psutil
import mysql.connector
from mysql.connector import Error

global connection
connection = mysql.connector.connect(host='127.0.0.1',  database='statisticsdb', user='pi',password='pi')
class RAM:

    def __init__(self):
        self.percentage = 0 #by default


    def set_Ram_Persentage(self):
        ram = psutil.virtual_memory().percent
        self.percentage = ram
            
    
    def intoDb(self):
        try:
            if(connection.is_connected()):
                print("connected")
            cursor = connection.cursor()
            query ="INSERT INTO ram_usage (ram_usage) VALUES (%s)" 

            var = (self.percentage,)
            
            result = cursor.execute(query,var)
            connection.commit()
            print("Record inserted successfully into ram_usage table")
            cursor.close()

        except mysql.connector.Error as error:
            print("Failed to insert record into ram_usage table {}".format(error))

    def get_Ram_Persentage(self):
        for i in range(40):
            self.set_Ram_Persentage()
            self.intoDb()
            print(self.percentage)
            time.sleep(10)

    def close(self):
        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")

r = RAM()
r.get_Ram_Persentage()
r.close()


