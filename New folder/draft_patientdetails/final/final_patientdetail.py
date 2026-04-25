import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime
import project_data as db

db.initDBConnection()

def submit_details():
    details = {
        "Patient Name": entry_name.get(),
        "Date of Birth": dob_entry.get(),
        "Age": entry_age.get(),
        "Gender": gender_var.get(),
        "Blood Group": blood_group_var.get(),
        "Phone Number": entry_phone.get(),
        "Email": entry_email.get(),
        "Address": entry_address.get("1.0", tk.END).strip(),
        "Medical History": entry_medical_history.get("1.0", tk.END).strip(),
        "Entry Date and Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Add details to database
    if db.addPatientDetails(details):
        messagebox.showinfo("Success", "Patient details submitted successfully")
    else:
        messagebox.showerror("Error", "Failed to submit patient details")

# Create the main window
root = tk.Tk()
root.title("Patient Details Dashboard")
root.configure(background='#D4F1F7')

# Create a frame to hold the form elements
frame = ttk.Frame(root, padding="20", style="TFrame")
frame.grid(row=0, column=0, sticky="nsew")

# Configure grid weights for centering the frame
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Configure the frame background color
style = ttk.Style()
style.configure("TFrame", background='#D4F1F7')
style.configure("TLabel", background='#D4F1F7')

# Patient Name
ttk.Label(frame, text="Patient Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_name = ttk.Entry(frame)
entry_name.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Date of Birth
ttk.Label(frame, text="Date of Birth:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
dob_entry = DateEntry(frame, date_pattern='yyyy-mm-dd')
dob_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Age
ttk.Label(frame, text="Age:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_age = ttk.Entry(frame)
entry_age.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Gender
ttk.Label(frame, text="Gender:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
gender_var = tk.StringVar()
gender_options = ["Male", "Female", "Other"]
gender_menu = ttk.Combobox(frame, textvariable=gender_var, values=gender_options)
gender_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Blood Group
ttk.Label(frame, text="Blood Group:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
blood_group_var = tk.StringVar()
blood_group_options = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
blood_group_menu = ttk.Combobox(frame, textvariable=blood_group_var, values=blood_group_options)
blood_group_menu.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Phone Number
ttk.Label(frame, text="Phone Number:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
entry_phone = ttk.Entry(frame)
entry_phone.grid(row=5, column=1, padx=10, pady=5, sticky="w")

# Email
ttk.Label(frame, text="Email:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
entry_email = ttk.Entry(frame)
entry_email.grid(row=6, column=1, padx=10, pady=5, sticky="w")

# Address
ttk.Label(frame, text="Address:").grid(row=7, column=0, padx=10, pady=5, sticky="ne")
entry_address = tk.Text(frame, height=3, width=30)
entry_address.grid(row=7, column=1, padx=10, pady=5, sticky="w")

# Medical History
ttk.Label(frame, text="Medical History:").grid(row=8, column=0, padx=10, pady=5, sticky="ne")
entry_medical_history = tk.Text(frame, height=5, width=30)
entry_medical_history.grid(row=8, column=1, padx=10, pady=5, sticky="w")

# Entry Date and Time
ttk.Label(frame, text="Entry Date and Time:").grid(row=9, column=0, padx=10, pady=5, sticky="e")
entry_datetime = ttk.Label(frame, text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
entry_datetime.grid(row=9, column=1, padx=10, pady=5, sticky="w")

# Submit Button
submit_button = ttk.Button(frame, text="Submit", command=submit_details)
submit_button.grid(row=10, column=0, columnspan=2, pady=10)

# Center align the frame in the window
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

root.update_idletasks()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# Start the GUI event loop
root.mainloop()
