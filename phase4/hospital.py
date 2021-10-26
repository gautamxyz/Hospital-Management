from os import initgroups
import subprocess as sp
import pymysql
import pymysql.cursors

gender_list = ["M", "F", "O"]
blood_group_list = ["A-", "A+", "B+", "B-", "O+", "O-", "AB-", "AB+"]


last_patient_added = 10
last_medical_dept_added = 5
last_doctor_added = 9
last_nurse_added = 3
last_labtech_added = 5


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
        number /= 10
        dig = dig + 1
    return dig
def DisplayQuery(fetched_results):
    if len(fetched_results) == 0:
        return 0
    else:
        for row in fetched_results : 
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
def AddEmergencyContact():
    global last_patient_added
    row = {}
    name = (input("NAME : ")).split(' ')
    row["VISITOR_NAME"] = name[0]
    row["REL_WITH_PATIENT"] = input("RELATION WITH THE PATIENT: ")
    row["PATIENT_ID"] = int(input("PATIENT ID : "))
    row["PHONE"] = input("PHONE : ")
    query = "INSERT INTO EMERGENCY_CONTACT( CONTACT_NAME ,REL_WITH_PATIENT,PATIENT_ID,PHONE) VALUES('%s', '%s','%d','%s')" % (
        row["VISITOR_NAME"], row["REL_WITH_PATIENT"], row["PATIENT_ID"], row["PHONE"])

    flag = ExecuteQuery(query)
    if flag == 1:
            print("Inserted Into Database")
    else:
        last_patient_added= last_patient_added - 1
    return
def AddDiseasePatient(id):
    patient_id = id
    disease_id = int(input("Enter Disease Id : "))
    query = "INSERT INTO DIS_PAT( PATIENT_ID ,DISEASE_ID)VALUES('%d','%d')" % (
        patient_id, disease_id)

    flag = ExecuteQuery(query)
    if flag == 1:
    print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        last_patient_added - 1
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return
def AddPatient():
    try:
        # Takes emplyee details as input
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
        if(patient_type != 0 or patient_type != 1):
            print("Invalid Patient Type \n")
            return
        query = "INSERT INTO PATIENT(FIRST_NAME, MIDDLE_NAME, LAST_NAME,DOB, GENDER, BLOOD_GROUP,PHONE) VALUES('%s', '%s', '%s', '%s' , '%s', '%s', '%s')" % (
            row["FIRST_NAME"], row["MIDDLE_NAME"], row["LAST_NAME"], row["DOB"], row["GENDER"], row["BLOOD_GROUP"], row["PHONE"])

        gender_count = gender_list.count(row["GENDER"])

        if gender_count == 0:
            print("Invalid Input for gender\nRecord Not added\nInvalid Input!!!\n")
            return

        blood_group_exists = blood_group_list.count(row["BLOOD_GROUP"])

        if blood_group_exists == 0:
            print("Invalid Input for blood_group\nRecord Not added\nInvalid Input!!!\n")
            return

        AddEmergencyContact()

        print(query)

        cur.execute(query)
        con.commit()
        AddDiseasePatient(row["PATIENT_ID"])
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        last_patient_added - 1
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return
def AddLabTechnician():
    try:
        # Takes emplyee details as input
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

        query = "INSERT INTO NURSES(FIRST_NAME, MIDDLE_NAME, LAST_NAME, NURSE_ID, DOB,GENDER,BLOOD_GROUP,PHONE,HOUSE,ZIP_CODE,QUALIFICATION,EXPERIENCE) VALUES('%s', '%s', '%s', '%d', '%s', '%c', '%s', %s, %s , %s, %d. %s,%d,%d)" % (
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

        if count_num_digits(row["ZIP_CODE"]) != 6:
            print("ZIP_CODE should be 6 digits long\n")
            return

        print(query)

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        last_nurse_added = last_nurse_added - 1
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def AddNurse():
    try:
        # Takes emplyee details as input
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

        query = "INSERT INTO NURSES(FIRST_NAME, MIDDLE_NAME, LAST_NAME, NURSE_ID, DOB,GENDER,BLOOD_GROUP,PHONE,HOUSE,ZIP_CODE,QUALIFICATION,EXPERIENCE) VALUES('%s', '%s', '%s', '%d', '%s', '%c', '%s', %s, %s , %s, %d. %s,%d)" % (
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

        if count_num_digits(row["ZIP_CODE"]) != 6:
            print("ZIP_CODE should be 6 digits long\n")
            return

        print(query)

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        last_nurse_added = last_nurse_added - 1
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def AddTrainee(id,query):
    try:
        row = {}
        row["DOCTOR_ID"] = id
        print("Enter Doctor's ID supervising the trainee: ")
        super_id = int(input())

        query += "INSERT INTO TRAINEE(DOCTOR_ID, TEMPORARY_ID) VALUES('%d','%d')" % (
            super_id, id)

        print(query)

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def AddPermanent(id,query):
    try:
        global last_doctor_added
        row = {}
        row["DOCTOR_ID"] = id
        position = input("Enter Doctor's Position ")

        query += "INSERT INTO PERMANENT(DOCTOR_ID, POSITION) VALUES('%d','%s')" % (
            id, position)

        print(query)

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        last_doctor_added = last_doctor_added - 1
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return
def AddDoctor():
    global last_doctor_added
    # Takes emplyee details as input
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
    row["QUALIFICATION"] = int(input("QUALIFICATION : "))
    row["EXPERIENCE"] = int(input("EXPERIENCE (in years) : "))
    row["MED_DEPAR_ID"] = int(input(
        "MEDICAL DEPARTMENT ID (\n1 - Cardiologists\n2 - Dermatologists\n3 - Neurologists\n4 - Pathologists\n5 - Psychiatrists\nenter option value : "))
    doc_type = int(input("Trainee - 0\nPermanent - 1\n"))
    if(doc_type !=0 or doc_type !=1):
        print("Invalid Input\n")
        return
    
    query = "INSERT INTO DOCTOR(FIRST_NAME, MIDDLE_NAME, LAST_NAME, DOCTOR_ID, DOB,GENDER,BLOOD_GROUP,PHONE,EMAIL,HOUSE,ZIP_CODE,QUALIFICATION,EXPERIENCE,MED_DEPAR_ID) VALUES('%s', '%s', '%s', '%d', '%s', '%c', '%s', %d, %s , %s, %d. %s,%d,%d)" % (
        row["FIRST_NAME"], row["MIDDLE_NAME"], row["LAST_NAME"], row["DOCTOR_ID"], row["DOB"], row["GENDER"], row["BLOOD_GROUP"], row["PHONE"], row["EMAIL"], row["HOUSE"], row["ZIP_CODE"], row["QUALIFICATION"], row["EXPERIENCE"], row["MED_DEPAR_ID"]);

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
    if count_num_digits(row["ZIP_CODE"]) != 6:
        print("ZIP_CODE should be 6 digits long\n")
        return

    print(query)

    print("Inserted Into Database")
    if doc_type == 0:
        AddTrainee(row["DOCTOR_ID"],query);
    else : 
        AddPermanent(row["DOCTOR_ID"],query);
def AddMedicalDepartment():
    try:
        # Takes emplyee details as input
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

        print(query)

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        last_medical_dept_added = last_medical_dept_added - 1
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def AddVisitor():
    try:
        # Takes emplyee details as input
        row = {}
        name = (input("NAME : ")).split(' ')
        row["VISITOR_NAME"] = name[0]
        row["REL_WITH_PATIENT"] = input("RELATION WITH THE PATIENT: ")
        row["PATIENT_ID"] = int(input("PATIENT ID : "))

        query = "INSERT INTO VISITOR( VISITOR_NAME ,REL_WITH_PATIENT,PATIENT_ID) VALUES('%s', '%s','%d')" % (
            row["VISITOR_NAME"], row["REL_WITH_PATIENT"], row["PATIENT_ID"])

        print(query)

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        last_patient_added - 1
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return
def CurrentDoctorsWorking():
    ExecuteQuery("SELECT FIRST_NAME,LAST_NAME,NAME FROM DOCTOR INNER JOIN MEDICAL_DEPARTMENT AS MD ON DOCTOR.MED_DEPAR_ID = MD.MED_DEPAR_ID;")
def CurrentMedicalDept():
    ExecuteQuery("SELECT MED_DEPAR_ID,NAME FROM MEDICAL_DEPARTMENT;")
def ShowXYZ():
    ExecuteQuery("SELECT MED_DEPAR_ID,NAME FROM MEDICAL_DEPARTMENT;")
    departmentName=int(input("Enter the Department Id :"))

    query = ""

    
def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        # tp be duifheiwuf
        option2()
    elif(ch == 2):
        option2()
    elif(ch == 3):
        option3()
    elif(ch == 4):
        option4()
    else:
        print("Error: Invalid Option")

def deleteDriver(employee_id):
    '''
        Function that delete record of driver
    '''



# Global
while(1):
    tmp = sp.call('clear', shell=True)

    # Can be skipped if you want to hardcode username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(host='localhost',
                              port=30306,
                              user="root",
                              password="password",
                              db='COMPANY',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Option 1")  # Hire an Employee
                print("2. Option 2")  # Fire an Employee
                print("3. Option 3")  # Promote Employee
                print("4. Option 4")  # Employee Statistics
                print("5. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 5:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
