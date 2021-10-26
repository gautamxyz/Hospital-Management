from os import initgroups
import subprocess as sp
import pymysql
import pymysql.cursors
from pymysql.constants import CLIENT
from datetime import date

gender_list = ["M", "F", "O"]
blood_group_list = ["A-", "A+", "B+", "B-", "O+", "O-", "AB-", "AB+"]
rooms = []
last_patient_added = 10
last_medical_dept_added = 5
last_doctor_added = 9
last_nurse_added = 3
last_labtech_added = 5
last_employee_added = 5


def option2():
    """
    Function to implement option 1
    """
    print("Not implemented")


def option3():
    """
    Function to implement option 2
    """
    print("Not implemented")


def option4():
    """
    Function to implement option 3
    """
    print("Not implemented")


def count_num_digits(number):
    dig = 0
    while number != 0:
        number = number/10
        dig = dig + 1
    return dig


def InitVariables():
    global last_patient_added
    global last_medical_dept_added
    global last_doctor_added
    global last_nurse_added
    global last_labtech_added
    global last_employee_added
    query = "SELECT * FROM GLOBAL_VARIABLES;"
    try:
        cur.execute(query)
        con.commit()
        data = cur.fetchall()[0]
        last_patient_added = int(data["LAST_PATIENT_ADDED"])
        last_doctor_added = int(data["LAST_DOCTOR_ADDED"])
        last_medical_dept_added = int(data["LAST_MEDICAL_DEPT_ADDED"])
        last_nurse_added = int(data["LAST_NURSE_ADDED"])
        last_labtech_added = int(data["LAST_LAB_TECH_ADDED"])
        last_employee_added = int(data["LAST_EMPLOYEE_ADDED"])

    except Exception as e:
        con.rollback()
        print("Failed to retrieve rooms data")
        print(">>>>>>>>>>>>>", e)
        exit(1)


def StoreVariables():
    global last_patient_added
    global last_medical_dept_added
    global last_doctor_added
    global last_nurse_added
    global last_labtech_added
    global last_employee_added
    query = "UPDATE GLOBAL_VARIABLES SET LAST_PATIENT_ADDED = '%d' LAST_MEDICAL_DEPT_ADDED ='%d' LAST_DOCTOR_ADDED = '%d' LAST_NURSE_ADDED ='%d' LAST_LAB_TECH_ADDED='%d' LAST_EMPLOYEE_ADDED = '%d'" % (
        last_patient_added, last_medical_dept_added, last_doctor_added, last_nurse_added, last_labtech_added, last_employee_added)
    try:
        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to store global data")
        print(">>>>>>>>>>>>>", e)
        exit(1)

    query = "DROP TABLE IF EXISTS `BEDS_OCCUPIED`; CREATE TABLE `BEDS_OCCUPIED` (`BED_NUMBER` int NOT NULL,`OCCUPIED` INT NOT NULL,PRIMARY KEY (`BED_NUMBER`));"
    insert_string = ""
    for i in range(1, 21):
        insert_string += "('%d','%d')," % (i, rooms[i])
    query += "INSERT INTO BEDS_OCCUPIED VALUES %s;" % (insert_string)

    try:
        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to rooms data")
        print(">>>>>>>>>>>>>", e)
        exit(1)


def InitBedsList():
    query = "SELECT * FROM BEDS_OCCUPIED;"
    try:
        print(query)
        cur.execute(query)
        con.commit()
        room_list = cur.fetchall()
        for i in range(1, 21):
            rooms.insert(i, room_list[i-1]["OCCUPIED"])

    except Exception as e:
        con.rollback()
        print("Failed to retrieve rooms data")
        print(">>>>>>>>>>>>>", e)
        exit(1)


def DisplayQuery(fetched_results):
    if len(fetched_results) == 0:
        return 0
    else:
        for row in fetched_results:
            print(row)


def ExecuteQuery(query):
    try:
        print(query)
        cur.execute(query)
        con.commit()
        DisplayQuery(cur.fetchall())

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return 0
    return 1


def ListBedsAvailable():
    print("Beds available are :")
    for i in range(1, 21):
        if rooms[i] == 0:
            print("bed ", i)


def AddEmergencyContact(query,id):
    global last_patient_added
    row = {}
    name = (input("NAME : ")).split(' ')
    row["VISITOR_NAME"] = name[0]
    row["REL_WITH_PATIENT"] = input("RELATION WITH THE PATIENT: ")
    row["PATIENT_ID"] = id
    row["PHONE"] = input("PHONE : ")
    query += "INSERT INTO EMERGENCY_CONTACT( CONTACT_NAME ,REL_WITH_PATIENT,PATIENT_ID,PHONE) VALUES('%s', '%s','%d','%s');" % (
        row["VISITOR_NAME"], row["REL_WITH_PATIENT"], row["PATIENT_ID"], row["PHONE"])

    flag = ExecuteQuery(query)
    if flag == 1:
        print("Inserted Into Database")
    else:
        last_patient_added = last_patient_added - 1
    return


def AddDiseasePatient():
    patient_id = int(input("Enter Patient Id :"))
    disease_id = int(input("Enter Disease Id : "))
    query = "INSERT INTO DIS_PAT( PATIENT_ID ,DISEASE_ID)VALUES('%d','%d')" % (
        patient_id, disease_id)

    flag = ExecuteQuery(query)
    if flag == 1:
        print("Inserted Into Database")


def AddOutPatient(query, id):
    query += "INSERT INTO OUT_PATIENT(PATIENT_ID) VALUES('%d');" % (id
                                                                    )
    AddEmergencyContact(query,id)

def NumberOfBedsAvaialable():
    count = 0
    for i in range(1, 21):
        if rooms[i] == 0:
            count = count + 1
    return count


def AddInPatient(query, id):
    beds = NumberOfBedsAvaialable()
    if beds == 0:
        print("No Beds available\npatient cant be admitted\n")
        return
    bed_allot = -1
    for i in range(1, len(rooms)):
        if rooms[i] == 0:
            bed_allot = i
            rooms[i] = 1
            break
    operation = input("Enter Operation : ")
    date_of_arrival = date.today()
    date_of_discharge = date_of_arrival
    query += "INSERT INTO IN_PATIENT(PATIENT_ID,BED_NUMBER,OPERATION,DATE_OF_ARRIVAL,DATE_OF_DISCHARGE) VALUES('%d','%d','%s','%s','%s');" % (id, bed_allot, operation, date_of_arrival, date_of_discharge
                                                                                                                                              )
    AddEmergencyContact(query,id)


def AddPatient():
    row = {}
    global last_patient_added
    print("Enter Patient details: ")
    name = (input("NAME (First_Name Middle_Name Last_Name): ")).split(' ')
    row["PATIENT_ID"] = last_patient_added + 1
    last_patient_added = last_patient_added + 1
    row["FIRST_NAME"] = name[0]
    row["MIDDLE_NAME"] = name[1]
    row["LAST_NAME"] = name[2]
    row["DOB"] = input("DATE OF BIRTH (YYYY-MM-DD): ")
    row["GENDER"] = input("GENDER(M/F/O): ")
    row["BLOOD_GROUP"] = input(
        "BLOOD_GROUP [A-,A+,B+,B-,O+,O-,AB-,AB+] : ")
    row["PHONE"] = (input("PHONE: "))
    patient_type = int(input("INPATIENT - 0 \nOUTPATIENT - 1\n"))
    if(patient_type != 0 and patient_type != 1):
        print("Invalid Patient Type \n")
        return
    query = "INSERT INTO PATIENT(FIRST_NAME, MIDDLE_NAME, LAST_NAME,DOB, GENDER, BLOOD_GROUP,PHONE) VALUES('%s', '%s', '%s', '%s' , '%s', '%s', '%s');" % (
        row["FIRST_NAME"], row["MIDDLE_NAME"], row["LAST_NAME"], row["DOB"], row["GENDER"], row["BLOOD_GROUP"], row["PHONE"])

    gender_count = gender_list.count(row["GENDER"])

    if gender_count == 0:
        print("Invalid Input for gender\nRecord Not added\nInvalid Input!!!\n")
        return

    blood_group_exists = blood_group_list.count(row["BLOOD_GROUP"])

    if blood_group_exists == 0:
        print("Invalid Input for blood_group\nRecord Not added\nInvalid Input!!!\n")
        return
    if patient_type == 1:
        AddOutPatient(query, row["PATIENT_ID"])
    else:
        AddInPatient(query, row["PATIENT_ID"])
    return


def AddLabTechnician():
    row = {}
    global last_labtech_added
    print("Enter Lab Technician's details: ")
    name = (input("NAME (First_Name Middle_Name Last_Name): ")).split(' ')
    row["FIRST_NAME"] = name[0]
    row["MIDDLE_NAME"] = name[1]
    row["LAST_NAME"] = name[2]
    row["LAB_TECH_ID"] = last_labtech_added+1
    last_nurse_added = last_labtech_added+1
    row["DOB"] = input("DATE OF BIRTH (YYYY-MM-DD): ")
    row["GENDER"] = input("GENDER(M/F/O): ")
    row["BLOOD_GROUP"] = input(
        "BLOOD_GROUP [A-,A+,B+,B-,O+,O-,AB-,AB+] : ")
    row["PHONE"] = (input("PHONE: "))
    #row["EMAIL"] = input("EMAIL : ")
    row["ZIP_CODE"] = int(input("ZIP_CODE : "))
    row["HOUSE"] = input("HOME ADDRESS : ")
    row["QUALIFICATION"] = int(input("QUALIFICATION : "))
    row["EXPERIENCE"] = int(input("EXPERIENCE (in years) : "))
    row["LAB_DEPAR_ID"] = int(input(
        "LAB DEPARTMENT ID (\n1 - Covid Testing lab\n2 - Ultrasound\n3 - X-RAY\n4 - General Purpose testing\n5 - MRI\nenter option value : "))

    query = "INSERT INTO NURSES(FIRST_NAME, MIDDLE_NAME, LAST_NAME, NURSE_ID, DOB,GENDER,BLOOD_GROUP,PHONE,HOUSE,ZIP_CODE,QUALIFICATION,EXPERIENCE) VALUES('%s', '%s', '%s', '%d', '%s', '%s', '%s', %s, %s , %s, %d. %s,%d,%d)" % (
        row["FIRST_NAME"], row["MIDDLE_NAME"], row["LAST_NAME"], row["LAB_TECH_ID"], row["DOB"], row["GENDER"], row["BLOOD_GROUP"], row["PHONE"], row["HOUSE"], row["ZIP_CODE"], row["QUALIFICATION"], row["EXPERIENCE"], row["LAB_DEPAR_ID"])

    gender_count = gender_list.count(row["GENDER"])

    if gender_count == 0:
        print("Invalid Input for gender\nRecord Not added\nInvalid Input!!!\n")
        return

    blood_group_exists = blood_group_list.count(row["BLOOD_GROUP"])

    if blood_group_exists == 0:
        print("Invalid Input for blood_group\nRecord Not added\nInvalid Input!!!\n")
        return

    if row["EXPERIENCE"] < 0:
        print("Enter non-negative value for Experience Field\n")
        return


    flag = ExecuteQuery(query)
    if flag == 1:
        print("Inserted Into Database")
    else:
        last_labtech_added = last_labtech_added - 1
    return


def AddNurse():
    row = {}
    global last_nurse_added
    print("Enter Nurse's details: ")
    name = (input("NAME (First_Name Middle_Name Last_Name): ")).split(' ')
    row["FIRST_NAME"] = name[0]
    row["MIDDLE_NAME"] = name[1]
    row["LAST_NAME"] = name[2]
    row["NURSE_ID"] = last_nurse_added+1
    last_nurse_added = last_nurse_added+1
    row["DOB"] = input("DATE OF BIRTH (YYYY-MM-DD): ")
    row["GENDER"] = input("GENDER(M/F/O): ")
    row["BLOOD_GROUP"] = input(
        "BLOOD_GROUP [A-,A+,B+,B-,O+,O-,AB-,AB+] : ")
    row["PHONE"] = (input("PHONE: "))
    #row["EMAIL"] = input("EMAIL : ")
    row["ZIP_CODE"] = int(input("ZIP_CODE : "))
    row["HOUSE"] = input("HOME ADDRESS : ")
    row["QUALIFICATION"] = int(input("QUALIFICATION : "))
    row["EXPERIENCE"] = int(input("EXPERIENCE (in years) : "))
    #row["MED_DEPAR_ID"] = int(input("MEDICAL DEPARTMENT ID (\n1 - Cardiologists\n2 - Dermatologists\n3 - Neurologists\n4 - Pathologists\n5 - Psychiatrists\nenter option value : "))

    query = "INSERT INTO NURSES(FIRST_NAME, MIDDLE_NAME, LAST_NAME, NURSE_ID, DOB,GENDER,BLOOD_GROUP,PHONE,HOUSE,ZIP_CODE,QUALIFICATION,EXPERIENCE) VALUES('%s', '%s', '%s', '%d', '%s', '%s', '%s', %s, %s , %s, %d. %s,%d)" % (
        row["FIRST_NAME"], row["MIDDLE_NAME"], row["LAST_NAME"], row["NURSE_ID"], row["DOB"], row["GENDER"], row["BLOOD_GROUP"], row["PHONE"], row["HOUSE"], row["ZIP_CODE"], row["QUALIFICATION"], row["EXPERIENCE"])

    gender_count = gender_list.count(row["GENDER"])

    if gender_count == 0:
        print("Invalid Input for gender\nRecord Not added\nInvalid Input!!!\n")
        return

    blood_group_exists = blood_group_list.count(row["BLOOD_GROUP"])

    if blood_group_exists == 0:
        print("Invalid Input for blood_group\nRecord Not added\nInvalid Input!!!\n")
        return

    if row["EXPERIENCE"] < 0:
        print("Enter non-negative value for Experience Field\n")
        return


    flag = ExecuteQuery(query)
    if flag == 1:
        print("Inserted Into Database")
    else:
        last_nurse_added = last_nurse_added - 1
    return


def AddVisitingHours(query, id):
    global last_doctor_added
    VisitingHours = input("Enter Visting Hours : ")
    query += "INSERT INTO VISITING_HOURS(DOCTOR_ID,VISITING_HOURS) VALUES ('%d', '%s');" % (
        id, VisitingHours)
    flag = ExecuteQuery(query)
    if flag == 1:
        print("Inserted Into Database")
    else:
        last_doctor_added = last_doctor_added - 1
def AddTrainee(id, query):
    row = {}
    row["DOCTOR_ID"] = id
    print("Enter Doctor's ID supervising the trainee: ")
    super_id = int(input())

    query += "INSERT INTO TRAINEE(DOCTOR_ID, TEMPORARY_ID) VALUES('%d','%d');" % (
        super_id, id)
    AddVisitingHours(query, id)
    return
def AddPermanent(id, query):
    row = {}
    row["DOCTOR_ID"] = id
    position = input("Enter Doctor's Position ")

    query += "INSERT INTO PERMANENT(DOCTOR_ID, POSITION) VALUES('%d','%s');" % (
        id, position)

    AddVisitingHours(query, id)
    return
def AddDoctor():
    global last_doctor_added
    row = {}
    row["DOCTOR_ID"] = last_doctor_added + 1
    last_doctor_added = last_doctor_added + 1
    print("Enter Doctor's details: ")
    name = (input("NAME (First_Name Middle_Name Last_Name): ")).split(' ')
    row["FIRST_NAME"] = name[0]
    row["MIDDLE_NAME"] = name[1]
    row["LAST_NAME"] = name[2]
    row["DOB"] = input("DATE OF BIRTH (YYYY-MM-DD): ")
    row["GENDER"] = input("GENDER(M/F/O): ")
    row["BLOOD_GROUP"] = input(
        "BLOOD_GROUP [A-,A+,B+,B-,O+,O-,AB-,AB+] : ")
    row["PHONE"] = (input("PHONE: "))
    row["EMAIL"] = input("EMAIL : ")
    row["ZIP_CODE"] = int(input("ZIP_CODE : "))
    row["HOUSE"] = input("HOME ADDRESS : ")
    row["QUALIFICATION"] = input("QUALIFICATION : ")
    row["EXPERIENCE"] = int(input("EXPERIENCE (in years) : "))
    row["MED_DEPAR_ID"] = int(input(
        "MEDICAL DEPARTMENT ID (\n1 - Cardiologists\n2 - Dermatologists\n3 - Neurologists\n4 - Pathologists\n5 - Psychiatrists\nenter option value : "))

    doc_type = int(input("Trainee - 0\nPermanent - 1\n"))
    if doc_type !=0 and doc_type != 1:
        print("Invalid Input\n")
        return
    query = "INSERT INTO DOCTOR(FIRST_NAME, MIDDLE_NAME, LAST_NAME, DOCTOR_ID, DOB,GENDER,BLOOD_GROUP,PHONE,EMAIL,HOUSE,ZIP_CODE,QUALIFICATION,EXPERIENCE,MED_DEPAR_ID) VALUES('%s', '%s', '%s', '%d', '%s', '%s', '%s', '%s', '%s' , '%s', '%d', '%s','%d','%d');" % (
        row["FIRST_NAME"], row["MIDDLE_NAME"], row["LAST_NAME"], row["DOCTOR_ID"], row["DOB"], row["GENDER"], row["BLOOD_GROUP"], row["PHONE"], row["EMAIL"], row["HOUSE"], row["ZIP_CODE"], row["QUALIFICATION"], row["EXPERIENCE"], row["MED_DEPAR_ID"])
    gender_count = gender_list.count(row["GENDER"])
    if gender_count == 0:
        print("Invalid Input for gender\nRecord Not added\nInvalid Input!!!\n")
        return
    blood_group_exists = blood_group_list.count(row["BLOOD_GROUP"])
    if blood_group_exists == 0:
        print("Invalid Input for blood_group\nRecord Not added\nInvalid Input!!!\n")
        return
    if row["EXPERIENCE"] < 0:
        print("Enter non-negative value for Experience Field\n")
        return

    if doc_type == 0:
        AddTrainee(row["DOCTOR_ID"], query)
    else:
        AddPermanent(row["DOCTOR_ID"], query)


def AddMedicalDepartment():
    global last_medical_dept_added
    row = {}
    row["MED_DEPAR_ID"] = last_medical_dept_added + 1
    last_medical_dept_added = last_medical_dept_added + 1
    row["NAME"] = input("Enter Department Name : ")
    row["FLOOR"] = int(input("Enter Medical Dept Id :"))
    row["NUMBER"] = int(input("Department Number ( on the floor ): "))

    if row["MED_DEPAR_ID"] < 0 or row["FLOOR"] < 0 or row["NUMBER"] < 0:
        print("Invalid Input\nFailed to add\n")
        return

    query = "INSERT INTO MEDICAL_DEPARTMENT(MED_DEPAR_ID, FLOOR, NAME, NUMBER ) VALUES('%d', '%d', '%s', '%d')" % (
        row["MED_DEPAR_ID"], row["FLOOR"], row["NAME"], row["NUMBER"])

    flag = ExecuteQuery(query)
    if flag == 1:
        print("Inserted Into Database")
    else:
        last_medical_dept_added = last_medical_dept_added - 1

    return


def AddVisitor():
    row = {}
    name = (input("NAME : ")).split(' ')
    row["VISITOR_NAME"] = name[0]
    row["REL_WITH_PATIENT"] = input("RELATION WITH THE PATIENT: ")
    row["PATIENT_ID"] = int(input("PATIENT ID : "))

    query = "INSERT INTO VISITOR( VISITOR_NAME ,REL_WITH_PATIENT,PATIENT_ID) VALUES('%s', '%s','%d')" % (
        row["VISITOR_NAME"], row["REL_WITH_PATIENT"], row["PATIENT_ID"])

    flag = ExecuteQuery(query)
    if flag == 1:
        print("Inserted Into Database")
    return


def AddDriver():
    global last_employee_added
    row = {}
    row["EMPLOYEE_ID"] = last_employee_added + 1
    last_employee_added = last_employee_added + 1
    print("Enter Employee details: ")
    name = (input("NAME (First_Name Middle_Name Last_Name): ")).split(' ')
    row["FIRST_NAME"] = name[0]
    row["MIDDLE_NAME"] = name[1]
    row["LAST_NAME"] = name[2]
    row["DOB"] = input("DATE OF BIRTH (YYYY-MM-DD): ")
    row["GENDER"] = input("GENDER(M/F/O): ")
    row["BLOOD_GROUP"] = input(
        "BLOOD_GROUP [A-,A+,B+,B-,O+,O-,AB-,AB+] : ")
    row["PHONE"] = (input("PHONE: "))
    row["LICENSE_NUMBER"] = input("LICENSE_NUMBER : ")
    row["INSURANCE_ID"]=input("INSURANCE ID : ")
    row["ZIP_CODE"] = int(input("ZIP_CODE : "))
    row["VEHICLE_NUMBER"] = input("VEHICLE NUMBER : ")
    row["HOUSE"] = input("HOUSE ADDRESS : ")
    query = "INSERT INTO DRIVER(EMPLOYEE_ID,FIRST_NAME, MIDDLE_NAME, LAST_NAME,DOB,LICENSE_NUMBER,GENDER,INSURANCE_ID,BLOOD_GROUP,PHONE,HOUSE,ZIP_CODE,VEHICLE_NUMBER) VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s' , '%d', '%s', '%s');" % (
        row["EMPLOYEE_ID"], row["FIRST_NAME"], row["MIDDLE_NAME"], row["LAST_NAME"], row["DOB"], row["LICENSE_NUMBER"],row["GENDER"],row["INSURANCE_ID"], row["BLOOD_GROUP"], row["PHONE"],row["HOUSE"],row["ZIP_CODE"],row["VEHICLE_NUMBER"])
    gender_count = gender_list.count(row["GENDER"])
    if gender_count == 0:
        print("Invalid Input for gender\nRecord Not added\nInvalid Input!!!\n")
        return
    blood_group_exists = blood_group_list.count(row["BLOOD_GROUP"])
    if blood_group_exists == 0:
        print("Invalid Input for blood_group\nRecord Not added\nInvalid Input!!!\n")
        return
    flag = ExecuteQuery(query)
    if flag == 1:
        print("Inserted Into Database")
    else:
        last_employee_added = last_employee_added - 1


def DischargePatient():
    patient_id = int(input("Enter Patient id"))
    date_of_discharge = date.today()
    query = "UPDATE IN_PATIENT SET DATE_OF_DISCHARGE='%s' WHERE PATIENT_ID='%d'" % (
        date_of_discharge, patient_id)
    ExecuteQuery(query)
    query = "SELECT * FROM IN_PATIENT WHERE PATIENT_ID = '%d'" % (patient_id)
    try:
        print(query)
        cur.execute(query)
        con.commit()
        result = cur.fetchall()
        room_id = result[0]["BED_NUMBER"]
        rooms[room_id] = 0
    except Exception as e:
        con.rollback()
        print("Execute Discharge\n")
        print(">>>>>>>>>>>>>", e)
        return 0
    return 1


def CurrentDoctorsWorking():
    ExecuteQuery(
        "SELECT FIRST_NAME,LAST_NAME,NAME FROM DOCTOR INNER JOIN MEDICAL_DEPARTMENT AS MD ON DOCTOR.MED_DEPAR_ID = MD.MED_DEPAR_ID;")


def CurrentMedicalDept():
    ExecuteQuery("SELECT MED_DEPAR_ID,NAME FROM MEDICAL_DEPARTMENT;")


def CurrentLabTests():
    ExecuteQuery("SELECT TEST_DESCRIPTION FROM TEST;")


def UpdateDocSalary():
    position = (input("Enter doctor position: "))
    salary = (int(input("Enter updated salary: ")))
    query = "UPDATE PERMANENT_SALARY SET SALARY='%d' WHERE POSITION='%s'" % (
        salary, position)
    ExecuteQuery(query)


def UpdateNurseSalary():
    exp = (int(input("Enter nurse's experience: ")))
    salary = (int(input("Enter updated salary: ")))
    query = "UPDATE NURSE_SALARY SET SALARY='%d' WHERE EXPERIENCE='%d'" % (
        salary, exp)
    ExecuteQuery(query)


def UpdateOtherStaffSalary():
    work = input("Enter work type: ")
    salary = (int(input("Enter updated Salary: ")))
    query = "UPDATE OTHER_STAFF_SALARY SET SALARY='%d' WHERE WORK='%s'" % (
        salary, work)
    ExecuteQuery(query)


def GetDoctorFromPosition():
    position = input("Enter the position like HOD, specialist, pupil,expert")
    query = "SELECT DOCTOR.FIRST_NAME, DOCTOR.MIDDLE_NAME,DOCTOR.LAST_NAME FROM DOCTOR INNER JOIN PERMANENT ON DOCTOR.DOCTOR_ID=PERMANENT.DOCTOR_ID WHERE PERMANENT.POSITION = '%s'" % (
        position)
    returnvalue = ExecuteQuery(query)
    if(returnvalue == 0):
        print("An error occured try again")
    return


def GetDoctorFromDepartment():
    position = input(
        "Enter the medical department like Cardiologists, Dermatologists, Neurologists, Pathologists, Psychiatrists")
    query = "SELECT DOCTOR.FIRST_NAME, DOCTOR.MIDDLE_NAME,DOCTOR.LAST_NAME FROM DOCTOR INNER JOIN MEDICAL_DEPARTMENT ON DOCTOR.MED_DEPAR_ID=MEDICAL_DEPARTMENT.MED_DEPAR_ID WHERE MEDICAL_DEPARTMENT.NAME = '%s'" % (
        position)
    returnvalue = ExecuteQuery(query)
    if(returnvalue == 0):
        print("An error occured try again")
    return


def CostOfLabTest():
    position = input(
        "Enter the medical department like RTPCR COVID TEST Rapid antigen test for covid, Test to check dengue and malaria, Blood test, Protient test ")
    query = "SELECT COST FROM TEST WHERE TEST_DESCRIPTION = '%s'" % (position)
    returnvalue = ExecuteQuery(query)
    if(returnvalue == 0):
        print("An error occured try again")
    return


def StockOfMedicine():
    position = input(
        "Enter the medicine name like Crocin Bitadine Paracetamol Aspirin Noradrenaline Firminho ")
    query = "SELECT STOCK FROM MEDICINE WHERE MEDICINE_NAME = '%s'" % (
        position)
    returnvalue = ExecuteQuery(query)
    if(returnvalue == 0):
        print("An error occured try again")
    return


def AvgStayOfDay():
    query = "SELECT AVG(DATEDIFF(DATE_OF_DISCHARGE,DATE_OF_ARRIVAL)) AS too_much_dna FROM IN_PATIENT"
    cur.execute(query)
    con.commit()
    A = cur.fetchall()
    print("Average Stay Of Day : ", A[0]["too_much_dna"])
    return A[0]["too_much_dna"]


def PatStayMoreThanAvg():
    position = AvgStayOfDay()
    query = "SELECT PATIENT.FIRST_NAME, PATIENT.MIDDLE_NAME, PATIENT.LAST_NAME FROM PATIENT INNER JOIN IN_PATIENT ON PATIENT.PATIENT_ID=IN_PATIENT.PATIENT_ID WHERE DATEDIFF(IN_PATIENT.DATE_OF_DISCHARGE,IN_PATIENT.DATE_OF_ARRIVAL) > '%f' " % (
        position)
    ExecuteQuery(query)


def PatWithSameName():
    position = input("Enter first name to display common patient")
    query = "SELECT * FROM PATIENT where FIRST_NAME  = '%s' " % (position)
    ExecuteQuery(query)


def GetMedicineID():
    position = input(
        "Enter Medicine name like Crocin Bitadine Paracetamol Aspirin Noradrenaline Firminho ")
    query = "SELECT MEDICINE_ID FROM MEDICINE where MEDICINE_NAME  = '%s' " % (
        position)
    cur.execute(query)
    con.commit()
    A = cur.fetchall()
    print("Medicine Id associated : ", A[0]["MEDICINE_ID"])
    return A[0]["MEDICINE_ID"]


def PatWithSameMedicine():
    position = GetMedicineID()
    query = "SELECT * FROM PATIENT INNER JOIN PRESCRIPTION ON PATIENT.PATIENT_ID = PRESCRIPTION.PATIENT_ID where MEDICINE_ID = '%d' " % (
        position)
    ExecuteQuery(query)


def AvgSalary():
    query = "SELECT * FROM PERMANENT_SALARY;"
    position = {}
    try:
        cur.execute(query)
        con.commit()
        salary = cur.fetchall()
        for items in salary:
            position[items["POSITION"]] = int(items["SALARY"])
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return 0

    num_permanent = 0
    avg_amount = 0
    try:
        query = "SELECT POSITION FROM PERMANENT"
        cur.execute(query)
        con.commit()
        permanent = cur.fetchall()
        for items in permanent:
            avg_amount = avg_amount + position[items["POSITION"]]
            num_permanent = num_permanent + 1

        if num_permanent != 0:
            avg_amount = avg_amount / num_permanent
            print("Average Doctor's Salary is : ", avg_amount)

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return 0
    return 1


def PatWithSameDisease():
    query = "SELECT * FROM DISEASE;"
    ExecuteQuery(query)
    disease_id = int(input("Enter Disease Id:"))
    query = "SELECT COUNT(*) AS COUNT_ANS FROM DIS_PAT WHERE DISEASE_ID = '%d'" % (disease_id)
    try:
        cur.execute(query)
        con.commit()
        ans = cur.fetchall()
        print("Patient with disease ", disease_id,
              " are ", ans[0]["COUNT_ANS"])
    except Exception as e:
        con.rollback()
        print("Execute Discharge\n")
        print(">>>>>>>>>>>>>", e)
        return 0
    return 1


def deleteDriver():
    '''
        Function that delete record of driver

    '''
    try:

        id = (int(input("Enter Driver_id: ")))
        query = "DELETE FROM DRIVER WHERE EMPLOYEE_ID='%s'" % (id)
        ExecuteQuery(query)
    except Exception as e:
        con.rollback()
        print("Failed to Execute")
        print(">>>>>>", e)
    return


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        deleteDriver()
    elif(ch == 2):
        StockOfMedicine()
    elif(ch == 3):
        CostOfLabTest()
    elif(ch == 4):
        GetDoctorFromDepartment()
    elif(ch == 5):
        GetDoctorFromPosition()
    elif(ch == 6):
        UpdateOtherStaffSalary()
    elif(ch == 7):
        UpdateNurseSalary()
    elif(ch == 8):
        UpdateDocSalary()
    elif(ch == 9):
        num = NumberOfBedsAvaialable()
        print("Number Of beds available : ", num)
    elif(ch == 10):
        CurrentLabTests()
    elif(ch == 11):
        CurrentMedicalDept()
    elif(ch == 12):
        CurrentDoctorsWorking()
    elif(ch == 13):
        AddDriver()
    elif(ch == 14):
        AddVisitor()
    elif(ch == 15):
        AddMedicalDepartment()
    elif(ch == 16):
        AddDoctor()
    elif(ch == 17):
        AddNurse()
    elif(ch == 18):
        AddLabTechnician()
    elif(ch == 19):
        AddPatient()
    elif(ch == 20):
        PatWithSameDisease()
    elif(ch == 21):
        AvgSalary()
    elif(ch == 22):
        PatWithSameMedicine()
    elif(ch == 23):
        PatWithSameName()
    elif(ch == 24):
        AvgStayOfDay()
    elif(ch == 25):
        PatStayMoreThanAvg()
    elif(ch == 26):
        DischargePatient()
    elif(ch == 27):
        ListBedsAvailable()    
    else:
        print("Error: Invalid Option")


# Global


while(1):
    tmp = sp.call('clear', shell=True)
    # Can be skipped if you want to hardcode username and password
    #  username = input("Username: ")
    # password = input("Password: ")
    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(host='localhost',
                              port=30306,
                              user="root",
                              password="MERASQL",
                              db='KAG-HOSPITAL',
                              cursorclass=pymysql.cursors.DictCursor,
                              client_flag = CLIENT.MULTI_STATEMENTS
                              )
                              
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")

        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")
        flag_check = 0
        with con.cursor() as cur:
            while(1):
                if flag_check == 0:
                    InitBedsList()
                    InitVariables()
                    flag_check = 1
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Delete Driver")  # Hire an Employee
                print("2. Check stock of a medicine")  # Fire an Employee
                print("3. Check cost of a lab test")  # Promote Employee
                # Employee Statistics
                print("4. Show Doctors working in a certain department")
                print("5. Show doctors working at a certain positon")
                print("6. Update salary of other staff")
                print("7. Update Nurse Salary")
                print("8. Update salary of doctors")
                print("9. Show vacant beds")
                print("10. Show lab tests")
                print("11. Show names of medical departments")
                print("12. Show names of doctors")
                print("13. Insert driver")
                print("14. Insert visitor")
                print("15. Insert medical department")
                print("16. Insert Doctor")
                print("17. Insert nurse")
                print("18. Insert Lab Technician")
                print("19. Insert patient")
                print("20. Show patients with same disease")
                print("21. Show average salary of doctors")
                print("22. Show patients that bought same medicine")
                print("23. Show patients with same first name ")
                print("24. Show average stay of patients")
                print("25. Show patients that stayed more than average days")
                print("26. Update discharge date of patient")
                print("27. Show beds available")
                print("28. Exit mysql")

                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 28:
                    StoreVariables()
                    exit(0)
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE >")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
