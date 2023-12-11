import customtkinter
from tkinter import *
from tkinter import messagebox

# Initialize the main window using customtkinter for styling
app = customtkinter.CTk()
app.title('The Ultimate Unit Converter') # Set the title of the window
app.geometry('500x500') # Set the size of the window
app.config(bg='#454545') # Set the background color of the window

# Define font styles for different text elements
font1 = ('Arial',35,'bold')
font2 = ('Arial',25,'bold')
font3 = ('Arial',10,'bold')

# Define options for unit conversion dropdown menus
unit_options = ['Length','Mass']
length_options = ['Meter','Centimeter','Foot','Kilometer','Miles','Inches']
mass_options = ['Kilogram','Gram','Pound','Ounce']

# Create StringVar objects for storing selected values from dropdown menus
variable1 = StringVar()
variable2 = StringVar()
variable3 = StringVar()

# Function to perform the unit conversion
def convert():
    # Define conversion factors for length and mass units
    length_factors = {'Meter':1, 'Centimeter': 0.01,'Foot': 0.3048, 'Kilometer': 1000, 'Miles':1609.34, 'Inches':0.0254 }
    mass_factors = {'Kilogram': 1, 'Gram': 0.001, 'Pound': 0.453592, 'Ounce': 0.02835 }
    try:
        # Perform conversion based on selected unit type (length or mass)
        if variable1.get() == 'Length':
            meters = float(value_entry.get()) * length_factors[variable2.get()]
            # Converts From Meters To The Desired Unit
            converted_value = meters / length_factors[variable3.get()]
        else:
            kilograms = float(value_entry.get()) * mass_factors[variable2.get()]
            # Converts From Kilograms To The Desired Unit
            converted_value = kilograms / mass_factors[variable3.get()]

        # Update result label with the converted value
        result_label.configure(text=f'{value_entry.get()} {variable2.get()} = {converted_value:.2f} {variable3.get()}')
    except:
        # Display an error message if invalid input is provided
        messagebox.showerror('Error', 'Enter Valid values Only!')

# Create and position various widgets (labels, dropdown menus, buttons, etc.)
title_label = customtkinter.CTkLabel(app,font=font1,text='The Ultimate Unit Converter',text_color='#FFFFFF',bg_color='#454545')
title_label.place(x=22,y=20)

unit_label = customtkinter.CTkLabel(app,font=font2,text='Unit',text_color='#FFFFFF',bg_color='#454545')
unit_label.place(x=180,y=100)

unit_option = customtkinter.CTkComboBox(app,font=font3,text_color='#000000',fg_color='#FFFFFF',dropdown_hover_color='#C6C6C6',values=unit_options,variable=variable1,width=120)
unit_option.place(x=180,y=130)

from_label = customtkinter.CTkLabel(app,font=font2,text='From',text_color='#FFFFFF',bg_color='#454545')
from_label.place(x=20,y=180)

from_option = customtkinter.CTkComboBox(app,font=font3,text_color='#000000',fg_color='#FFFFFF',dropdown_hover_color='#C6C6C6',variable=variable2,width=120)
from_option.place(x=20,y=210)

to_label = customtkinter.CTkLabel(app,font=font2,text='To',text_color='#FFFFFF',bg_color='#454545')
to_label.place(x=180,y=180)

to_option = customtkinter.CTkComboBox(app,font=font3,text_color='#000000',fg_color='#FFFFFF',dropdown_hover_color='#C6C6C6',variable=variable3,width=120)
to_option.place(x=180,y=210)

value_label = customtkinter.CTkLabel(app,font=font2,text='Value',text_color='#FFFFFF',bg_color='#454545')
value_label.place(x=340,y=180)

value_entry = customtkinter.CTkEntry(app,font=font3,text_color='#000000',fg_color='#FFFFFF',border_color='#FFFFFF',width=150)
value_entry.place(x=340,y=210)

convert_button = customtkinter.CTkButton(app,command=convert,font=font2,text_color='#FFFFFF',text='Convert',fg_color='#EE0000',hover_color='#C6C6C6',bg_color='#454545',cursor='hand2',corner_radius=10,width=200)
convert_button.place(x=150,y=280)

# Create a frame for the result label without setting the background color
result_frame = customtkinter.CTkFrame(app)
result_frame.pack(fill='x', pady=(350, 0))  # Fill in the x-direction and add some padding on the y-axis

# Create the result label and pack it inside the result frame
result_label = customtkinter.CTkLabel(result_frame, text='', font=font2, text_color='#FFFFFF', bg_color='#454545')
result_label.pack()


# Function to update dropdown options based on selected unit type
def update_options(*args):
    if variable1.get() == 'Length':
        from_option.configure(values=length_options)
        to_option.configure(values=length_options)
        from_option.set('Meter')
        to_option.set('Centimeter')
    else:
        from_option.configure(values=mass_options)
        to_option.configure(values=mass_options)
        from_option.set('Kilogram')
        to_option.set('Gram')

# Set a trace on variable1 to call update_options function whenever it changes
variable1.trace("w",update_options)

# Start the main loop of the application
app.mainloop()

