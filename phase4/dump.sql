
-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: Company
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


DROP DATABASE IF EXISTS `KAG-HOSPITAL`;
CREATE SCHEMA `KAG-HOSPITAL`;
USE `KAG-HOSPITAL`;
DROP TABLE IF EXISTS `PATIENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PATIENT` (
  `PATIENT_ID` int NOT NULL,
  `DOB` date NOT NULL,
  `FIRST_NAME` varchar(15) NOT NULL,
  `MIDDLE_NAME` varchar(15) DEFAULT NULL,
  `LAST_NAME` varchar(15) DEFAULT NULL,
  `GENDER` varchar(2)  NOT NULL,
  `BLOOD_GROUP` varchar(4)  NOT NULL,
  `PHONE` varchar(10) NOT NULL, 
  PRIMARY KEY (`PATIENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PATIENT`
--

LOCK TABLES `PATIENT` WRITE;
/*!40000 ALTER TABLE `PATIENT` DISABLE KEYS */;
INSERT INTO `PATIENT` VALUES ('1','1962/11/11','Prasadh','Krishnan','Reddy','M','O+','9898989898'), ('2','1999/10/11','Dhruvee',null,'Birla','F','O-','9898989897'), ('3','1999/11/12','Leo',null,'Messi','M','O+','9898989896'), ('4','2011/11/8','Robert',null,'Lewandoski','M','O+','9898989895'),('5','2011/10/8','Thomas',null,'Muller','M','AB+','9898989894'),('6','2011/7/9','Manuel',null,'Neuer','M','B+','9898989893'),('7','2011/4/8','Sriram',null,'Devata','M','O+','9898989891'),('8','2011/5/6','Cardi',null,'B','F','B+','9898989889'),('9','2011/11/8','Lady',null,'Gaga','F','B-','9898989888'),('10','2011/10/3','Prabhakar',null,null,'M','AB+','9898989885');
/*!40000 ALTER TABLE `PATIENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `IN_PATIENT`
--

DROP TABLE IF EXISTS `IN_PATIENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `IN_PATIENT` (
  `PATIENT_ID` int NOT NULL,
  `BED_NUMBER` int NOT NULL,
  `OPERATION` varchar(255) DEFAULT NULL,
  `DATE_OF_ARRIVAL` date NOT NULL,
  `DATE_OF_DISCHARGE` date NOT NULL, 
  PRIMARY KEY (`PATIENT_ID`),
  CONSTRAINT `PATIENT_ID_ibfk` FOREIGN KEY (`PATIENT_ID`) REFERENCES `PATIENT` (`PATIENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/* !40101 SET character_set_client = @saved_cs_client */;
--
-- Dumping data for table `IN_PATIENT`
--
LOCK TABLES `IN_PATIENT` WRITE;
/*!40000 ALTER TABLE `IN_PATIENT` DISABLE KEYS */;
INSERT INTO `IN_PATIENT` VALUES ('123456789','Alice','F','1988-12-30','Daughter'),('123456789','Elizabeth','F','1967-05-05','Spouse'),('123456789','Michael','M','1988-01-04','Son'),('333445555','Alice','F','1986-04-05','Daughter'),('333445555','Joy','F','1958-05-03','Spouse'),('333445555','Theodore','M','1983-10-25','Son'),('987654321','Abner','M','1942-02-28','Spouse');
/*!40000 ALTER TABLE `IN_PATIENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OUT-PATIENT`
--
DROP TABLE IF EXISTS `OUT_PATIENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OUT_PATIENT` (
  `PATIENT_ID` int NOT NULL,
  PRIMARY KEY (`PATIENT_ID`),
  CONSTRAINT `PATIENT_ID_ibfk1` FOREIGN KEY (`PATIENT_ID`) REFERENCES `PATIENT` (`PATIENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
--
-- Dumping data for table `OUT_PATIENT`
--
LOCK TABLES `OUT_PATIENT` WRITE;
/*!40000 ALTER TABLE `OUT_PATIENT` DISABLE KEYS */;
INSERT INTO `OUT_PATIENT` VALUES ('3'),('4'),('6'),('8'),('9'),('10');
/*!40000 ALTER TABLE `OUT_PATIENT` ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS `ZIP_COUNTRY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ZIP_COUNTRY` (
  `ZIP_CODE` int NOT NULL,
  `CITY` varchar(100)  NOT NULL
 ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `ZIP_COUNTRY` WRITE;
/*!40000 ALTER TABLE `ZIP_COUNTRY` DISABLE KEYS */;
INSERT INTO `ZIP_COUNTRY` VALUES (('110060','NEW DELHI'),('110011','NEW DELHI'),('323232','KARACHI'),('110060','KANPUR'),('110071','KABUL'));
/*!40000 ALTER TABLE `ZIP_COUNTRY` ENABLE KEYS */;
UNLOCK TABLES;

--
--Table structure for table `VISITOR`
--

DROP TABLE IF EXISTS `VISITOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `VISITOR` (
  `NAME` varchar(100) NOT NULL,
  `REL_WITH_PATIENT` varchar(100)  NOT NULL,
  `PATIENT_ID` int NOT NULL,
  FOREIGN KEY (`PATIENT_ID`) REFERENCES `PATIENT` (`PATIENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `VISITOR` WRITE;
/*!40000 ALTER TABLE `VISITOR` DISABLE KEYS */;
INSERT INTO `VISITOR` VALUES (('AMIT SHAH','FRIEND','1'),('HAFEEZ SAEED','ENEMY','2'),('BAGDADI','BROTHER','3'));
/*!40000 ALTER TABLE `VISITOR` ENABLE KEYS */;
UNLOCK TABLES;

--
--Table structure for table `EMERGENCY_CONTACT`
--

DROP TABLE IF EXISTS `EMERGENCY_CONTACT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EMERGENCY_CONTACT` (
  `NAME` varchar(100) NOT NULL,
  `REL_WITH_PATIENT` varchar(100)  NOT NULL,
  `PATIENT_ID` int NOT NULL,
  `PHONE` varchar(13) NOT NULL
  FOREIGN KEY (`PATIENT_ID`) REFERENCES `PATIENT` (`PATIENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `EMERGENCY_CONTACT` WRITE;
/*!40000 ALTER TABLE `EMERGENCY_CONTACT` DISABLE KEYS */;
INSERT INTO `EMERGENCY_CONTACT` VALUES (('AMIT SHAH','FRIEND','1'),('HAFEEZ SAEED','ENEMY','2'),('BAGDADI','BROTHER','3'));
/*!40000 ALTER TABLE `EMERGENCY_CONTACT` ENABLE KEYS */;
UNLOCK TABLES;

--
--Table structure for table `DISEASE`
--

DROP TABLE IF EXISTS `DISEASE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DISEASE` (
   `DISEASE_NAME` varchar(50) NOT NULL,
   `DISEASE_ID` int NOT NULL,  
    PRIMARY KEY (`DISEASE_ID`),
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `DISEASE` WRITE;
/*!40000 ALTER TABLE `DISEASE` DISABLE KEYS */;
INSERT INTO `DISEASE` VALUES (('AMIT SHAH','FRIEND','1'),('HAFEEZ SAEED','ENEMY','2'),('BAGDADI','BROTHER','3'));
/*!40000 ALTER TABLE `DISEASE` ENABLE KEYS */;
UNLOCK TABLES;

--
--Table structure for table `DIS_PAT`
--

DROP TABLE IF EXISTS `DIS_PAT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DIS_PAT` (
   `PATIENT_ID` int NOT NULL,
   `DISEASE_ID` int NOT NULL,
   
  PRIMARY KEY (`DISEASE_ID`),
  FOREIGN KEY (`PATIENT_ID`) REFERENCES `PATIENT` (`PATIENT_ID`)
  FOREIGN KEY (`DISEASE_ID`) REFERENCES `PATIENT` (`PATIENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `DIS_PAT` WRITE;
/*!40000 ALTER TABLE `DIS_PAT` DISABLE KEYS */;
INSERT INTO `DIS_PAT` VALUES (('AMIT SHAH','FRIEND','1'),('HAFEEZ SAEED','ENEMY','2'),('BAGDADI','BROTHER','3'));
/*!40000 ALTER TABLE `EMERGENCY_CONTACT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DOCTOR`
--

DROP TABLE IF EXISTS `DOCTOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DOCTOR` (
  `FIRST_NAME` varchar(15) NOT NULL,
  `MIDDLE_NAME` varchar(15) DEFAULT NULL,
  `LAST_NAME` varchar(15) DEFAULT NULL,
  `DOCTOR_ID` int NOT NULL,
  `DOB` date NOT NULL,
  `GENDER` char(1) NOT NULL,
  `BLOOD_GROUP` varchar(3) NOT NULL,
  `PHONE` varchar(10) NOT NULL, 
  `EMAIL` varchar(100) NOT NULL, 
  `HOUSE` varchar(255) NOT NULL,
  `ZIP_CODE` varchar(6) NOT NULL,
  `QUALIFICATION` varchar(255) NOT NULL,
  `EXPERIENCE` int NOT NULL,
  `MED_DEPAR_ID` int NOT NULL ,
  PRIMARY KEY (`DOCTOR_ID`),
  UNIQUE KEY `PHONE` (`PHONE`),
  UNIQUE KEY `EMAIL` (`EMAIL`),
  FOREIGN KEY (`ZIP_CODE`) REFERENCES `ZIP_COUNTRY` (`ZIP_CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DOCTOR`
--

LOCK TABLES `DOCTOR` WRITE;
/*!40000 ALTER TABLE `DOCTOR` DISABLE KEYS */;
INSERT INTO `DOCTOR` VALUES ('Virat',null,'KOHLI','1','2000-03-02','M','AB-','6969696969','vk@gmail.com','10 Downing-Street','110001','MBBS-AIIMS Delhi','10','4'),
 ('Mahendra','Singh','Dhoni','2','1900-03-02','M','AB-','6969694200','msd@gmail.com','1 Downing-Street','110001','MBBS-AIIMS Mumbai','20','1'),
 ('Anthony',null,'Fauci','3','1970-03-02','M','B-','6969694210','fauci@gmail.com','13 Bank Road','110071','IISC','30','2'),
 ('Neha',null,'Sharma','4','1980-06-02','F','A-','6969694221','neha@gmail.com','3 KG Road','110070','MBBS-Maulana Azad College, Delhi','7','1'),
 ('Rohit',null,'Sharma','5','1985-06-15','M','A+','9069694221','rohit@gmail.com','420 SP Marg','110060','MBBS-Maulana Azad College, Delhi','5','5'),
('Shikhar',null,'Dhawan','6','1976-05-20','M','O+','9069694224','dhawan@gmail.com','69 SP Marg','110060','MBBS-Maulana Azad College, Delhi','6','3'),
 ('Babar',null,'Azam','7','1996-05-14','M','O-','9090909019','babarouton0@gmail.com','garreb gali pakistan','219898','College of Lahore',null,'4'),
 ('Narender','Damodas','Modi','8','1996-05-11','M','O-','9090909018','a@gmail.com','39 lamba marg','110001','College of kolkata',null,'1'),
 ('Anjana','OM','Kashyap','9','1996-05-10','F','O+','9090909017','b@gmail.com','420 shaitaan gali ','323232','College of mumbai',null,'2');
/*!40000 ALTER TABLE `DOCTOR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MEDICAL_DEPARTMENT`
--

DROP TABLE IF EXISTS `MEDICAL_DEPARTMENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MEDICAL_DEPARTMENT` (
  `MED_DEPAR_ID` int NOT NULL,
  `FLOOR` int NOT NULL,
  `NAME` varchar(15) DEFAULT NULL,
  `NUMBER` int NOT NULL,
  PRIMARY KEY (`MED_DEPAR_ID`),
  UNIQUE KEY `DEPAR_ID` (`FLOOR`,`NUMBER`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MEDICAL_DEPARTMENT`
--

LOCK TABLES `MEDICAL_DEPARTMENT` WRITE;
/*!40000 ALTER TABLE `MEDICAL_DEPARTMENT` DISABLE KEYS */;
INSERT INTO `MEDICAL_DEPARTMENT` VALUES ('1','2','Cardiologists','4'),('2','2','Dermatologists','6'),('3','1','Neurologists','1'),('4','3','Pathologists','3'),('5','4','Psychiatrists','4');
/*!40000 ALTER TABLE `MEDICAL_DEPARTMENT` ENABLE KEYS */;
UNLOCK TABLES;

-- Table structure for `PERMANENT_SALARY`

DROP TABLE IF EXISTS `PERMANENT_SALARY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PERMANENT_SALARY` (
  `SALARY` int NOT NULL,
  `POSITION` varchar(15) NOT NULL,
  PRIMARY KEY (`POSITION`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
 
LOCK TABLES `PERMANENT_SALARY` WRITE;
/*!40000 ALTER TABLE `PERMANENT_SALARY` DISABLE KEYS */;
INSERT INTO `PERMANENT_SALARY` VALUES ('25000','Pupil'),('55000','Specialist'),('75000','Expert'),('105000','HOD');
/*!40000 ALTER TABLE `PERMANENT_SALARY` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PERMANENT`
--
DROP TABLE IF EXISTS `PERMANENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PERMANENT` (
  `DOCTOR_ID` int NOT NULL,
  `POSITION` varchar(15) NOT NULL,
  PRIMARY KEY (`DOCTOR_ID`),
  CONSTRAINT `DOCTOR_ibfk_1` FOREIGN KEY (`DOCTOR_ID`) REFERENCES `DOCTOR` (`DOCTOR_ID`),
  FOREIGN KEY (`POSITION`) REFERENCES `PERMANENT_SALARY` (`POSITION`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET character_set_client = @saved_cs_client */;
--
-- Dumping data for table `WORKS_ON`
--

LOCK TABLES `PERMANENT` WRITE;
/*!40000 ALTER TABLE `PERMANENT` DISABLE KEYS */;
INSERT INTO `PERMANENT` VALUES ('1','HOD'),('2','Specialist'),('3','Pupil'),('4','Expert'),('5','HOD'),('6','Pupil');
/*!40000 ALTER TABLE `PERMANENT` ENABLE KEYS */;
UNLOCK TABLES;

-- 



DROP TABLE IF EXISTS `TRAINEE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TRAINEE` (
  `DOCTOR_ID` int NOT NULL,
  `TEMPORARY_ID` int NOT NULL,
  -- `EDUCATION` varchar(255) NOT NULL,
  -- NO NEED REDUNDANT DATA 
  -- DOCTOR ID - UNDER WHOSE SUPERVISION , TRAINEE IS WORKING
  FOREIGN KEY (`DOCTOR_ID`) REFERENCES `DOCTOR` (`DOCTOR_ID`),
  -- TEMPORARY_ID ID OF THE TRAINEE  
  FOREIGN KEY (`TEMPORARY_ID`) REFERENCES `DOCTOR` (`DOCTOR_ID`)  
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
 
LOCK TABLES `TRAINEE` WRITE;
/*!40000 ALTER TABLE `TRAINEE` DISABLE KEYS */;
INSERT INTO `TRAINEE` VALUES ('1','7'),('2','8'),('3','9'));
/*!40000 ALTER TABLE `TRAINEE` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `TRAINEE_SALARY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TRAINEE_SALARY` (
  `SALARY` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
 
LOCK TABLES `TRAINEE_SALARY` WRITE;
/*!40000 ALTER TABLE `TRAINEE_SALARY` DISABLE KEYS */;
INSERT INTO `TRAINEE_SALARY` VALUE ('20000');
/*!40000 ALTER TABLE `TRAINEE_SALARY` ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS `VISITING_HOURS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `VISITING_HOURS` (
  `DOCTOR_ID` int NOT NULL,
  `VISITING_HOURS` varchar(10)  NOT NULL,
  FOREIGN KEY (`DOCTOR_ID`) REFERENCES `DOCTOR` (`DOCTOR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `VISITING_HOURS` WRITE;
/*!40000 ALTER TABLE `VISITING_HOURS` DISABLE KEYS */;
INSERT INTO `VISITING_HOURS` VALUES (('1','3pm-4pm'),('2','4pm-5pm'),('3','2pm-5pm'),('4','12pm-3pm'));
/*!40000 ALTER TABLE `VISITING_HOURS` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `NURSE_SALARY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `NURSE_SALARY` (
  `EXPERIENCE` int NOT NULL,
  `SALARY` int  NOT NULL,
  PRIMARY KEY (`EXPERIENCE`),
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `NURSE_SALARY` WRITE;
/*!40000 ALTER TABLE `NURSE_SALARY` DISABLE KEYS */;
INSERT INTO `NURSE_SALARY` VALUES (('1','10000'),('2','20000'),('3','40000'),('5','50000'));
/*!40000 ALTER TABLE `NURSE_SALARY` ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS `NURSES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `NURSES` (
  `FIRST_NAME` varchar(15) NOT NULL,
  `MIDDLE_NAME` varchar(15) DEFAULT NULL,
  `LAST_NAME` varchar(15) DEFAULT NULL,
  `NURSE_ID` int NOT NULL,
  `DOB` date NOT NULL,
  `GENDER` char(1) NOT NULL,
  `BLOOD_GROUP` varchar(3) NOT NULL,
  `PHONE` varchar(10) NOT NULL, 
  `HOUSE` varchar(255) NOT NULL,
  `ZIP_CODE` varchar(6) NOT NULL,
  `QUALIFICATION` varchar(255) NOT NULL,
  `EXPERIENCE` int NOT NULL,
  PRIMARY KEY (`NURSE_ID`),
  UNIQUE KEY `PHONE` (`PHONE`),
  CONSTRAINT `NURSES_ibfk` FOREIGN KEY (`ZIP_CODE`) REFERENCES `ZIP_COUNTRY` (`ZIP_CODE`),
  CONSTRAINT `NURSES_ibfk` FOREIGN KEY (`EXPERIENCE`) REFERENCES `NURSE_SALARY` (`EXPERIENCE`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
LOCK TABLES `NURSES` WRITE;
/*!40000 ALTER TABLE `NURSES` DISABLE KEYS */;
INSERT INTO `NURSES` VALUES ('Chaitali',null,'Singh','1','1990-03-07','F','O+','6969893425','5 Milton Street','110017','Nursing Diploma-Nursing School,Delhi','3'),
('Shefali',null,'Singh','2','1990-03-01','F','A+','6969893434','5 Lawerence Street','110019','Nursing Diploma-Nursing School,Delhi','2'),
('Priya',null,'Sharma','3','1991-03-07','F','B+','8969893425','7 Mill Street','110018','Nursing Diploma-Nursing School,Delhi','1');
/*!40000 ALTER TABLE `NURSES` ENABLE KEYS */;
UNLOCK TABLES;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DOCTOR`
--

LOCK TABLES `NURSES` WRITE;
/*!40000 ALTER TABLE `NURSES` DISABLE KEYS */;
INSERT INTO `NURSES` VALUES 
/*!40000 ALTER TABLE `NURSES` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `SHIFT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SHIFT` (
  `NURSE_ID` int NOT NULL,
  `SHIFT` varchar(15)  NOT NULL,
  PRIMARY KEY (`NURSE_ID`),
  FOREIGN KEY (`NURSE_ID`) REFERENCES `NURSES` (`NURSE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `SHIFT` WRITE;
/*!40000 ALTER TABLE `SHIFT` DISABLE KEYS */;
INSERT INTO `SHIFT` VALUES (('1','3pm-4pm'),('2','4pm-5pm'),('3','2pm-5pm'),('4','12pm-3pm'));
/*!40000 ALTER TABLE `SHIFT` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `AMBULANCE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE  `AMBULANCE`( `INSURANCE_ID` VARCHAR(10), `VEHICLE_NUMBER` VARCHAR(10), `MODEL` varchar(10), PRIMARY KEY (`VEHICLE_NUMBER`) )ENGINE=InnoDB DEFAULT CHARSET=latin1
LOCK TABLES `AMBULANCE` WRITE;
/*!40000 ALTER TABLE `AMBULANCE` DISABLE KEYS */;
INSERT INTO `AMBULANCE` VALUES ('1234567890','DEL123','ABCD'),('9876543210','DEL456','PQRS'),('1212121212','MUM789','CRETA')
/*!40000 ALTER TABLE `AMBULANCE` ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS `DRIVER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DRIVER`(
  `EMPLOYEE_ID` INT NOT NULL,
  `FIRST_NAME` varchar (15),
  `MIDDLE_NAME` varchar(15),
  `LAST_NAME` varchar(15),
  `DOB` date NOT NULL,
  `LICENSE_NUMBER` varchar(15) NOT NULL,
  `GENDER` char(1) NOT NULL,
  `INSURANCE_ID` varchar(10),
  `BLOOD_GROUP` VARCHAR (3),
  `PHONE` varchar(10) NOT NULL,
  `HOUSE` varchar(100) NOT NULL,
  `ZIP_CODE` varchar(6),
  `VEHICLE_NUMBER` varchar(10),
  CONSTRAINT `DRIVER_ibfk_1` FOREIGN KEY (`VEHICLE_NUMBER`) REFERENCES `AMBULANCE` (`VEHICLE_NUMBER`),
  CONSTRAINT `DRIVER_ibfk_2` FOREIGN KEY (`ZIP_CODE`) REFERENCES `ZIP_COUNTRY` (`ZIP_CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `DRIVER` WRITE;
/*!40000 ALTER TABLE `DRIVER` DISABLE KEYS */;
INSERT INTO `PRESCRIPTION` VALUES (1,'Houston'),(4,'Stafford'),(5,'Bellaire'),(5,'Houston'),(5,'Sugarland');
/*!40000 ALTER TABLE `PRESCRIPTION` ENABLE KEYS */;
UNLOCK TABLES;
DROP TABLE IF EXISTS `OTHER_STAFF_SALARY`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OTHER_STAFF_SALARY`(
  
  `WORK` varchar (50),
  `SALARY` int,
  PRIMARY KEY (`WORK`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



DROP TABLE IF EXISTS `OTHER_STAFF`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OTHER_STAFF`(
  `EMPLOYEE_ID` INT NOT NULL,
  `FIRST_NAME` varchar (15),
  `MIDDLE_NAME` varchar(15),
  `LAST_NAME` varchar(15),
  `DOB` date NOT NULL,  
  `GENDER` char(1) NOT NULL,  
  `BLOOD_GROUP` varchar(3),
  `PHONE` varchar(10),
  `WORK` varchar (50)
  PRIMARY KEY (`EMPLOYEE_ID`),
  CONSTRAINT `OTHER_STAFF_ibfk_1` FOREIGN KEY (`WORK`) REFERENCES `OTHER_STAFF_SALARY` (`WORK`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



DROP TABLE IF EXISTS `MEDICINE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MEDICINE` (
  `MEDICINE_ID` int NOT NULL,
  `MEDICINE_NAME` varchar(25) NOT NULL,
  `COST` int NOT NULL,
  `STOCK` int NOT NULL,
  PRIMARY KEY (`MEDICINE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
 
LOCK TABLES `MEDICINE` WRITE;
/*!40000 ALTER TABLE `MEDICINE` DISABLE KEYS */;
INSERT INTO `MEDICINE` VALUES ('1','Crocin','12','14'),('2','Bitadine','75','67'),('3','Paracetamol','19','69'),('4','Aspirin','500','0'),('5','Noradrenaline','18','200'),('6','Firminho','12','1000');
/*!40000 ALTER TABLE `MEDICINE` ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS `PRESCRIPTION`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PRESCRIPTION` (
  `PATIENT_ID` int NOT NULL,
  `DOCTOR_ID` int NOT NULL,
  `MEDICINE_ID` int NOT NULL,
   CONSTRAINT `PRESCRIPTION_ibfk_1` FOREIGN KEY (`DOCTOR_ID`) REFERENCES `DOCTOR` (`DOCTOR_ID`),
   CONSTRAINT `PRESCRIPTION_ibfk_2` FOREIGN KEY (`PATIENT_ID`) REFERENCES `PATIENT` (`PATIENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PRESCRIPTION`
--
LOCK TABLES `PRESCRIPTION` WRITE;
/*!40000 ALTER TABLE `PRESCRIPTION` DISABLE KEYS */;
INSERT INTO `PRESCRIPTION` VALUES (1,'Houston'),(4,'Stafford'),(5,'Bellaire'),(5,'Houston'),(5,'Sugarland');
/*!40000 ALTER TABLE `PRESCRIPTION` ENABLE KEYS */;
UNLOCK TABLES;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-12 23:29:32