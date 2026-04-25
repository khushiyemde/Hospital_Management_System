import sqlite3 as sqlite
from datetime import datetime

connection = None
cursor = None

#for creating tables
def initDBConnection():
    global connection, cursor
    connection = sqlite.connect("hospital_db1.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        patient_name TEXT,
                        dob TEXT,
                        age INTEGER,
                        gender TEXT,
                        blood_group TEXT,
                        phone TEXT,
                        email TEXT,
                        address TEXT,
                        medical_history TEXT,
                        entry_datetime TEXT,
                        checkout_datetime TEXT,
                        room_type TEXT,
                        bed_number TEXT,
                        doctor_name TEXT
                      )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS rooms (
                        room_type TEXT,
                        bed_number TEXT,
                        occupied BOOLEAN)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        patient_name TEXT,
                        bed_number TEXT)''')
    initialize_rooms()
    connection.commit()
    
def initialize_rooms():
        rooms = {
            'single': 9,
            'dual': 4,
            'General': 14,
            'icu': 9
                }
    

#for adding patients details to database
def addPatientDetails(details):
    global connection, cursor
    try:
        cursor.execute('''INSERT INTO patients 
                          (patient_name, dob, age, gender, blood_group, phone, email, address, medical_history, entry_datetime)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                       (details['Patient Name'], details['Date of Birth'], details['Age'], 
                        details['Gender'], details['Blood Group'], details['Phone Number'], details['Email'], 
                        details['Address'], details['Medical History'], details['Entry Date and Time']))
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
#to get rooms availabe in our system
def getRoomBeds(room_type):
    cursor.execute("SELECT bed_number, occupied FROM rooms WHERE room_type = ?", (room_type,))
    return cursor.fetchall()
#to get name of all the patients in a scrolldown
def getPatients():
    global connection, cursor
    cursor.execute("SELECT patient_id, patient_name FROM patients")
    return cursor.fetchall()

#to link patient name to bed
def admitPatient(patient_name, bed_number):
    cursor.execute("UPDATE rooms SET occupied = ? WHERE bed_number = ?", (True, bed_number))
    cursor.execute("INSERT INTO patients (patient_name, bed_number) VALUES (?, ?)", (patient_name, bed_number))
    connection.commit()

#for closing database
def closeDBConnection():
    global connection, cursor
    if cursor:
        cursor.close()
    if connection:
        connection.close()
