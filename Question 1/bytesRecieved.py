'''
CPU Usage tracker 
Author: Marcell Oosthuizen
This script keeps track of the CPU Usage 
It utilises a quadratic equation to workout the CPU Usage

'''


'''These are the imports used within the program'''
import time
import psutil
import mysql.connector
from mysql.connector import Error
import cryptography


'''This is the class for CPU Usage'''
class bytesR:
    '''Def init initializes the perce of ram used to 0 as a default'''
    global connection
    connection = mysql.connector.connect(host='db',  database='demodbs', user='root',password='root',auth_plugin='mysql_native_password')

    def __init__(self):
        self.bytes_recv = 0 #by default

    ''' The set bytes Recieved function polls the hardware '''
    def set_bytes_Recieved(self):
        bytse = psutil.net_io_counters(pernic=True)# pulls byte data
        newtworks = bytse.keys() # gets diffrent connections 
        print(newtworks)
        info = bytse[newtworks[3]] # this selects wifi on my laptop as the connection to track 
        self.bytes_recv = info.bytes_recv


    def intoDb(self):
        try:
            if(connection.is_connected()):
                print("connected")
            cursor = connection.cursor()
            query ="INSERT INTO bytes_recv (total_bytes) VALUES (%s)"

            var = (self.bytes_recv,)

            result = cursor.execute(query,var)
            connection.commit()
            print("Record inserted successfully into bytes_recv table")
            cursor.close()

        except mysql.connector.Error as error:
            print("Failed to insert record into bytes_recv table {}".format(error))

    '''
    This function just functions as the run function that is called by external processes from other files
    Since bytes recieved data is important it polls after each 1 seconds 
    Calls both functions : set_bytes_Recieved
                         : intoDb
    '''
    def get_bytes_recieved(self):
        for i in range(400):
            self.set_bytes_Recieved()
            self.intoDb()
            print(self.bytes_recv)
            time.sleep(1)
    def close(self):
        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")

'''This code was used to test each part of the code seperately'''
b = bytesR()
b.get_bytes_recieved()
b.close()
