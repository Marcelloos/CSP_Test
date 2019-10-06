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
) ENGINE=InnoDB AUTO_INCREMENT=1919 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


cpu_usage Table
----------------
CREATE TABLE `cpu_usage` (
  `id_cpu_usage` int(11) NOT NULL AUTO_INCREMENT,
  `cpu_per` float NOT NULL,
  `time_stamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_cpu_usage`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


packet_lenght Table
-------------------
CREATE TABLE `packet_lenght` (
  `idpacket_lenght` int(11) NOT NULL AUTO_INCREMENT,
  `packet_len` int(11) DEFAULT NULL,
  `time_stamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idpacket_lenght`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ram_usage Table
----------------
CREATE TABLE `ram_usage` (
  `idram_usage` int(11) NOT NULL AUTO_INCREMENT,
  `ram_usage` float NOT NULL,
  `time_stamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idram_usage`)
) ENGINE=InnoDB AUTO_INCREMENT=255 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


tempreture Table
-----------------
CREATE TABLE `tempreture` (
  `idtempreture` int(11) NOT NULL AUTO_INCREMENT,
  `curr_tempreture` int(11) NOT NULL,
  `time_stamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idtempreture`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;




