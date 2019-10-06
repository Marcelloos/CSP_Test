'''
Tempreture tracker 
Author: Marcell Oosthuizen
This script keeps track of the tempreture 
It utilises a quadratic equation to workout the tempreture

'''


'''These are the imports used within the program'''
import time
import psutil
import mysql.connector
from mysql.connector import Error
from datetime import datetime

'''This is the class for tempreture'''
class TEMP:
    '''Makes a global variable for this class to use'''
    global connection
    connection = mysql.connector.connect(host='127.0.0.1',  database='statisticsdb', user='pi',password='pi')
    
    '''This initiazation function sets the default temp to 0 as well as it declares 0 for the last variable'
    The last variable is used to keep track of the last input into the DB
    '''
    def __init__(self):
        self.temp = 0 #by default
        self.last = 0

    '''This function uses a quadratic equation to workout the tempreture at a certain time of day
    This function assumes that the max tempreture is 25 and that the time of day that the tempreture is the highest is 12 o'clock 
    It all so asumes that the the time of the lowest tempreture is 12 o'clock at night
    '''
    def set_tempreture(self):
        now = datetime.now()
        sec_passed= -43200+(now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds() # works out the seconds passed so far on the day
        temps =-1*(0.00000001368093*(sec_passed*sec_passed))  #use a quadratic equation to work out the tempreture 
        temps = int(temps-(-25.533))
        self.temp = temps

            
    '''This function checks the connection to the database and then inserts the data from the class variable persentage into the database '''
    def intoDb(self):
        if (self.temp - self.last >= 1):
            try:
                if(connection.is_connected()):
                    print("connected")
                cursor = connection.cursor()
                query ="INSERT INTO tempreture (curr_tempreture) VALUES (%s)" 

                var = (self.temp,)
                
                result = cursor.execute(query,var)
                connection.commit()
                print("Record inserted successfully into temp table")
                cursor.close()
                self.last= self.temp

            except mysql.connector.Error as error:
                print("Failed to insert record into temp table {}".format(error))
                
        else:
            time.sleep(10) #executes every ten seconds 
        
    '''
    This function is seen as a runner function for the program and is mostly called by other classes
    This functon will make calls to the set_tempreture function and the intoDb function
    '''    
    def get_temp(self):
        for i in range(90):# runs for 90 iterations
            self.set_tempreture()
            self.intoDb()
            print(self.temp)
    '''This function is used to close the connection to the database'''        
    def close(self):
        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")
t = TEMP()
t.get_temp()
t.close()