import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
import projectdata as db

# Initialize the main application window
top = tk.Tk()
top.title("Doctor Appointment System")
top.geometry("800x600")
top.configure(bg="#D4F1F7")
db.initDBConnection()
db.createTables()

# Functions
def addAppointment():
    appointment_form = tk.Toplevel(top)
    appointment_form.title("Add Appointment")
    appointment_form.geometry("400x500")
    appointment_form.configure(bg="#D4F1F7")
    
    # Load data from the database
    patients = db.getPatients()
    doctors = db.getDoctors()
    
    # Patient name
    tk.Label(appointment_form, text="Patient Name:", bg="#D4F1F7").grid(row=0, column=0, padx=10, pady=10, sticky='w')
    patient_name_var = tk.StringVar()
    patient_combo = ttk.Combobox(appointment_form, textvariable=patient_name_var)
    patient_combo['values'] = [patient[1] for patient in patients]
    patient_combo.grid(row=0, column=1, padx=10, pady=10)
    
    # Doctor name
    tk.Label(appointment_form, text="Doctor Name:", bg="#D4F1F7").grid(row=1, column=0, padx=10, pady=10, sticky='w')
    doctor_name_var = tk.StringVar()
    doctor_combo = ttk.Combobox(appointment_form, textvariable=doctor_name_var)
    doctor_combo['values'] = [doctor[1] for doctor in doctors]
    doctor_combo.grid(row=1, column=1, padx=10, pady=10)
    
    # Date
    tk.Label(appointment_form, text="Date:", bg="#D4F1F7").grid(row=2, column=0, padx=10, pady=10, sticky='w')
    date_entry = DateEntry(appointment_form, selectmode='day', date_pattern='yyyy-mm-dd')
    date_entry.grid(row=2, column=1, padx=10, pady=10)
    
    # Time
    tk.Label(appointment_form, text="Time:", bg="#D4F1F7").grid(row=3, column=0, padx=10, pady=10, sticky='w')
    time_var = tk.StringVar()
    time_combo = ttk.Combobox(appointment_form, textvariable=time_var)
    time_combo['values'] = ['10:00am', '10:30am', '11:00am', '11:30am', '12:00pm', '12:30pm', '01:00pm', '01:30pm', '2:00pm', '2:30pm']
    time_combo.grid(row=3, column=1, padx=10, pady=10)
    
    # Purpose
    tk.Label(appointment_form, text="Purpose:", bg="#D4F1F7").grid(row=4, column=0, padx=10, pady=10, sticky='w')
    purpose_entry = ttk.Entry(appointment_form)
    purpose_entry.grid(row=4, column=1, padx=10, pady=10)
    
    # Button to book appointment
    def bookAppointment():
        patient_name = patient_name_var.get()
        doctor_name = doctor_name_var.get()
        date = date_entry.get_date()
        time = time_var.get()
        purpose = purpose_entry.get()
        
        if not (patient_name and doctor_name and date and time and purpose):
            messagebox.showerror("Error", "All fields are required.")
            return
        
        try:
            patient_id = next(patient[0] for patient in patients if patient[1] == patient_name)
        except StopIteration:
            messagebox.showerror("Error", "Selected patient does not exist.")
            return
        
        try:
            doctor_id = next(doctor[0] for doctor in doctors if doctor[1] == doctor_name)
        except StopIteration:
            messagebox.showerror("Error", "Selected doctor does not exist.")
            return
        
        if not db.isSlotAvailable(doctor_id, date, time):
            messagebox.showwarning("Slot Unavailable", "Selected slot is not available. Please choose another time.")
            return
        
        if db.createAppointment(patient_id, doctor_id, date, time, purpose):
            messagebox.showinfo("Success", "Appointment booked successfully.")
            refreshAppointmentList()
            appointment_form.destroy()
        else:
            messagebox.showerror("Error", "Failed to book appointment.")
    
    ttk.Button(appointment_form, text="Book Appointment", command=bookAppointment).grid(row=5, column=0, columnspan=2, pady=20)

def deleteAppointment():
    selected_item = appointment_tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select an appointment to delete.")
        return

    appointment_id = appointment_tree.item(selected_item)['values'][0]
    if db.deleteAppointment(appointment_id):
        messagebox.showinfo("Success", "Appointment deleted successfully.")
        refreshAppointmentList()
    else:
        messagebox.showerror("Error", "Failed to delete appointment.")

def refreshAppointmentList():
    for i in appointment_tree.get_children():
        appointment_tree.delete(i)
    
    appointments = db.getAppointments()
    for appointment in appointments:
        appointment_tree.insert('', 'end', values=appointment)

def closeApplication(event=None):
    db.closeDBConnection()
    top.destroy()

# GUI Contents

# Heading
heading_label = tk.Label(top, text="APPOINTMENTS", font=("Arial", 18, "bold"), bg="#D4F1F7")
heading_label.grid(row=0, column=0, columnspan=2, pady=10)

# Appointment List
columns = ('ID', 'Patient Name', 'Doctor Name', 'Date', 'Time', 'Purpose', 'Status')
appointment_tree = ttk.Treeview(top, columns=columns, show='headings')
for col in columns:
    appointment_tree.heading(col, text=col, anchor='center')

appointment_tree.column('ID', width=30, anchor='center')
appointment_tree.column('Patient Name', width=100, anchor='center')
appointment_tree.column('Doctor Name', width=100, anchor='center')
appointment_tree.column('Date', width=80, anchor='center')
appointment_tree.column('Time', width=70, anchor='center')
appointment_tree.column('Purpose', width=150, anchor='center')
appointment_tree.column('Status', width=100, anchor='center')

style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

appointment_tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
top.grid_rowconfigure(1, weight=1)
top.grid_columnconfigure(0, weight=1)
top.grid_columnconfigure(1, weight=1)

# Add and Delete Appointment Buttons
ttk.Button(top, text="Add Appointment", command=addAppointment, width=20).grid(row=2, column=0, pady=20, padx=10, ipadx=20, ipady=10)
ttk.Button(top, text="Delete Appointment", command=deleteAppointment, width=20).grid(row=2, column=1, pady=20, padx=10, ipadx=20, ipady=10)

# Initial data load
refreshAppointmentList()

top.protocol("WM_DELETE_WINDOW", closeApplication)
top.mainloop()
