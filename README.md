# too_much_data Group Project Phase 4

- **Gautam Ghai 2020101023**
- **Aditya Malhotra 2020101052**
- **Karmanjyot Singh 2020101062**

## How to run script

Run the following from the project folder

- to load our database

The start command is

```
mysql -u <user_name> -p <password>
source ./dump.sql;
```

Then exit the MySQL CLI

```
exit
```

- Please have pymysql installed if not installed do the following step

```
pip3 install pymysql
```

```
python3 operations.py
```
- give your username, password, and port (for mysql), it assumed that it is on localhost.

## Functions

1. Delete Driver 
	After pressing 1 you would be able to delete a record of the driver from the table DRIVER , holding the data , after entering the DRIVER ID ( employee ID corresponding to the record to be deleted)
	
2. Check stock of a medicine
	After pressing 2 you would be able to see the stock of available medicine , 
    After pressing 2 enter the Medicine ID , to check the stock of that specific Medicine.
    
	
3. Check cost of a lab test
   
	After pressing 3 you would be able to see the cost of a lab test
	
4. Show Doctors working in a certain department
	After pressing 4 you would be asked to enter medical department id and then it will display the doctors working in that department. 
	
5. Show doctors working at a certain positon
	After pressing 5 you would be asked to enter position and then it will display the doctors that have the same position

6. Update salary of other staff
   

7. Update Nurse Salary

8. Update salary of doctors

**Function 6,7,8 are somewhat similar and they update the salary of staff in the video we have shown only function 6 as they are similar**

9. Show vacant beds
	After pressing 9 you would be able to see count of vacant beds available in our hospital
	
10. Show lab tests
	After pressing 10 you would be able to see the test our hospital can conduct
	
11. Show names of medical departments
	After pressing 11 you would be able to see the medical departments our hospital have conduct
	
12. Show names of doctors
	After pressing 12 you would be able to see the name of all the doctors that work in our hospital
	
13. Insert driver

14. Insert visitor

15. Insert medical department

16. Insert Doctor

17. Insert nurse

18. Insert Lab Technician

19. Insert patient

	The function 13,14,15,16,17,18,19,20 are somewhat similar they ask data from the users and add them in the respective table in case of some wrong input entered by the user it shows error

20. Show patients with same disease
	It displays the name of the patient that are infected by same disease, it asks for disease id after displaying disease name
	
21. Show average salary of doctors
	It displays the average of the salary that the doctors {PERMANENT} earns
	
22. Show patients that bought same medicine
	It shows details of all the patient that are prescriped/bought same the medicine
	
23. Show patients with same first name
	It shows details of the patient that have a common first name
    
24. Show average stay of patients
	It shows the average number of days a patient {in patient} stays in the hospital
	
25. Show patients that stayed more than average days
	It displays the name of the patient that stayed more than average in the hospital
	
26. Update discharge date of patient
	We assume that a discharge date is determined by the doctor so this will be updated by the doctor only, this will update the beds available and will update date of discharge
	
27. Show beds available
	It shows the number of the beds that are currently not occupied
	
28. Exit mysql

    saves the updated tables into the database, and exits

## Changes made from Phase 3

- Added table GLOBAL_VARIABLES to store some variables that are used in the code and need to stay updated even after the CLI has been exited
- Added table BEDS_OCCUPIED it used to store whether the beds are occupied or not, it has 2 attributes BED_NUMBER and OCCUPIED, occupied equal to 1 shows bed occupied and 0 means bed not occupied
