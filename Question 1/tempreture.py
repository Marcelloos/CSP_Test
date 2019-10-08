import time
import psutil
import mysql.connector
from mysql.connector import Error
from datetime import datetime


class TEMP:

    global connection
    connection = mysql.connector.connect(host='db',  database='demodbs', user='root',password='root',auth_plugin='mysql_native_password')

    def __init__(self):
        self.temp = 0 #by default
        self.last = 0


    def set_tempreture(self):
        now = datetime.now()
        sec_passed= -43200+(now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds() # works out the seconds passed so far on the day
        temps =-1*(0.00000001368093*(sec_passed*sec_passed))  #use a quadratic equation to work out the tempreture 
        temps = int(temps-(-25.533))
        self.temp = temps

            
    
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
            time.sleep(10)

    def get_temp(self):
        for i in range(90):
            self.set_tempreture()
            self.intoDb()
            print(self.temp)
            
    def close(self):
        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")
t = TEMP()
t.get_temp()
t.close()
