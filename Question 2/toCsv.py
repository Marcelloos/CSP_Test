# requirement: python-mysqldb

import mysql.connector
import sys
import csv
from datetime import datetime

QUERY="SELECT time_stamp FROM statisticsdb.bytes_recv ORDER BY time_stamp ASC LIMIT 1"
connection = mysql.connector.connect(host='127.0.0.1',  database='statisticsdb', user='pi',password='pi')
cur=connection.cursor()
cur.execute(QUERY)
result=cur.fetchall()
print(type(result))
fan = result[0]
fan = fan[0]
print(fan.minute)
a = datetime(fan.year, fan.month, fan.day, fan.hour, fan.minute +5, fan.second, fan.microsecond)
print(a)
b = a.strftime("%Y-%m-%d %H:%M:%S")


#select * from the_table where timestamp_column <= timestamp '2014-03-25 14:00:00' - interval '5' minute;

aq = (b,)

cur.execute("SELECT * FROM statisticsdb.bytes_recv WHERE time_stamp <= '%s'" % aq)
result=cur.fetchall()
#print(result)
arr = ["ID","Percentage","time_stamp"]
c = csv.writer(open('bytes_recv.csv', 'wb'))
c.writerow(arr)
for x in result:
    c.writerow(x)
    
    
