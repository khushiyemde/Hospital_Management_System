import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class PatientDetailsApp:
    def __init__(self, parent):
        self.parent = parent

        # Configure the grid layout
        self.parent.columnconfigure(0, weight=1)
        self.parent.columnconfigure(1, weight=3)

        # Styling
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 14), padding=10)
        style.configure("TEntry", font=("Arial", 14))
        style.configure("TButton", font=("Arial", 14), padding=10)
        style.configure("TCombobox", font=("Arial", 14))

        # Create and place labels and entry widgets
        ttk.Label(parent, text="Patient ID:").grid(row=0, column=0, sticky=tk.E, padx=10, pady=5)
        self.patient_id_entry = ttk.Entry(parent)
        self.patient_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W + tk.E)

        ttk.Label(parent, text="Name:").grid(row=1, column=0, sticky=tk.E, padx=10, pady=5)
        self.name_entry = ttk.Entry(parent)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W + tk.E)

        ttk.Label(parent, text="Date of Birth:").grid(row=2, column=0, sticky=tk.E, padx=10, pady=5)
        self.dob_entry = ttk.Entry(parent)
        self.dob_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W + tk.E)

        ttk.Label(parent, text="Age:").grid(row=3, column=0, sticky=tk.E, padx=10, pady=5)
        self.age_entry = ttk.Entry(parent)
        self.age_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W + tk.E)

        ttk.Label(parent, text="Gender:").grid(row=4, column=0, sticky=tk.E, padx=10, pady=5)
        self.gender_combobox = ttk.Combobox(parent, values=["Male", "Female", "Other"])
        self.gender_combobox.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W + tk.E)

        ttk.Label(parent, text="Blood Group:").grid(row=5, column=0, sticky=tk.E, padx=10, pady=5)
        self.blood_group_combobox = ttk.Combobox(parent, values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        self.blood_group_combobox.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W + tk.E)

        ttk.Label(parent, text="Address:").grid(row=6, column=0, sticky=tk.E, padx=10, pady=5)
        self.address_entry = ttk.Entry(parent)
        self.address_entry.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W + tk.E)

        ttk.Label(parent, text="Phone Number:").grid(row=7, column=0, sticky=tk.E, padx=10, pady=5)
        self.phone_entry = ttk.Entry(parent)
        self.phone_entry.grid(row=7, column=1, padx=10, pady=5, sticky=tk.W + tk.E)

        ttk.Label(parent, text="Email:").grid(row=8, column=0, sticky=tk.E, padx=10, pady=5)
        self.email_entry = ttk.Entry(parent)
        self.email_entry.grid(row=8, column=1, padx=10, pady=5, sticky=tk.W + tk.E)

        ttk.Label(parent, text="Emergency Contact:").grid(row=9, column=0, sticky=tk.E, padx=10, pady=5)
        self.emergency_contact_entry = ttk.Entry(parent)
        self.emergency_contact_entry.grid(row=9, column=1, padx=10, pady=5, sticky=tk.W + tk.E)

        ttk.Label(parent, text="Medical History:").grid(row=10, column=0, sticky=tk.E, padx=10, pady=5)
        self.medical_history_entry = ttk.Entry(parent)
        self.medical_history_entry.grid(row=10, column=1, padx=10, pady=5, sticky=tk.W + tk.E)

        ttk.Label(parent, text="Date and Time of Entry:").grid(row=11, column=0, sticky=tk.E, padx=10, pady=5)
        self.datetime_entry = ttk.Entry(parent)
        self.datetime_entry.grid(row=11, column=1, padx=10, pady=5, sticky=tk.W + tk.E)
        self.datetime_entry.insert(0, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.datetime_entry.config(state='readonly')

        # Create and place buttons
        ttk.Button(parent, text="Submit", command=self.submit).grid(row=12, column=0, padx=10, pady=10, sticky=tk.E + tk.W)
        ttk.Button(parent, text="Clear", command=self.clear).grid(row=12, column=1, padx=10, pady=10, sticky=tk.E + tk.W)

    def submit(self):
        # Retrieve data from entries
        patient_id = self.patient_id_entry.get()
        name = self.name_entry.get()
        dob = self.dob_entry.get()
        age = self.age_entry.get()
        gender = self.gender_combobox.get()
        blood_group = self.blood_group_combobox.get()
        address = self.address_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        emergency_contact = self.emergency_contact_entry.get()
        medical_history = self.medical_history_entry.get()
        datetime_entry = self.datetime_entry.get()

        # Validation
        if not patient_id or not name or not dob or not age or not gender or not blood_group or not address or not phone or not email or not emergency_contact or not medical_history:
            messagebox.showwarning("Input Error", "All fields are required.")
            return

        if not age.isdigit():
            messagebox.showwarning("Input Error", "Age must be a number.")
            return

        if not phone.isdigit():
            messagebox.showwarning("Input Error", "Phone number must be a number.")
            return

        if not emergency_contact.isdigit():
            messagebox.showwarning("Input Error", "Emergency contact number must be a number.")
            return

        # Show messagebox with patient details
        messagebox.showinfo("Patient Details", 
                            f"Patient ID: {patient_id}\nName: {name}\nDate of Birth: {dob}\nAge: {age}\nGender: {gender}\nBlood Group: {blood_group}\nAddress: {address}\nPhone: {phone}\nEmail: {email}\nEmergency Contact: {emergency_contact}\nMedical History: {medical_history}\nDate and Time of Entry: {datetime_entry}")

    def clear(self):
        # Clear all entries
        self.patient_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.dob_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_combobox.set('')
        self.blood_group_combobox.set('')
        self.address_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.emergency_contact_entry.delete(0, tk.END)
        self.medical_history_entry.delete(0, tk.END)
        self.datetime_entry.config(state='normal')
        self.datetime_entry.delete(0, tk.END)
        self.datetime_entry.insert(0, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.datetime_entry.config(state='readonly')
