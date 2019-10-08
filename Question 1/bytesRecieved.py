import time
import psutil
import mysql.connector
from mysql.connector import Error
import cryptography


class bytesR:

    global connection
    connection = mysql.connector.connect(host='db',  database='demodbs', user='root',password='root',auth_plugin='mysql_native_password')

    def __init__(self):
        self.bytes_recv = 0 #by default


    def set_bytes_Recieved(self):
        bytse = psutil.net_io_counters(pernic=True)
        newtworks = bytse.keys()
        print(newtworks)
        info = bytse[newtworks[3]]
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

b = bytesR()
b.get_bytes_recieved()
b.close()
