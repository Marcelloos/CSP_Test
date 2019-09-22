import time
import psutil
import mysql.connector
from mysql.connector import Error



cpus = psutil.cpu_percent(interval=0.5, percpu=True)
avg = 0
for i in cpus:
    avg = avg + i 
self.percentage = avg/len(cpus)

ram = psutil.virtual_memory().percent
self.percentage = ram