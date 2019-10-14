'''Author :  Marcell Oosthuizen
   email : oosthuizenmarcell@gmail.com
   CSP Question 2
'''

import cryptography
from flask import Flask, request , render_template
from flaskext.mysql import MySQL
import time
import psutil
import mysql.connector
from datetime import datetime
#from scapy.all import *



app = Flask(__name__)

'''The below code will configure the database by supplying the information that is needed.
'''

'''
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'servers'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'demodbs'
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['PORT']='3306'
app.config['AUTH_plugin']='mysql_native_password')
mysql.init_app(app)
'''

config = {
	'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'demodbs',
	'auth_plugin':'mysql_native_password'
	}

'''The below code is used to act as flags in controlling the services. They are used by both the stopAll and restetAll function.
The way that they work is simply having the
'''
cpu_flag = True
ram_flag = True
bytes_flag = True
temp_flag = True
packet_flag = True

@app.route('/')
def home():
    return render_template("home.html")



@app.route('/temp', methods=["POST"])  # if the user types in past the server  and port ip / temp this process will start


def addTemp():
    '''This method works out the tempreture given the amount of seconds that passed that day ,
    this uses a parabola function with the max temprature of 25 and a min of 0 degrees celsius.
    after a tempreture is found an id statement will check whether its 1 or more degrees higher than the last tempreture pushed to the database.
    If it is then it will push the tempreture to the data base, else it will just wait 10 seconds and then run again.
    '''
    global temp_flag , config
    conn = mysql.connector.connect(**config)
    last = 0
    while temp_flag:
        now = datetime.now()
        sec_passed= -43200+(now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds() # works out the seconds passed so far on the day
        temp =-1*(0.00000001368093*(sec_passed*sec_passed))  #use a quadratic equation to work out the tempreture
        temp = int(temp-(-25.533))
        if (temp-last >= 1):
            cursor = conn.cursor()
            query ="INSERT INTO tempreture (curr_tempreture) VALUES (%s)" #query to insert into the database
            var = (temp,)
            result = cursor.execute(query,var)
            conn.commit()
            print("Record inserted successfully into tempreture table")
            last = temp
        else:
            time.sleep(10) # since tempreture will change slowly I set a 10 timer for it to not constantly check
    return 'This service cant run now , please use the reset all command : /reset all'


@app.route('/cpu', methods=["POST"]) # if the user types in past the server  and port ip /cpu this process will start

def addCpuU():
    '''
    This method cecks the average cpu usage every 0.5 seconds. This is done by polling all the cores of the cpu and getting the average over them.
    The data will then be commited to the database
    '''
    global cpu_flag,config
    conn = mysql.connector.connect(**config)
    while cpu_flag:
        cpus = psutil.cpu_percent(interval=0.5, percpu=True) #reurns list of cpu's which is your cores and each of their usage
        avg = 0
        for i in cpus:
            avg = avg + i
        percentage = avg/len(cpus)  #get the avrage usage over all the cpu cores
        cursor = conn.cursor()
        query ="INSERT INTO cpu_usage (cpu_per) VALUES (%s)"

        var = (percentage,)

        result = cursor.execute(query,var)#execution of the sql query
        conn.commit()
        print("Record inserted successfully into cpu table")
        time.sleep(0.5)
    return 'This service cant run now , please use the reset all command : /reset all'

@app.route('/ram', methods=["POST"]) # if the user types in past the server  ip  and port /Ram this process will start

def RamUSage():
    '''
    This method will check the percentage of RAM that is in use and submit this data to the database every 10 seconds since it is a less important function.
    '''
    global ram_flag,config
    while ram_flag:
        conn = mysql.connector.connect(**config)
        ram = psutil.virtual_memory().percent #retrieve percentage of used ram
        cursor = conn.cursor()
        query ="INSERT INTO ram_usage (ram_usage) VALUES (%s)"
        var = (ram,) #creating a tuple
        result = cursor.execute(query,var)
        conn.commit()
        print("Record inserted successfully into ram_usage table")
        time.sleep(10)
    return 'This service cant run now , please use the reset all command : /reset all'


@app.route('/bytes', methods=["POST"])
def BytesRec(): # if the user types in past the server  and port ip /bytes this process will start
    '''
    This method checks the amount of bytes that is recieved by one of the network interfaces and is then commited to the database ever second
    '''
    global bytes_flag,config
    bytse = psutil.net_io_counters(pernic=True)
    networks = list(bytse.keys())   # get a array of the network interfaces
    highest = 0
    for i in range(len(networks)):
    	if bytse[networks[i]].bytes_recv > bytse[networks[highest]].bytes_recv:
        	highest = i

    while bytes_flag:
        conn = mysql.connector.connect(**config)
        bytse = psutil.net_io_counters(pernic=True)
        networks = list(bytse.keys())   # get a array of the network interfaces
        info = bytse[networks[highest]] #[3]for wifi on my machine and [6] for internet
        bytes_recv = info.bytes_recv #get the bytes recieved from your selected network interface
        cursor = conn.cursor()
        query ="INSERT INTO bytes_recv (total_bytes) VALUES (%s)"

        var = (bytes_recv,)

        result = cursor.execute(query,var)
        conn.commit()
        print("Record inserted successfully into bytes_recv table")
        time.sleep(1)
    return 'This service cant run now , please use the reset all command : /reset all'

@app.route('/stop all')
def stopAll():
    '''
    This function is used to stop all the runnin processes on this server. This is done by setting their running condition to false
    '''
    global cpu_flag,ram_flag,bytes_flag,temp_flag
    cpu_flag = False
    bytes_flag = False
    ram_flag = False
    temp_flag = False
    return "<h1>All processes have been stopped</h1>"

@app.route('/reset all')

def resetAll():
    '''
    This function is used to rest the running conditions for all of the processes on this server. This is done by setting their running condition to true.
    You need to run this statement before attempting to restart any of the processes that "you used stop all" to stop.
    '''
    global cpu_flag,ram_flag,bytes_flag,temp_flag
    cpu_flag = True
    bytes_flag = True
    ram_flag = True
    temp_flag = True
    return "<h1>All processes have been reset, restart them by typing in their routes</h1>"





if __name__ == '__main__':
    app.run(host='0.0.0.0' port=5000 debug=true)
