CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY,
    patient_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS doctors (
    doctor_id INTEGER PRIMARY KEY,
    doctor_name TEXT NOT NULL
);

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
);
