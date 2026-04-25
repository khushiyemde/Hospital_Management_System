import tkinter as tk
from tkinter import font

class WellstoneHospitalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Wellstone Hospital")
        self.geometry("800x600")
        self.resizable(width = False, height = False)

        # Load the new background image
        self.bg_image = tk.PhotoImage(file="clipart.png")

        # Create canvas to draw shapes and text
        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)

        # Get the dimensions of the image and the window
        self.bg_width = self.bg_image.width()
        self.bg_height = self.bg_image.height()
        self.window_width = 800
        self.window_height = 600

        # Calculate the position to center the image
        self.bg_x = (self.window_width - self.bg_width) // 2
        self.bg_y = (self.window_height - self.bg_height) // 2

        # Display background image centered
        self.canvas.create_image(self.bg_x, self.bg_y, image=self.bg_image, anchor="nw")

        # Draw the interface
        self.create_interface()

    def create_interface(self):
        # Custom font
        title_font = font.Font(family="Helvetica", size=32, weight="bold")
        button_font = font.Font(family="Helvetica", size=16, weight="bold")

        # Title
        self.canvas.create_text(400, 50, text="Wellstone Hospital", font=title_font, fill="#E283FF")

        # Draw buttons
        self.create_rounded_rectangle(50, 130, 250, 180, 20, "#AAC4F4", "Patient Details", button_font, self.show_patient_details)
        self.create_rounded_rectangle(80, 380, 280, 430, 22, "#FFFFFF", "Room Allocation", button_font, self.room_allocation)
        self.create_rounded_rectangle(520, 130, 720, 180, 22, "#FFFFFF", "Book Appointment", button_font, self.book_appointment)
        self.create_rounded_rectangle(520, 380, 720, 430, 22, "#AAC4F4", "Billing", button_font, self.billing)


    def create_rounded_rectangle(self, x1, y1, x2, y2, radius, color, text, font, command):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        self.canvas.create_polygon(points, smooth=True, fill=color, outline=color)
        button = tk.Button(self, text=text, font=font, bg=color, fg="#000000", activebackground=color, activeforeground="#000000", borderwidth=0, command=command)
        button_window = self.canvas.create_window((x1+x2)//2, (y1+y2)//2, window=button, anchor="center")

    def show_patient_details(self):
        print("Patient Details")

    def book_appointment(self):
        print("Book Appointment")

    def room_allocation(self):
        print("Room Allocation")

    def billing(self):
        print("Billing")

if __name__ == "__main__":
    app = WellstoneHospitalApp()
    app.mainloop()
