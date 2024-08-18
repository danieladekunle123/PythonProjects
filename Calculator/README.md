# Customtkinter Calculator

This project is a simple graphical calculator built using Python's `customtkinter` library, which extends the capabilities of the traditional `tkinter` library. The calculator supports basic arithmetic operations and provides a sleek interface suitable for general use.

## Features

- **Sleek Interface**: Utilizes `customtkinter` for a modern look and responsive design.
- **Basic Arithmetic**: Supports addition, subtraction, multiplication, division, and decimal inputs.
- **Error Handling**: Includes error notifications for invalid inputs or mathematical errors, such as division by zero.

## Getting Started

### Prerequisites

- Python 3.x
- `customtkinter` library

### Installing customtkinter

To install `customtkinter`, run the following command in your terminal:

```bash
pip install customtkinter
```

## Usage

Once the application is running, you will see a simple calculator interface with numbered buttons from 0 to 9, operation buttons (`+`, `-`, `*`, `/`), a decimal point (`.`), and an equals button (`=`) for calculations. There is also a clear button (`C`) to reset the current input.

## Controls

- **Number Buttons (0-9)**: Input numerical values.
- **Operation Buttons (+, -, *, /)**: Specify the arithmetic operation to perform.
- **Decimal Button (.)**: Include decimal points in numerical entries.
- **Equals Button (=)**: Compute the entered equation.
- **Clear Button (C)**: Clear the current equation or result.

## Functionality

- **Input Numbers**: Click the number buttons to form a number.
- **Choose Operation**: Click an operation button after entering the first number.
- **Enter Second Number**: Input the second number.
- **Compute**: Press the equals button to perform the calculation.
- **Clear**: To start a new calculation, press the `C` button.

## Code Structure

- **Button Functions**: Functions tied to buttons (`button_click`, `clear`, `calculate`) to handle interactions.
- **GUI Setup**: Defines and positions buttons and entry widgets using `customtkinter`.
- **Event Handling**: Uses the mainloop of `tkinter` to handle user interactions.

## Error Handling

- Handles division by zero and invalid values by displaying error messages.

## Conclusion

This calculator is designed for ease of use with a clear, straightforward interface, suitable for everyday arithmetic tasks.
