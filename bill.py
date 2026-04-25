import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Function to calculate total bill
def calculate_bill():
    try:
        room_charge = float(room_charge_entry.get())
        medicine_charge = float(medicine_charge_entry.get())
        lab_charge = float(lab_charge_entry.get())
        insurance_cover = float(insurance_cover_entry.get())
        
        total_charge = room_charge + medicine_charge + lab_charge - insurance_cover
        total_charge_label.config(text=f'Total Bill: Rs {total_charge:.2f}')
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for charges.")

# Function to generate invoice and display in notepad
def generate_invoice():
    patient_name = patient_name_entry.get()
    patient_id = patient_id_entry.get()
    admit_date = admit_date_entry.get()
    discharge_date = discharge_date_entry.get()
    room_charge = room_charge_entry.get()
    medicine_charge = medicine_charge_entry.get()
    lab_charge = lab_charge_entry.get()
    insurance_cover = insurance_cover_entry.get()
    total_charge = total_charge_label.cget("text")

    invoice_text = (f"Wellstone Hospital\n"
                    f"Touch of Care\n"
                    f"-------------------------------------------\n"
                    f"Patient Name: {patient_name}\n"
                    f"Patient ID: {patient_id}\n"
                    f"Admit Date: {admit_date}\n"
                    f"Discharge Date: {discharge_date}\n\n"
                    f"Room Charges: Rs {room_charge}\n"
                    f"Medicine Charges: Rs {medicine_charge}\n"
                    f"Lab Charges: Rs {lab_charge}\n\n"
                    f"Insurance Cover: Rs {insurance_cover}\n\n"
                    f"{total_charge}")

    # Clear previous text
    invoice_text_widget.delete(1.0, tk.END)
    # Insert new invoice text
    invoice_text_widget.insert(tk.END, invoice_text)

# Create main window
root = tk.Tk()
root.title("Wellstone Hospital")

# Set initial window size and position
window_width = 1366
window_height = 768
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

root.resizable(width=False, height=False)
root.configure(bg="#F0F0F0") 

def logout(event=None):
    result = messagebox.askyesno("Logout", "Are you sure you want to exit?")
    if result:
        root.destroy()

# Create menubar
menubar = tk.Menu(root)

homemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Home", menu=homemenu)
homemenu.add_command(label="Patient Details")
homemenu.add_command(label="Availability")
homemenu.add_separator()
homemenu.add_command(label="Exit", command=logout)

aboutusmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="About Us", menu=aboutusmenu)

supportmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Support", menu=supportmenu)

contactmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Contact", menu=contactmenu)

root.config(menu=menubar)

# Create a style for the widgets
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TEntry", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 12), background="#F0F0F0")
style.configure("TLabelframe.Label", font=("Helvetica", 14, "bold"), background="#F0F0F0")
style.configure("TLabelframe", background="#F0F0F0", padding=10)

# Create and configure widgets directly on the root window

# Patient Information Section
patient_info_frame = ttk.LabelFrame(root, text="Patient Information", padding=(20, 10))
patient_info_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

ttk.Label(patient_info_frame, text="Patient Name:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
patient_name_entry = ttk.Entry(patient_info_frame, width=30)
patient_name_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(patient_info_frame, text="Patient ID:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
patient_id_entry = ttk.Entry(patient_info_frame, width=30)
patient_id_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(patient_info_frame, text="Admit Date :").grid(row=2, column=0, sticky="w", padx=10, pady=5)
admit_date_entry = DateEntry(patient_info_frame, width=28, background='darkblue', foreground='white', borderwidth=2, date_pattern='y-mm-dd')
admit_date_entry.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(patient_info_frame, text="Discharge Date:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
discharge_date_entry = DateEntry(patient_info_frame, width=28, background='darkblue', foreground='white', borderwidth=2, date_pattern='y-mm-dd')
discharge_date_entry.grid(row=3, column=1, padx=10, pady=5)

# Charges Section
charges_frame = ttk.LabelFrame(root, text="Charges", padding=(20, 10))
charges_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

ttk.Label(charges_frame, text="Room Charges (Rs): ").grid(row=0, column=0, sticky="w", padx=10, pady=5)
room_charge_entry = ttk.Entry(charges_frame, width=20)
room_charge_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(charges_frame, text="Medicine Charges (Rs): ").grid(row=1, column=0, sticky="w", padx=10, pady=5)
medicine_charge_entry = ttk.Entry(charges_frame, width=20)
medicine_charge_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(charges_frame, text="Lab Charges (Rs): ").grid(row=2, column=0, sticky="w", padx=10, pady=5)
lab_charge_entry = ttk.Entry(charges_frame, width=20)
lab_charge_entry.grid(row=2, column=1, padx=10, pady=5)

# Insurance Section
insurance_frame = ttk.LabelFrame(root, text="Insurance", padding=(20, 10))
insurance_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

ttk.Label(insurance_frame, text="Insurance:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
insurance_options = ["Yes", "No"]
insurance_var = tk.StringVar(value=insurance_options[0])
insurance_menu = ttk.Combobox(insurance_frame, textvariable=insurance_var, values=insurance_options, state="readonly")
insurance_menu.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(insurance_frame, text="Insurance Name : ").grid(row=1, column=0, sticky="w", padx=10, pady=5)
insurance_name_entry = ttk.Entry(insurance_frame, width=20)
insurance_name_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(insurance_frame, text="Insurance Cover (Rs): ").grid(row=2, column=0, sticky="w", padx=10, pady=5)
insurance_cover_entry = ttk.Entry(insurance_frame, width=20)
insurance_cover_entry.grid(row=2, column=1, padx=10, pady=5)

# Buttons
calculate_button = ttk.Button(root, text="Calculate Bill", command=calculate_bill)
calculate_button.grid(row=3, column=0, pady=10, padx=20, sticky="ew")

# Total Bill Label
total_charge_label = ttk.Label(root, text="Total Bill: Rs 0.00")
total_charge_label.grid(row=4, column=0, padx=20, pady=10)

# Generate Invoice Button
generate_button = ttk.Button(root, text="Generate Invoice", command=generate_invoice)
generate_button.grid(row=5, column=0, pady=10, padx=20, sticky="ew")

# Invoice Text Display Section (Text widget) integrated into the main window
invoice_text_widget = tk.Text(root, wrap="word", font=("Helvetica", 12), padx=10, pady=10)
invoice_text_widget.grid(row=0, column=1, rowspan=6, padx=20, pady=20, sticky="nsew")

# Configure grid weights to make widgets resize properly
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)

# Start the Tkinter event loop
root.mainloop()
