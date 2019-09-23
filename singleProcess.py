import time
import psutil
import mysql.connector
from mysql.connector import Error


class singleP()
    
    
        
    def __init__(self):
    
        self.cpu_perc = 0
        self.ram_perc = 0
        self.bytese_recv = 0
        
    def gatherData(self):
    
        #get cpu usage data
        cpus = psutil.cpu_percent(interval=0.5, percpu=True)
        avg = 0
        for i in cpus:
            avg = avg + i 
        self.cpu_perc = avg/len(cpus)
        
        #get ram percentage used
        ram = psutil.virtual_memory().percent
        self.ram_perc = ram
        
        #get the amount of bytes 
        bytse = psutil.net_io_counters(pernic=True)
        newtworks = bytse.keys()
        info = bytse[newtworks[1]]
        self.bytese_recv = info.bytes_recv
        
    def toDB(self):
        connection = mysql.connector.connect(host='127.0.0.1',  database='statisticsdb', user='pi',password='pi')
    
        
        
        
        
        