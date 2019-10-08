import psutil
import time
import mysql.connector
from mysql.connector import Error
import cryptography

global connection
connection = mysql.connector.connect(host='db',  database='demodbs', user='root',password='root',auth_plugin='mysql_native_password')
class CPU:

    def __init__(self):
        self.percentage = 0 #by default


    def set_Cpu_Persentage(self):
        cpus = psutil.cpu_percent(interval=0.5, percpu=True)
        avg = 0
        for i in cpus:
            avg = avg + i
        self.percentage = avg/len(cpus)



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

s = CPU()
s.get_Cpu_Persentage()
s.close()
