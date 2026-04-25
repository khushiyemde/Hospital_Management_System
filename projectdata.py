import sqlite3 as sqlite

connection = None
cursor = None

def initDBConnection():
    global connection, cursor
    connection = sqlite.connect("hospital_db.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS rooms (
                        room_type TEXT,
                        bed_number TEXT,
                        occupied BOOLEAN)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        patient_name TEXT,
                        bed_number TEXT)''')
    initialize_rooms()
    
def initialize_rooms():
    rooms = {
        'single': 9,
        'dual': 4,
        'dormant': 14,
        'icu': 9
    }
##    for room_type, beds in rooms.items():
##        for i in range(1, beds + 1):
##            bed_number = f"{i:02}" if room_type != 'icu' else f"{i*11}"
##            cursor.execute("INSERT INTO rooms (room_type, bed_number, occupied) VALUES (?, ?, ?)",
##                           (room_type, bed_number, False))
##    connection.commit()

def getRoomBeds(room_type):
    cursor.execute("SELECT bed_number, occupied FROM rooms WHERE room_type = ?", (room_type,))
    return cursor.fetchall()

def admitPatient(patient_name, bed_number):
    cursor.execute("UPDATE rooms SET occupied = ? WHERE bed_number = ?", (True, bed_number))
    cursor.execute("INSERT INTO patients (patient_name, bed_number) VALUES (?, ?)", (patient_name, bed_number))
    connection.commit()

def closeDBConnection():
    cursor.close()
    connection.close()
