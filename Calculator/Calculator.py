import customtkinter
from tkinter import *
from tkinter import messagebox

# Initialize the main window using customtkinter for styling
app = customtkinter.CTk()
app.title('Calculator') # Set the title of the window
app.geometry('300x350') # Set the size of the window
app.resizable(False, False)  # Prevent resizing of the window
app.config(bg='#000000') # Set the background color of the window

# Define font styles for different text elements
font1 = ('Arial',35,'bold')

def button_click(number):
    equation_entry.insert(END,number)

def clear():
    equation_entry.delete(0,END)

def calculate():
    try:
        equation = equation_entry.get()
        result = eval(equation)
        clear()
        equation_entry.insert(0,result)
    except ZeroDivisionError:
        messagebox.showerror('Error', 'Can not divide by 0!')
    except:
        messagebox.showerror('Error', 'Enter Valid Values!')

equation_entry = customtkinter.CTkEntry(app,font=font1,text_color='#FFFFFF',fg_color='#000000',border_color='#FFFFFF',width=280,height=50)
equation_entry.place(x=10,y=10)

b1_button = customtkinter.CTkButton(app,command=lambda: button_click('7'),font=font1,text_color='#FFFFFF',text='7',fg_color='#999999',hover_color='#EE0000',bg_color='#000000',cursor='hand2',width=60)
b1_button.place(x=10,y=80)

b2_button = customtkinter.CTkButton(app,command=lambda: button_click('8'),font=font1,text_color='#FFFFFF',text='8',fg_color='#999999',hover_color='#EE0000',bg_color='#000000',cursor='hand2',width=60)
b2_button.place(x=80,y=80)

b3_button = customtkinter.CTkButton(app,command=lambda: button_click('9'),font=font1,text_color='#FFFFFF',text='9',fg_color='#999999',hover_color='#EE0000',bg_color='#000000',cursor='hand2',width=60)
b3_button.place(x=150,y=80)

b4_button = customtkinter.CTkButton(app,command=lambda: button_click('4'),font=font1,text_color='#FFFFFF',text='4',fg_color='#999999',hover_color='#EE0000',bg_color='#000000',cursor='hand2',width=60)
b4_button.place(x=10,y=135)

b5_button = customtkinter.CTkButton(app,command=lambda: button_click('5'),font=font1,text_color='#FFFFFF',text='5',fg_color='#999999',hover_color='#EE0000',bg_color='#000000',cursor='hand2',width=60)
b5_button.place(x=80,y=135)

b6_button = customtkinter.CTkButton(app,command=lambda: button_click('6'),font=font1,text_color='#FFFFFF',text='6',fg_color='#999999',hover_color='#EE0000',bg_color='#000000',cursor='hand2',width=60)
b6_button.place(x=150,y=135)

b7_button = customtkinter.CTkButton(app,command=lambda: button_click('1'),font=font1,text_color='#FFFFFF',text='1',fg_color='#999999',hover_color='#EE0000',bg_color='#000000',cursor='hand2',width=60)
b7_button.place(x=10,y=190)

b8_button = customtkinter.CTkButton(app,command=lambda: button_click('2'),font=font1,text_color='#FFFFFF',text='2',fg_color='#999999',hover_color='#EE0000',bg_color='#000000',cursor='hand2',width=60)
b8_button.place(x=80,y=190)

b9_button = customtkinter.CTkButton(app,command=lambda: button_click('3'),font=font1,text_color='#FFFFFF',text='3',fg_color='#999999',hover_color='#EE0000',bg_color='#000000',cursor='hand2',width=60)
b9_button.place(x=150,y=190)

b10_button = customtkinter.CTkButton(app,command=lambda: button_click('0'),font=font1,text_color='#FFFFFF',text='0',fg_color='#999999',hover_color='#EE0000',bg_color='#000000',cursor='hand2',width=60)
b10_button.place(x=10,y=245)

b11_button = customtkinter.CTkButton(app,command=lambda: button_click('.'),font=font1,text_color='#FFFFFF',text='.',fg_color='#999999',hover_color='#EE0000',bg_color='#000000',cursor='hand2',width=60)
b11_button.place(x=80,y=245)

b12_button = customtkinter.CTkButton(app,command=clear,font=font1,text_color='#FFFFFF',text='C',fg_color='#E45A00',hover_color='#C6C6C6',bg_color='#000000',cursor='hand2',width=60)
b12_button.place(x=150,y=245)

b13_button = customtkinter.CTkButton(app,command=calculate,font=font1,text_color='#FFFFFF',text='=',fg_color='#EE0000',hover_color='#C6C6C6',bg_color='#000000',cursor='hand2',corner_radius=10,width=280)
b13_button.place(x=10,y=300)

b14_button = customtkinter.CTkButton(app,command=lambda: button_click('/'),font=font1,text_color='#FFFFFF',text='/',fg_color='#5AE804',hover_color='#C6C6C6',bg_color='#000000',cursor='hand2',width=70)
b14_button.place(x=220,y=80)

b15_button = customtkinter.CTkButton(app,command=lambda: button_click('*'),font=font1,text_color='#FFFFFF',text='*',fg_color='#5AE804',hover_color='#C6C6C6',bg_color='#000000',cursor='hand2',width=70)
b15_button.place(x=220,y=135)

b16_button = customtkinter.CTkButton(app,command=lambda: button_click('-'),font=font1,text_color='#FFFFFF',text='-',fg_color='#5AE804',hover_color='#C6C6C6',bg_color='#000000',cursor='hand2',width=70)
b16_button.place(x=220,y=190)

b17_button = customtkinter.CTkButton(app,command=lambda: button_click('+'),font=font1,text_color='#FFFFFF',text='+',fg_color='#5AE804',hover_color='#C6C6C6',bg_color='#000000',cursor='hand2',width=70)
b17_button.place(x=220,y=245)



app.mainloop()