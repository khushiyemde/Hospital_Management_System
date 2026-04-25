from tkinter import *
from tkinter import ttk 
import home 
import patient_details

# Colors
BG = "#D4F1F7"
dblue = "#33526F"
lblue = "#A7E5E8"

def center_window(window, width, height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # Calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    # Set the dimensions and position of the window
    window.geometry(f'{width}x{height}+{x}+{y}')

def create_dashboard(window):
    dashboard = Toplevel(window)
    window_width = 1000
    window_height = 700
    dashboard.title("Wellstone Hospital")

    # Create a PanedWindow to divide the screen
    paned_window = PanedWindow(dashboard, orient=HORIZONTAL)
    paned_window.pack(fill=BOTH, expand=True)

    # Create a Frame for the navigation buttons on the left
    nav_frame = Frame(paned_window, bg=dblue, width=200)
    nav_frame.pack_propagate(False)  # Prevent frame from resizing to fit widgets

    # Create a Frame for the content on the right
    content_frame = Frame(paned_window, bg=BG)
    content_frame.pack(fill=BOTH, expand=True)

    # Function to show the selected tab content
    def show_tab(content):
        for widget in content_frame.winfo_children():
            widget.pack_forget()  # Hide all content frames
        content.pack(fill=BOTH, expand=True)  # Show the selected content frame

    # Create frames for each tab content
    home_tab = home.create_home_tab(content_frame)
    patient_details_tab = Frame(content_frame, bg=BG)
    appointments_tab = Frame(content_frame, bg=BG)
    billing_tab = Frame(content_frame, bg=BG)
    room_availability_tab = Frame(content_frame, bg=BG)

    # Create buttons for navigation
    buttons = [
        ("Home", home_tab),
        ("Patient Details", patient_details_tab),
        ("Appointments", appointments_tab),
        ("Billing", billing_tab),
        ("Room Availability", room_availability_tab)
    ]

    # Create buttons with slide-in animation
    def create_button(text, tab, delay):
        btn = Button(nav_frame, text=text, command=lambda: show_tab(tab), bg=lblue, fg=dblue, font=('Arial', 14), pady=10)
        nav_frame.after(delay, lambda: btn.pack(fill=X, padx=10, pady=5))

    delay = 0
    for text, tab in buttons:
        create_button(text, tab, delay)
        delay += 100  # Increase delay for each button for the slide-in effect

    # Add the PanedWindow components
    paned_window.add(nav_frame)
    paned_window.add(content_frame)

    # Add PatientDetailsApp to the patient_details_tab
    patient_details_app = patient_details.PatientDetailsApp(patient_details_tab)   

    # Center the dashboard window
    center_window(dashboard, window_width, window_height)

# Example usage
root = Tk()
root.withdraw()  # Hide the root window
create_dashboard(root)
root.mainloop()

