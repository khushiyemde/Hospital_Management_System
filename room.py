'''import tkinter as tk
from tkinter import ttk, messagebox
import projectdata as db

# Initialize database connection
db.initDBConnection()

# Main application window
top = tk.Tk()
top.title("Hospital Admission System")
top.geometry("800x600")  # Set the same dimension as the dashboard
top.resizable(width=False, height=False)

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def showRoomBeds(room_type):
    beds = db.getRoomBeds(room_type)
    bed_window = tk.Toplevel(top)
    bed_window.title(f"{room_type.capitalize()} Room")
    bed_window.geometry("800x600")  # Set the same dimension as the dashboard
    bed_window.resizable(width=False, height=False)
    bed_window.transient(top)
    bed_window.grab_set()
    center_window(bed_window)

    rows, cols = {
        'single': (3, 3),
        'dual': (7, 2),
        'dormant': (2, 7),
        'icu': (3, 3)
    }[room_type]

    # Center frame for bed buttons
    beds_frame = tk.Frame(bed_window)
    beds_frame.place(relx=0.5, rely=0.5, anchor="center")

    for i, (bed_number, occupied) in enumerate(beds):
        button = tk.Button(beds_frame, text=bed_number, bg='red' if occupied else 'white', width=10, height=3)
        button.grid(row=i // cols, column=i % cols, padx=5, pady=5)
        if not occupied:
            button.config(command=lambda b=bed_number: admitPatientDialog(bed_window, b))

def admitPatientDialog(parent, bed_number):
    def admit():
        patient_name = patient_name_entry.get()
        if patient_name:
            db.admitPatient(patient_name, bed_number)
            messagebox.showinfo("Success", f"Bed {bed_number} booked for {patient_name}")
            admit_window.destroy()
        else:
            messagebox.showwarning("Error", "Please enter a patient name")

    admit_window = tk.Toplevel(parent)
    admit_window.title("Admit Patient")
    admit_window.geometry("400x200")  # Set a smaller size for the admit dialog
    admit_window.transient(parent)
    admit_window.grab_set()
    center_window(admit_window)

    tk.Label(admit_window, text="Patient Name:").pack(padx=10, pady=10)
    patient_name_entry = tk.Entry(admit_window)
    patient_name_entry.pack(padx=10, pady=10)
    
    tk.Button(admit_window, text="Admit", command=admit).pack(padx=10, pady=10)

# Room type selection buttons
rooms_frame = tk.Frame(top)
rooms_frame.place(relx=0.5, rely=0.5, anchor="center")

rooms = ['single', 'dual', 'dormant', 'icu']

for i, room in enumerate(rooms):
    button = tk.Button(rooms_frame, text=f"{room.capitalize()} Room", width=20, height=5, font=('Arial', 12, 'bold'), bg='#1E3A58', fg='white', command=lambda r=room: showRoomBeds(r))
    button.grid(row=i//2, column=i%2, padx=20, pady=20)  # Positioning buttons in a 2x2 grid

# Close application properly
def closeApplication():
    db.closeDBConnection()
    top.destroy()

top.protocol("WM_DELETE_WINDOW", closeApplication)
center_window(top)
top.mainloop()'''


import tkinter as tk
from tkinter import ttk, messagebox
import projectdata as db

# Initialize database connection
db.initDBConnection()

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def show_room_ui(parent):
    room_window = tk.Toplevel(parent)
    room_window.title("Room Allocation")
    room_window.geometry("800x600")  # Set the same dimension as the dashboard
    room_window.resizable(width=False, height=False)
    center_window(room_window)

    def showRoomBeds(room_type):
        beds = db.getRoomBeds(room_type)
        bed_window = tk.Toplevel(room_window)
        bed_window.title(f"{room_type.capitalize()} Room")
        bed_window.geometry("800x600")  # Set the same dimension as the dashboard
        bed_window.resizable(width=False, height=False)
        bed_window.transient(room_window)
        bed_window.grab_set()
        center_window(bed_window)

        rows, cols = {
            'single': (3, 3),
            'dual': (7, 2),
            'dormant': (2, 7),
            'icu': (3, 3)
        }[room_type]

        # Center frame for bed buttons
        beds_frame = tk.Frame(bed_window)
        beds_frame.place(relx=0.5, rely=0.5, anchor="center")

        for i, (bed_number, occupied) in enumerate(beds):
            button = tk.Button(beds_frame, text=bed_number, bg='red' if occupied else 'white', width=10, height=3)
            button.grid(row=i // cols, column=i % cols, padx=5, pady=5)
            if not occupied:
                button.config(command=lambda b=bed_number: admitPatientDialog(bed_window, b))

    def admitPatientDialog(parent, bed_number):
        def admit():
            patient_name = patient_name_entry.get()
            if patient_name:
                db.admitPatient(patient_name, bed_number)
                messagebox.showinfo("Success", f"Bed {bed_number} booked for {patient_name}")
                admit_window.destroy()
            else:
                messagebox.showwarning("Error", "Please enter a patient name")

        admit_window = tk.Toplevel(parent)
        admit_window.title("Admit Patient")
        admit_window.geometry("400x200")  # Set a smaller size for the admit dialog
        admit_window.transient(parent)
        admit_window.grab_set()
        center_window(admit_window)

        tk.Label(admit_window, text="Patient Name:").pack(padx=10, pady=10)
        patient_name_entry = tk.Entry(admit_window)
        patient_name_entry.pack(padx=10, pady=10)
        
        tk.Button(admit_window, text="Admit", command=admit).pack(padx=10, pady=10)

    # Room type selection buttons
    rooms_frame = tk.Frame(room_window)
    rooms_frame.place(relx=0.5, rely=0.5, anchor="center")

    rooms = ['single', 'dual', 'dormant', 'icu']

    for i, room in enumerate(rooms):
        button = tk.Button(rooms_frame, text=f"{room.capitalize()} Room", width=20, height=5, font=('Arial', 12, 'bold'), bg='#1E3A58', fg='white', command=lambda r=room: showRoomBeds(r))
        button.grid(row=i//2, column=i%2, padx=20, pady=20)  # Positioning buttons in a 2x2 grid

    # Close application properly
    def closeApplication():
        db.closeDBConnection()
        room_window.destroy()

    room_window.protocol("WM_DELETE_WINDOW", closeApplication)

