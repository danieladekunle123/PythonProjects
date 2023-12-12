import customtkinter
from tkinter import *
from tkinter import messagebox

class TodoApp: # This class encapsulates the entire To-do application
    def __init__(self): # Initialize the main application window and GUI components
        self.app = customtkinter.CTk() # Create the main application window
        self.app.title('Daniel\'s TO-DO List') # Set the title of the window
        self.app.geometry('500x750') # Set the size of the window
        self.app.config(bg='#B2B2B2') # Configure the background color of the window
        self.app.resizable(False, False)  # Prevent window from being resizable

        # Define font styles for different text elements
        font1 = ('Arial', 35, 'bold')
        font2 = ('Arial', 20, 'bold')
        font3 = ('Arial', 10, 'bold')

        self.title_label = customtkinter.CTkLabel(self.app, font=font1, text='Daniel\'s TO-DO List', text_color='#FFFFFF', bg_color='#B2B2B2')
        # Create the title label
        self.title_label.place(x=90, y=20)


        self.add_button = customtkinter.CTkButton(self.app, command=self.add_task, font=font2, text_color='#FFFFFF', text='Append Task', fg_color='#06911f', hover_color='#6ff55b', bg_color='#B2B2B2', cursor='hand2', corner_radius=10, width=120)
        # Create the 'Append Task' button
        self.add_button.place(x=95, y=80)

        self.remove_button = customtkinter.CTkButton(self.app, command=self.remove_task, font=font2, text_color='#FFFFFF', text='Remove Task', fg_color='#ff0000', hover_color='#ff4d4d', bg_color='#B2B2B2', cursor='hand2', corner_radius=10, width=120)
        # Create the 'Remove Task' button
        self.remove_button.place(x=255, y=80)

        self.task_entry = customtkinter.CTkEntry(self.app, font=font2, text_color='#000000', fg_color='#FFFFFF', border_color='#000000', width=350)
        # Create the entry field for adding new tasks
        self.task_entry.place(x=77, y=120)

        self.tasks_list = Listbox(self.app, width=60, height=25, font=font3)
        # Create the listbox to display tasks
        self.tasks_list.place(x=39, y=170)

        self.load_tasks()

        self.app.mainloop()
        # Start the main loop to run the application

    def add_task(self):
        # Method to add a new task to the list
        task = self.task_entry.get()
        if task:
            self.tasks_list.insert(0, task)
            self.task_entry.delete(0, END)
            self.save_tasks()
        else:
            messagebox.showerror('Error', 'You must Enter A Task To Add')

    def remove_task(self):
        # Method to remove a selected task from the list
        selected = self.tasks_list.curselection()
        if selected:
            self.tasks_list.delete(selected[0])
            self.save_tasks()
        else:
            messagebox.showerror('Error', 'You must Select A Task To Delete')

    def save_tasks(self):
        # Method to save tasks to a file
        with open("tasks.txt", "w") as f:
            tasks = self.tasks_list.get(0, END)
            for task in tasks:
                f.write(task + "\n")

    def load_tasks(self):
        # Method to load tasks from a file
        try:
            with open("tasks.txt", "r") as f:
                tasks = f.readlines()
                for task in tasks:
                    self.tasks_list.insert(0, task.strip())
        except FileNotFoundError:
            pass

# Run the app
if __name__ == "__main__":
    TodoApp()
# This block ensures the app runs only when executed as a script