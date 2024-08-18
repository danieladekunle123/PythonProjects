# Daniel's TO-DO List Application

This project is a simple graphical to-do list application built using Python's `customtkinter` library. It allows users to add, remove, and manage tasks in a user-friendly interface.

## Features

- **Graphical Interface**: Built using `customtkinter` for modern and appealing styling.
- **Add Tasks**: Users can add tasks to their to-do list.
- **Remove Tasks**: Users can remove completed or unwanted tasks.
- **Persistence**: Tasks are saved to a file, allowing them to persist between application restarts.
- **Error Handling**: Provides feedback if users try to add an empty task or remove an unselected task.

## Getting Started

### Prerequisites

- Python 3.x
- `customtkinter` library

### Installing customtkinter

To install the `customtkinter` library, run the following command:

```bash
pip install customtkinter
```

## Usage

When you run the application, you will be presented with a window titled **"Daniel's TO-DO List."** The window will allow you to:

- **Add a Task**: Enter a task in the text field and click the 'Append Task' button.
- **Remove a Task**: Select a task from the list and click the 'Remove Task' button.

## Controls

- **Append Task Button**: Click to add the entered task to the list.
- **Remove Task Button**: Click to remove the selected task from the list.
- **Task Entry**: Enter the text for a new task here.
- **Tasks List**: Displays the current list of tasks. Click to select a task.

## Functionality

- **Adding Tasks**: Tasks are added to the top of the list and saved in a file.
- **Removing Tasks**: Selected tasks can be removed by the user. The list updates immediately.
- **Loading Tasks**: When the application starts, it loads existing tasks from a file.

## Code Structure

- **TodoApp Class**: Manages the creation and operation of the to-do list GUI.
- **add_task Method**: Adds a new task to the list.
- **remove_task Method**: Removes the selected task from the list.
- **save_tasks Method**: Saves all current tasks to a file.
- **load_tasks Method**: Loads tasks from a file at application startup.

## Error Handling

- **Add Task**: If an empty task is entered, an error message is shown.
- **Remove Task**: If no task is selected for deletion, an error message is shown.

## Conclusion

Daniel's TO-DO List application is designed to be straightforward and easy to use, making task management simple and effective for everyday use.
