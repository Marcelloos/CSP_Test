# CSP_Test
This ReadMe is for the CSP test
-------------------------------


IMPORTANT: Data Base set up
----------------------------
To set up the data base you need to use the following sql queries to create the databases.
I used msql workbench to monitor and manage the database.


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

Note:
------------------
when using the queries above remember to add the database name infront of the table name for example lets say your database name is obsidion then your query for the temprature table should be :

CREATE TABLE obsidion.tempreture ( idtempreture int(11) NOT NULL AUTO_INCREMENT, curr_tempreture int(11) NOT NULL, time_stamp datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (idtempreture) )
