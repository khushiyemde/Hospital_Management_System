import tkinter as tk
from tkinter import ttk, messagebox
import projectdata as db

# Initialize database connection
db.initDBConnection()

# Main application window
top = tk.Tk()
top.title("Hospital Admission System")
top.geometry("1000x200")

def showRoomBeds(room_type):
    beds = db.getRoomBeds(room_type)
    bed_window = tk.Toplevel(top)
    bed_window.title(f"{room_type.capitalize()} Room")
    
    rows, cols = {
        'single': (3, 3),
        'dual': (7, 2),
        'dormant': (2, 7),
        'icu': (3, 3)
    }[room_type]

    for i, (bed_number, occupied) in enumerate(beds):
        button = tk.Button(bed_window, text=bed_number, bg='red' if occupied else 'white', width=10, height=3)
        button.grid(row=i // cols, column=i % cols, padx=5, pady=5)
        if not occupied:
            button.config(command=lambda b=bed_number: admitPatientDialog(b))

def admitPatientDialog(bed_number):
    def admit():
        patient_name = patient_name_entry.get()
        if patient_name:
            db.admitPatient(patient_name, bed_number)
            messagebox.showinfo("Success", f"Bed {bed_number} booked for {patient_name}")
            admit_window.destroy()
        else:
            messagebox.showwarning("Error", "Please enter a patient name")

    admit_window = tk.Toplevel(top)
    admit_window.title("Admit Patient")
    
    tk.Label(admit_window, text="Patient Name:").pack(padx=10, pady=10)
    patient_name_entry = tk.Entry(admit_window)
    patient_name_entry.pack(padx=10, pady=10)
    
    tk.Button(admit_window, text="Admit", command=admit).pack(padx=10, pady=10)

# Room type selection buttons
rooms_frame = tk.Frame(top)
rooms_frame.pack(pady=20)

rooms = ['single', 'dual', 'dormant', 'icu']
for room in rooms:
    #button = tk.Button(rooms_frame, text=f"{room.capitalize()} Room", command=lambda r=room: showRoomBeds(r))
    #button.pack(side=tk.LEFT, padx=10)
    button = tk.Button(rooms_frame, text=f"{room.capitalize()} Room", width=20, height=5, font=('Arial', 12, 'bold'), bg='#1E3A58', fg='white', command=lambda r=room: showRoomBeds(r))
    button.pack(side=tk.LEFT, padx=10)
    
# Close application properly
def closeApplication():
    db.closeDBConnection()
    top.destroy()

top.protocol("WM_DELETE_WINDOW", closeApplication)
top.mainloop()
