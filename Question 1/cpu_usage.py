'''
CPU Usage tracker 
Author: Marcell Oosthuizen
This script keeps track of the CPU Usage 
It utilises a quadratic equation to workout the CPU Usage

'''


'''These are the imports used within the program'''
import psutil
import time
import mysql.connector
from mysql.connector import Error



'''This is the class for CPU Usage'''
class CPU:
    '''Def init initializes the perce of ram used to 0 as a default'''
    global connection
    connection = mysql.connector.connect(host='127.0.0.1',  database='statisticsdb', user='pi',password='pi')
    def __init__(self):
        self.percentage = 0 #by default

    '''This function polls the hardware to find the perce of cpu usage.
       This takes into account all the cores of the cpu and will take the average of the amount of cpu cores the cpu has.
    '''
    def set_Cpu_Persentage(self):
        cpus = psutil.cpu_percent(interval=0.5, percpu=True)
        avg = 0
        for i in cpus: # run through all the cores
            avg = avg + i # adds up the amounts into a variable avg
        self.percentage = avg/len(cpus)  # sets the object's percentage variable to the average
            

    '''This function checks the connection to the database and then inserts the data from the class variable persentage into the database '''
    def intoDb(self):
        try:
            if(connection.is_connected()):
                print("connected")
            cursor = connection.cursor()
            query ="INSERT INTO cpu_usage (cpu_per) VALUES (%s)" 

            var = (self.percentage,)
            
            result = cursor.execute(query,var)
            connection.commit()
            print("Record inserted successfully into cpu_usage table")
            cursor.close()

        except mysql.connector.Error as error:
            print("Failed to insert record into cpuusage table {}".format(error))
    '''
    This function just functions as the run function that is called by external processes from other files
    Since cpu data is important it polls after each 0.5 seconds 
    Calls both functions : set_Cpu_Persentage
                         : intoDb
    '''
    def get_Cpu_Persentage(self):
        for i in range(900):
            self.set_Cpu_Persentage()
            self.intoDb()
            print(self.percentage)
            time.sleep(0.5)
            
    def close(self):
        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")


'''This code was used to test each part of the code seperately'''
s = CPU()
s.get_Cpu_Persentage()    
s.close()


