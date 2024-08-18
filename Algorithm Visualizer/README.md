**Sorting Algorithm Visualizer**

This project is a Python-based visualizer for various sorting algorithms. It allows users to see how different algorithms work in real-time as they sort a list of numbers. The visualizer is built using the pygame library, which provides the graphical interface for the visualization.

**Features**

- Real-time Visualization: Watch sorting algorithms as they sort the list step-by-step.
- Multiple Algorithms: Includes Bubble Sort, Insertion Sort, Heap Sort, and Selection Sort.
- Interactive Controls: Start/stop sorting, reset the list, and choose sorting order (ascending/descending).
- Dynamic List Generation: Generates a random list of numbers with customizable size and range.

Getting Started - Prerequisites
- Python 3.x
- pygame library

Installing pygame
You can install pygame using pip:

"pip install pygame"

**Controls**

- R: Reset the list with new random values.
- SPACE: Start or pause the sorting process.
- A: Set sorting order to Ascending.
- D: Set sorting order to Descending.
- I: Use Insertion Sort.
- B: Use Bubble Sort.
- H: Use Heap Sort.
- S: Use Selection Sort.
 
**Visualized Algorithms**

- Bubble Sort: A simple comparison-based algorithm where adjacent elements are swapped if they are in the wrong order. The process repeats until the list is sorted.

- Insertion Sort: Builds the sorted list one element at a time by repeatedly picking the next element and inserting it into its correct position.

- Heap Sort: Converts the list into a heap structure, then repeatedly extracts the maximum element and places it at the end of the list.

- Selection Sort: Repeatedly selects the minimum element from the unsorted portion of the list and swaps it with the first unsorted element.

**How It Works**

The visualizer displays a graphical representation of the list of numbers as vertical bars of varying heights. The height of each bar corresponds to the value of the element in the list. As the algorithm processes the list, the bars are colored to show which elements are being compared, swapped, or moved.

- Green: The current elements being swapped.
- Red: The elements that have just been compared.
  
**Code Structure**

- DrawInformation Class: Handles all the graphical rendering and window management.
- Sorting Functions: Implementations of different sorting algorithms. These functions use Python generators (yield) to pause and resume execution, allowing the visualizer to update the display after each operation.
- Main Loop: Manages user input, controls the sorting process, and updates the display.
