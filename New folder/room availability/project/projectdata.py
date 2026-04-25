import sqlite3 as sqlite

connection = None
cursor = None

def initDBConnection():
    global connection, cursor
    connection = sqlite.connect("project_db.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    connection.commit()

def createTables():
    global connection, cursor
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_id INTEGER PRIMARY KEY,
            patient_name TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctors (
            doctor_id INTEGER PRIMARY KEY,
            doctor_name TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            doctor_id INTEGER,
            date TEXT,
            time TEXT,
            purpose TEXT,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
            FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id)
        )
    """)
    connection.commit()

def getPatients():
    global connection, cursor
    cursor.execute("SELECT patient_id, patient_name FROM patients")
    return cursor.fetchall()

def getDoctors():
    global connection, cursor
    cursor.execute("SELECT doctor_id, doctor_name FROM doctors")
    return cursor.fetchall()

def createAppointment(patient_id, doctor_id, date, time, purpose):
    global connection, cursor
    PARAMETERS = (patient_id, doctor_id, date, time, purpose)
    SQL = "INSERT INTO appointments (patient_id, doctor_id, date, time, purpose) VALUES (?, ?, ?, ?, ?)"
    try:
        cursor.execute(SQL, PARAMETERS)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

def getAppointments():
    global connection, cursor
    SQL = """
    SELECT a.appointment_id, p.patient_name, d.doctor_name, a.date, a.time, a.purpose, a.status
    FROM appointments a
    JOIN patients p ON a.patient_id = p.patient_id
    JOIN doctors d ON a.doctor_id = d.doctor_id
    """
    cursor.execute(SQL)
    return cursor.fetchall()

def closeDBConnection():
    global connection, cursor
    cursor.close()
    connection.close()
    
def isSlotAvailable(doctor_id, date, time):
    global connection, cursor
    SQL = "SELECT COUNT(*) FROM appointments WHERE doctor_id = ? AND date = ? AND time = ?"
    cursor.execute(SQL, (doctor_id, date, time))
    count = cursor.fetchone()[0]
    return count == 0

def deleteAppointment(appointment_id):
    global connection, cursor
    SQL = "DELETE FROM appointments WHERE appointment_id = ?"
    try:
        cursor.execute(SQL, (appointment_id,))
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

