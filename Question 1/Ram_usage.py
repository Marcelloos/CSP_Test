'''
RAM Usage Trakker
Author: Marcell Oosthuizen
This script keeps track of the ram usage of the computer it is running on.
It will measure the data and send it to a my sql database for storage and later use

'''


'''
Imports Used
'''
import time
import psutil
import mysql.connector
from mysql.connector import Error
import cryptography

''' Make a global variable for connection but can be changed to def __init__'''


'''Class of ram '''
class RAM:
    global connection
    connection = mysql.connector.connect(host='db',  database='demodbs', user='root',password='root'auth_plugin='mysql_native_password')

    '''Def init initializes the perce of ram used to 0 as a default'''
    def __init__(self):
        self.percentage = 0 #by default

    '''
    This function retrieves the ram usage and sets the class variable to it
    '''
    def set_Ram_Persentage(self):
        ram = psutil.virtual_memory().percent
        self.percentage = ram
            
    '''This function checks the connection to the database and then inserts the data from the class variable persentage into the database '''
    def intoDb(self):
        try:
            if(connection.is_connected()):
                print("connected")
            cursor = connection.cursor()
            query ="INSERT INTO ram_usage (ram_usage) VALUES (%s)"  # query to insert into the database

            var = (self.percentage,)
            
            result = cursor.execute(query,var) # this executes the query
            connection.commit()
            print("Record inserted successfully into ram_usage table")
            cursor.close()

        except mysql.connector.Error as error:
            print("Failed to insert record into ram_usage table {}".format(error)) #in case of an erroer this messege will be printed

    '''This function is called by other classes but is mainly used to compile the other to functions and is used as a runner function for them'''
    def get_Ram_Persentage(self):
        for i in range(40):
            self.set_Ram_Persentage()
            self.intoDb()
            print(self.percentage)
            time.sleep(10)
    '''This function is used to close the connection to the database'''
    def close(self):
        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")

r = RAM()
r.get_Ram_Persentage()
r.close()
