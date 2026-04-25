import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime
import project_data as db

class PatientDetailsWindow:
    def __init__(self, parent):
        self.parent = parent
        self.root = tk.Toplevel(parent)
        self.root.title("Patient Details Dashboard")
        self.root.configure(background='#D4F1F7')

        # Determine the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the position coordinates to center the window
        window_width = 800  # Example width
        window_height = 600  # Example height
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)

        # Set the window dimensions and position
        self.root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

        # Create a frame to hold the form elements
        self.frame = ttk.Frame(self.root, padding="20", style="TFrame")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Configure the frame background color
        style = ttk.Style()
        style.configure("TFrame", background='#D4F1F7')
        style.configure("TLabel", background='#D4F1F7')

        # Center align the frame contents
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # Add heading "Patient Details"
        heading_label = ttk.Label(self.frame, text="Patient Details", font=("Tahoma", 20, "bold"), background='#D4F1F7')
        heading_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Patient Name
        label_name = ttk.Label(self.frame, text="Patient Name:")
        label_name.grid(row=1, column=0, padx=(200, 10), pady=5, sticky="e")  # Adjust padx to center align

        self.entry_name = ttk.Entry(self.frame)
        self.entry_name.grid(row=1, column=1, padx=(0, 200), pady=5, sticky="w")  # Adjust padx to center align

        # Date of Birth
        label_dob = ttk.Label(self.frame, text="Date of Birth:")
        label_dob.grid(row=2, column=0, padx=(200, 10), pady=5, sticky="e")  # Adjust padx to center align

        self.dob_entry = DateEntry(self.frame, date_pattern='yyyy-mm-dd')
        self.dob_entry.grid(row=2, column=1, padx=(0, 200), pady=5, sticky="w")  # Adjust padx to center align

        # Age
        label_age = ttk.Label(self.frame, text="Age:")
        label_age.grid(row=3, column=0, padx=(200, 10), pady=5, sticky="e")  # Adjust padx to center align

        self.entry_age = ttk.Entry(self.frame)
        self.entry_age.grid(row=3, column=1, padx=(0, 200), pady=5, sticky="w")  # Adjust padx to center align

        # Gender
        label_gender = ttk.Label(self.frame, text="Gender:")
        label_gender.grid(row=4, column=0, padx=(200, 10), pady=5, sticky="e")  # Adjust padx to center align

        self.gender_var = tk.StringVar()
        gender_options = ["Male", "Female", "Other"]
        self.gender_menu = ttk.Combobox(self.frame, textvariable=self.gender_var, values=gender_options, width=17)
        self.gender_menu.grid(row=4, column=1, padx=(0, 200), pady=5, sticky="w")  # Adjust padx to center align

        # Blood Group
        label_blood_group = ttk.Label(self.frame, text="Blood Group:")
        label_blood_group.grid(row=5, column=0, padx=(200, 10), pady=5, sticky="e")  # Adjust padx to center align

        self.blood_group_var = tk.StringVar()
        blood_group_options = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        self.blood_group_menu = ttk.Combobox(self.frame, textvariable=self.blood_group_var, values=blood_group_options, width=17)
        self.blood_group_menu.grid(row=5, column=1, padx=(0, 200), pady=5, sticky="w")  # Adjust padx to center align

        # Phone Number
        label_phone = ttk.Label(self.frame, text="Phone Number:")
        label_phone.grid(row=6, column=0, padx=(200, 10), pady=5, sticky="e")  # Adjust padx to center align

        self.entry_phone = ttk.Entry(self.frame)
        self.entry_phone.grid(row=6, column=1, padx=(0, 200), pady=5, sticky="w")  # Adjust padx to center align

        # Email
        label_email = ttk.Label(self.frame, text="Email:")
        label_email.grid(row=7, column=0, padx=(200, 10), pady=5, sticky="e")  # Adjust padx to center align

        self.entry_email = ttk.Entry(self.frame)
        self.entry_email.grid(row=7, column=1, padx=(0, 200), pady=5, sticky="w")  # Adjust padx to center align

        # Address
        label_address = ttk.Label(self.frame, text="Address:")
        label_address.grid(row=8, column=0, padx=(200, 10), pady=5, sticky="e")  # Adjust padx to center align

        self.entry_address = tk.Text(self.frame, height=3, width=30)
        self.entry_address.grid(row=8, column=1, padx=(0, 200), pady=5, sticky="w")  # Adjust padx to center align

        # Entry Date and Time
        label_datetime = ttk.Label(self.frame, text="Entry Date and Time:")
        label_datetime.grid(row=9, column=0, padx=(200, 10), pady=5, sticky="e")  # Adjust padx to center align

        self.entry_datetime = ttk.Label(self.frame, text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.entry_datetime.grid(row=9, column=1, padx=(0, 200), pady=5, sticky="w")  # Adjust padx to center align

        # Submit Button
        submit_button = ttk.Button(self.frame, text="Submit", command=self.submit_details)
        submit_button.grid(row=10, column=0, columnspan=2, pady=10)

    def submit_details(self):
        details = {
            "Patient Name": self.entry_name.get(),
            "Date of Birth": self.dob_entry.get(),
            "Age": self.entry_age.get(),
            "Gender": self.gender_var.get(),
            "Blood Group": self.blood_group_var.get(),
            "Phone Number": self.entry_phone.get(),
            "Email": self.entry_email.get(),
            "Address": self.entry_address.get("1.0", tk.END).strip(),
            "Entry Date and Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Add details to database
        if db.addPatientDetails(details):
            messagebox.showinfo("Success", "Patient details submitted successfully")
        else:
            messagebox.showerror("Error", "Failed to submit patient details")

        # Close the window after submission
        self.root.destroy()

def main():
    root = tk.Tk()
    root.title("Main Application")
    root.geometry("800x600")  # Example dimensions for the main application window

    # Example button to open Patient Details Window
    open_details_button = ttk.Button(root, text="Open Patient Details", command=lambda: PatientDetailsWindow(root))
    open_details_button.pack(pady=20)

    #root.mainloop()
