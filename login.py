from tkinter import *
from tkinter import messagebox

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

def login(event=None):
    username = user.get()
    password_text = password.get()
    if username == 'Admin' and password_text == '1234':
        messagebox.showinfo("Success", "Congrats!!\nWelcome")
        window.destroy()  # Close the login window
        import dashboard  # Import the main dashboard here
        dashboard.launch_dashboard()  # Launch the main dashboard
    else:
        messagebox.showerror("Fail", "Try again")

# Create the main window
window = Tk()
window.title("Healthcare")

# Set the desired window size
window_width = 550
window_height = 300

# Center the window
center_window(window, window_width, window_height)

# Images
icon = PhotoImage(file="logo1.png")
window.iconphoto(True, icon)
photo = PhotoImage(file='doctor.png')

# Window config
window.configure(bg=BG)
window.geometry(f"{window_width}x{window_height}")
window.resizable(width=False, height=False)

# Doctor clip art
label1 = Label(window, image=photo, bg=BG, width=200, height=200)
label1.grid(row=0, column=1, rowspan=3, padx=20, pady=30)

# Sign-in details frame
frame = Frame(window, width=300, height=270, bg=BG)
frame.grid(row=0, column=0, padx=20, pady=20, rowspan=3)

heading = Label(frame, text="Sign in", fg=dblue, bg=BG, font=('Ariel', 24, 'bold'))
heading.grid(row=0, column=0, columnspan=2, pady=10)

# Placeholder functions for user entry
def on_enter_user(e):
    if user.get() == 'enter name':
        user.delete(0, 'end')
        user.config(fg=dblue)

def on_leave_user(e):
    if user.get() == '':
        user.insert(0, 'enter name')
        user.config(fg=dblue)

# User entry
user = Entry(frame, width=25, fg=dblue, bg=lblue, border=0, font=('Ariel', 14))
user.grid(row=1, column=0, padx=10, pady=(10, 5))
user.insert(0, 'enter name')
user.bind("<FocusIn>", on_enter_user)
user.bind("<FocusOut>", on_leave_user)

# Placeholder functions for password entry
def on_enter_password(e):
    if password.get() == 'enter password':
        password.delete(0, 'end')
        password.config(fg=dblue, show='*')

def on_leave_password(e):
    if password.get() == '':
        password.insert(0, 'enter password')
        password.config(fg=dblue, show='')

# Password entry
password = Entry(frame, width=25, fg=dblue, bg=lblue, border=0, font=('Ariel', 14))
password.grid(row=2, column=0, padx=10, pady=(10, 5))
password.insert(0, 'enter password')
password.bind("<FocusIn>", on_enter_password)
password.bind("<FocusOut>", on_leave_password)

# Sign In button
login_button = Button(frame, text='login', fg=lblue, bg=dblue, font=('Ariel', 14), border=0, command=login)
login_button.grid(row=3, column=0, padx=10, pady=(20, 10))

# Bind the Enter key to the login function
window.bind('<Return>', login)

# Run the application
window.mainloop()


