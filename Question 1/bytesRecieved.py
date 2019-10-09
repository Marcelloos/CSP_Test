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
        self.whatNet = 0
        self.bytes_recv = 0 #by default
    #selects the network interface with the highest byte count to track
    def setNet(self):
        bytse = psutil.net_io_counters(pernic=True)# pulls byte data
        networks = bytse.keys() # gets diffrent connections
        highest = 0
        for i in range(len(networks)):
            if bytse[networks[i]].bytes_recv > bytse[networks[highest]].bytes_recv:
                highest = i
        self.whatNet = highest



    ''' The set bytes Recieved function polls the hardware '''
    def set_bytes_Recieved(self):
        bytse = psutil.net_io_counters(pernic=True)# pulls byte data
        networks = bytse.keys() # gets diffrent connections
        print(networks)
        info = bytse[networks[self.whatNet]] # this selects wifi on my laptop as the connection to track
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
        self.setNet()
        for i in range(10):
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
