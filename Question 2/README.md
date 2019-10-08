# CSP_Test
This ReadMe is for the CSP test
-------------------------------


IMPORTANT: Data Base set up
----------------------------
To set up the data base you need to use the following sql queries to create the databases.
I used msql workbench to monitor and manage the database.
The database is dockerized for both of the Questions so no initialization is needed. All that needed to be done is to install docker and docker compose on the machine then navigate to the directiory that has the docker compose file for either question 1 or 2 given which one you want to run.

To view database in mysql workbench :
        
    --> Open a new terminal instance and type in 'docker ps' to view the running containers
    --> Find the database container for this program it will look like : question1_db_1
    --> Then type in to the terminal 'docker inspect question1_db_1'
    --> Then close to the bottom find the IPv4 adress and use it as the host address in Mysql workbench
    --> Use root as user and root as password




bytes_recv Table
---------------------------
CREATE TABLE `bytes_recv` (
  `idbytes_recv` int(11) NOT NULL AUTO_INCREMENT,
  `total_bytes` int(11) NOT NULL,
  `time_stamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idbytes_recv`)
) 


cpu_usage Table
----------------
CREATE TABLE `cpu_usage` (
  `id_cpu_usage` int(11) NOT NULL AUTO_INCREMENT,
  `cpu_per` float NOT NULL,
  `time_stamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_cpu_usage`)
) 


packet_lenght Table
-------------------
CREATE TABLE `packet_lenght` (
  `idpacket_lenght` int(11) NOT NULL AUTO_INCREMENT,
  `packet_len` int(11) DEFAULT NULL,
  `time_stamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idpacket_lenght`)
) 

ram_usage Table
----------------
CREATE TABLE `ram_usage` (
  `idram_usage` int(11) NOT NULL AUTO_INCREMENT,
  `ram_usage` float NOT NULL,
  `time_stamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idram_usage`)
) 

tempreture Table
-----------------
CREATE TABLE `tempreture` (
  `idtempreture` int(11) NOT NULL AUTO_INCREMENT,
  `curr_tempreture` int(11) NOT NULL,
  `time_stamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idtempreture`)
) 


Question 1
------------------
For this question I tried to implement a single python file that pulls methods from other files I created and use threading to run them together. I used the psutil module to retrieve the data that is needed from the server, further more I used 4 tabels to store the data since I have not yet added the packet lenght service. The questions script has been fully containerized using docker and only needs to be run by using the docker compose up command(or build and run). Issues I have with this implementation is the fact that it is not running in parralal but actually its running sequeantialy so in that sence I failed at using multithreading correctly. this thou will be something I will look into further to fully understand the multythreading module and how to use it.

The Breakdown
--------------
This script is broken down into 4 seprate files a and then called by a single file (ironicly named single.py) each file is used and a instance is made within the single.py file: 

          --> cpu_usage.py
          --> Ram_usage.py
          --> bytesRecieved.py
          --> tempreture.py

As stated these files have their own dedicated fucntions and is used by the single.py file. 

The Requirements
-----------------
With the first version I did not used docker at all since I had some issues with it , but through alot of research and bug testing I got it working. Now the requirements of each of the two containers is handeled by docker meaning you do not have to manualy install any of the requirements of this service. The docker-compose.yaml  handels most of the setting up that needs to be done. 
Below is a list of dependencies that are handeled by docker:

    FROM python:2.7

    WORKDIR /project

    ADD . /project

    RUN pip install -r requirements.txt

    CMD ["/bin/bash", "-c", "sleep 120 && python single.py"]  
    
Note that the modules required is stored in a requirements.txt file which is then read by docker which in turn uses pip to install these dependencies on the container.

The requirements file looks like the following:

    psutil
    mysql-connector-python
    multiprocessing
    cryptography
    
These are the modules this script needs to run.
A full explanation on docker is added to Question 2

QUESTION 2
------------------

For this question I implemented a python flask server that acts as the interface between the processes/services and the database. I used docker to containerize both the database as well as the flask server. I used docker compose to run the docker images togeter. This was harder than I exctpected as I ran into quite a few probelms more on that in the problem section. I chose Flask for the reason that I have grown very fond of python and wish to learn to use it for web development and since Flask is a upcomming framework and is making waves in the web development field so it felt like the obvious choice for me to use. Futher for containerization I used Docker and a requirements file to make it easier to deploy and ship the whole program as a packadge so setup time and difficulty is at a minimum. 

The Breakdown
--------------
So this service is broken down into the app.py file and then the database related files. The app.py file contains the code for the services and and what routes you need to use to enable what services. There are 5 services that can be run these include : 

          --> cpu usage
          --> ram usage
          --> bytes recieved
          --> temprature
          --> packet length (not full added yet)

These services are all packed into functions. The functions get invoked whenever the correct route is called apon. As of yet I have not added a functioning GUI to the service so for now the user has to manualy type in the differnt key words to invoke the services as they are maped for example http://0.0.0.0:5000/cpu will startup the cpu usage monitoring service.

Maped out :

      cpu usage service --> http://0.0.0.0:5000/cpu
      temreture service --> http://0.0.0.0:5000/temp
      bytes recieved service --> http://0.0.0.0:5000/bytes
      ram usage service --> http://0.0.0.0:5000/ram
      packet lenght srvice --> http://0.0.0.0:5000/packet

Once a service is started it will not change the current page so at this point the only visual indicator is the spinning wheel. But it does allow you to start all of the servers and have them run at the same time. The services state is controlled with global true or false variables. If the state variable is false the service will stop running and to start the service again the state variable must be reset first to true.

To stop all the services use the route http://0.0.0.0:5000/stop all . This 'command' will stop all of the services that are currently running.

To reset the stoped services use the route http://0.0.0.0:5000/reset all. This 'command' resets the global state variables to allow the user to run the services again. This means after using the stop all command you HAVE TO USE the reset all command in order to start services run a service.

The Requirements
-----------------
With the first version I did not used docker at all since I had some issues with it , but through alot of research and bug testing I got it working. Now the requirements of each of the two containers is handeled by docker meaning you do not have to manualy install any of the requirements of this service. The docker-compose.yaml  handels most of the setting up that needs to be done. 
Below is a list of dependencies that are handeled by docker:

    Dockerfile for app.py:FROM python:3.6
    ADD app.py /                                 Adds your app.py file

    RUN pip3 install psutil                      Uses pip3 (for python3) to install psutil 

    RUN pip3 install cryptography                "                    "             cryptography

    RUN pip3 install flask                       "                    "             Flask

    RUN pip3 install flask-mysql                 "                    "             flask.mysql module

    RUN pip3 install mysql-connector-python      "                    "             mysql connector python module



  EXPOSE  5000                                 exposes port 5000 for use by the service

  CMD [ "python", "./app.py" ]                 
  
This is called apon by the docker-compose.yaml file and built. The docker-compose.yaml also allows running both the services(app.py) container and the mysql container whch is set up with a initilization file so it can create its on database and you do not have to lift a finger. This file will create 5 tables for each of the services and I used MSQL workbench to view and make sure the data is posted correctly.

Content Of The docker-compose.yml file:

    version: "2"
    services:
      app:
        build: .                                Checks in the current directory for the Dockerfile for the app.py
        links:
          - db                                  links the databsase container
        ports:
          - "5000:5000"                         ports exposed
      db:
        image: mysql:latest                     base image of mysql is used as well a it is the latest that is avalible
        ports:
          - "32000:3306"                        connects through port 3306
        environment:
          MYSQL_ROOT_PASSWORD : root            password for root used 
        volumes:
          - ./db:/docker-entrypoint-initdb.d/:ro   This line sets up the database and will look for the ini sql file which is in                                                a sub directory
For more information look at the init.sql file to see the creation queries for the database as well as the tables that are needed.

Using docker
------------
Something to note that development was first done in a windows enviroment but given alot of problems i faced I swiched over to Ubuntu 18.04 LTS. 

To Run:

    --> press ctr + alt and then t to open up a terminal instance 
    --> install docker using : sudo apt install docker.io
    --> to start and allow docker to start after boot use : sudo systemctl start docker & sudo systemctl enable docker
    --> navigate to the directory of the docker-compose.yml file
    --> use the command : docker-compose up , this will spin up 2 containers one for the services and another for the database.
    --> Since docker compose up will handel creation of the docker image as well as runs right after you dont need to build then run.
    --> Note that you might want to check the IP adress of the docker container when you want to connect to the database with MYSQL workbench. To do this open up a second terminal window and type in : docker images , this will bring up all the images and then type in : docker inspect #imageName this will bring up alot of information about the image but we are interested in the ipV4 adress when connecting with mysql workbench. 
    --> by this time the server is running with both the DB and the services and it can be used.
    --> to close you can just use ctr-c and it will stop the containers from running
    
    
Future Improvements
--------------------

Some of the future imporvements would be to add the missing packet lenght service and nasty service then with that I would also like to add a decent UI to the project. 
Another thing is to add ubuntu itself to the dockerfile in essence spinning up a ubuntu container for a more accurate running enviroment.
Last thing is to improve the Question 1 script to run using true multi-threading
      
  







