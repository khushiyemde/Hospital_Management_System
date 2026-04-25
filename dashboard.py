# wellstone_hospital.py

import tkinter as tk
from tkinter import font, PhotoImage
from tkinter import ttk
from final_patientdetail import PatientDetailsWindow  # Importing PatientDetailsWindow class
import room  # Assuming you have a room module for room allocation


class WellstoneHospitalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Wellstone Hospital")
        self.geometry("800x600")
        self.resizable(width=False, height=False)
        self.center_window()

        # Load the background image
        self.bg_image = PhotoImage(file="clipart.png")

        # Create canvas to draw shapes and text
        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)

        # Display background image centered
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        # Draw the interface
        self.create_interface()

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_interface(self):
        # Custom font
        title_font = font.Font(family="Tahoma", size=32, weight="bold")
        button_font = font.Font(family="Helvetica", size=16, weight="bold")

        # Title
        self.canvas.create_text(400, 50, text="Wellstone Hospital", font=title_font, fill="#18264D")

        # Draw buttons with rounded rectangles
        self.create_rounded_rectangle(50, 130, 250, 180, 20, "#479CAD", "Patient Details", button_font, self.show_patient_details)
        self.create_rounded_rectangle(80, 380, 280, 430, 22, "#FFFFFF", "Room Allocation", button_font, self.room_allocation)
        self.create_rounded_rectangle(520, 130, 720, 180, 22, "#FFFFFF", "Book Appointment", button_font, self.book_appointment)
        self.create_rounded_rectangle(520, 380, 720, 430, 22, "#479CAD", "Billing", button_font, self.billing)

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius, color, text, font, command):
        points = [x1 + radius, y1,
                  x1 + radius, y1,
                  x2 - radius, y1,
                  x2 - radius, y1,
                  x2, y1,
                  x2, y1 + radius,
                  x2, y1 + radius,
                  x2, y2 - radius,
                  x2, y2 - radius,
                  x2, y2,
                  x2 - radius, y2,
                  x2 - radius, y2,
                  x1 + radius, y2,
                  x1 + radius, y2,
                  x1, y2,
                  x1, y2 - radius,
                  x1, y2 - radius,
                  x1, y1 + radius,
                  x1, y1 + radius,
                  x1, y1]

        self.canvas.create_polygon(points, smooth=True, fill=color, outline=color)
        button = tk.Button(self, text=text, font=font, bg=color, fg="#000000", activebackground=color,
                           activeforeground="#000000", borderwidth=0, command=command)
        self.canvas.create_window((x1 + x2) // 2, (y1 + y2) // 2, window=button, anchor="center")

    def show_patient_details(self):
        # Open Patient Details Window
        PatientDetailsWindow(self)

    def book_appointment(self):
        # Replace with code to handle booking an appointment
        print("Book Appointment")

    def room_allocation(self):
        room.show_room_ui(self)
        
    def billing(self):
        # Replace with code to handle billing
        print("Billing")

def launch_dashboard():
    app = WellstoneHospitalApp()
    app.mainloop()

if __name__ == "__main__":
    launch_dashboard()


