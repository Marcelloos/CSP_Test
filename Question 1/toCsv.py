# requirement: python-mysqldb

import mysql.connector
import sys
import csv
from datetime import datetime

QUERY="SELECT time_stamp FROM statisticsdb.ram_usage ORDER BY time_stamp ASC LIMIT 1"
connection = mysql.connector.connect(host='db',  database='demodbs', user='root',password='root')
cur=connection.cursor()
cur.execute(QUERY)
result=cur.fetchall()
print(type(result))
fan = result[0]
fan = fan[0]
print(fan.minute)
if (fan.minute < 55):  #tests the boaderline case of when adding the next five minutes will result in being more than 60 minutes
    a = datetime(fan.year, fan.month, fan.day, fan.hour, fan.minute +5, fan.second, fan.microsecond)
    print(a)
    b = a.strftime("%Y-%m-%d %H:%M:%S")

else:
    c = (fan.minute + 5)- 60
    a = datetime(fan.year, fan.month, fan.day, fan.hour + 1, fan.minute + c, fan.second, fan.microsecond)
    print(a)
    b = a.strftime("%Y-%m-%d %H:%M:%S")


#select * from the_table where timestamp_column <= timestamp '2014-03-25 14:00:00' - interval '5' minute;

aq = (b,) #makes a tuple

cur.execute("SELECT * FROM statisticsdb.ram_usage WHERE time_stamp <= '%s'" % aq)
result=cur.fetchall()
#print(result)
arr = ["ID","ram_usege","time_stamp"]
c = csv.writer(open('ram_usage.csv', 'wb'))          # pipes data to a csv file and creates it if not yet created
c.writerow(arr)
for x in result:
    c.writerow(x)
