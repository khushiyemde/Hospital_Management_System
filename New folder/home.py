from tkinter import *

def create_home_tab(notebook):
    home_tab = Frame(notebook)
    
    # content for the home tab
    home_label = Label(home_tab, text="Welcome to Wellstone Hospital", font=('Ariel', 24, 'bold'))
    home_label.pack(pady=20)
    
    # Placeholder for the image
    home_image = Label(home_tab)
    home_image.pack(pady=20)
    
    # load and display the image
    def show_image(event):
        selected_tab = event.widget.tab(event.widget.index("current"))["text"]
        if selected_tab == "Home":
            image = PhotoImage(file="abc.png")  # Replace 'hospital.png' with your image file
            home_image.config(image=image)
            home_image.image = image  # Keep a reference to avoid garbage collection
    
    # tab selection event to the show_image function
    notebook.bind("<<NotebookTabChanged>>", show_image)

    # Return the home tab frame
    return home_tab

