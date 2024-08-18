import pygame  # Import the pygame library for creating the graphical interface
import random  # Import the random library to generate random numbers
import math    # Import the math library for mathematical operations
pygame.init()  # Initialize the pygame module to use its functionalities

# This class handles everything related to drawing the sorting visualizer
class DrawInformation: 
    # Define colors in RGB format
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = GREY  # Set the background color for the window

    # Padding values for the sides and top of the window
    SIDE_PAD = 100
    TOP_PAD = 150

    # Set the font for text display in the window
    FONT = pygame.font.SysFont('impact', 20)

    # Define different shades of teal for drawing the bars
    GRADIENTS = [
        (0, 128, 128), 
        (0, 150, 150),   
        (0, 180, 180)
    ]

    # Initialize the window and list
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height  
        self.window = pygame.display.set_mode((width, height))  # Set the display window size
        pygame.display.set_caption("Sorting Algorithm Visualiser")  # Set the window title
        self.set_list(lst)  # Call set_list to initialize list-related properties

    # Function to set the list and calculate properties related to drawing
    def set_list(self, lst):
        self.lst = lst  # Set the list of values to be sorted
        self.min_val = min(lst)  # Find the minimum value in the list
        self.max_val = max(lst)  # Find the maximum value in the list
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))  # Calculate the width of each bar
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))  # Calculate the height scaling factor
        self.start_x = self.SIDE_PAD // 2  # Calculate the starting x position for the first bar

# Function to generate a list of random integers
def generating_starting_list(n, min_val, max_val):
    lst = []  # Initialize an empty list

    # Generate n random integers between min_val and max_val
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)  # Append each random integer to the list

    return lst  # Return the generated list

# Function to draw the visualizer window, including text and bars
def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)  # Fill the background color of the window

    # Render the title of the algorithm being used
    title = draw_info.FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.BLACK)
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))  # Center the title at the top

    # Render the controls instructions
    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending |", 1, draw_info.WHITE)
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 45))  # Center the controls instructions

    # Render the sorting algorithm options
    sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort | H - Heap Sort | S - Selection Sort |", 1, draw_info.WHITE)
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 75))  # Center the sorting options

    draw_list(draw_info)  # Call draw_list to draw the bars representing the list values
    pygame.display.update()  # Update the display with all the new drawings

# Function to draw the list of bars in the visualizer
def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst  # Get the list of values

    if clear_bg:
        # Clear the area where the bars are drawn
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    # Draw each bar in the list
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width  # Calculate the x position of the bar
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height  # Calculate the y position of the bar

        color = draw_info.GRADIENTS[i % 3]  # Assign a color based on the bar's position

        if i in color_positions:
            color = color_positions[i]  # Override the color if specified in color_positions

        # Draw the bar as a rectangle
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height - y))

    if clear_bg:
        pygame.display.update()  # Update the display if the background was cleared

# Implementation of the Bubble Sort algorithm
def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst  # Get the list of values

    # Perform bubble sort
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            # Swap elements if they are in the wrong order
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

                # Draw the list to visualize the sorting process
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True  # Pause to allow for visual updates

    return lst  # Return the sorted list

# Implementation of the Insertion Sort algorithm
def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst  # Get the list of values

    # Perform insertion sort
    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            # If the current element is in the correct position, break the loop
            if not ascending_sort and not descending_sort:
                break

            # Shift elements to the right to make space for the current element
            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current

            # Draw the list to visualize the sorting process
            draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
            yield True  # Pause to allow for visual updates

    return lst  # Return the sorted list

# Function to maintain the heap property
def heapify(draw_info, lst, n, i, ascending=True):
    largest = i  # Assume the current element is the largest
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if the left child is larger (or smaller, depending on sorting order)
    if left < n and ((lst[left] > lst[largest] and ascending) or (lst[left] < lst[largest] and not ascending)):
        largest = left

    # Check if the right child is larger (or smaller, depending on sorting order)
    if right < n and ((lst[right] > lst[largest] and ascending) or (lst[right] < lst[largest] and not ascending)):
        largest = right

    # If the largest element is not the current element, swap them
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        
        # Draw the list to visualize the sorting process
        draw_list(draw_info, {i: draw_info.GREEN, largest: draw_info.RED}, True)
        yield True  # Pause to allow for visual updates

        # Recursively heapify the affected sub-tree
        yield from heapify(draw_info, lst, n, largest, ascending)

# Implementation of the Heap Sort algorithm
def heap_sort(draw_info, ascending=True):
    lst = draw_info.lst  # Get the list of values
    n = len(lst)

    # Build a max heap (or min heap, depending on sorting order)
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(draw_info, lst, n, i, ascending)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]  # Swap the root with the last element
        draw_list(draw_info, {0: draw_info.GREEN, i: draw_info.RED}, True)
        yield True  # Pause to allow for visual updates
        yield from heapify(draw_info, lst, i, 0, ascending)  # Heapify the reduced heap

    return lst  # Return the sorted list

# Implementation of the Selection Sort algorithm
def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst  # Get the list of values
    n = len(lst)

    # Perform selection sort
    for i in range(n):
        min_index = i
        
        # Find the minimum (or maximum) element in the remaining unsorted part
        for j in range(i + 1, n):
            if (lst[j] < lst[min_index] and ascending) or (lst[j] > lst[min_index] and not ascending):
                min_index = j
        
        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]
        
        # Draw the list to visualize the sorting process
        draw_list(draw_info, {i: draw_info.GREEN, min_index: draw_info.RED}, True)
        yield True  # Pause to allow for visual updates

    return lst  # Return the sorted list

# Main function to run the Pygame application
def main():
    run = True  # Variable to control the main loop
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate

    # Set initial parameters
    n = 50  # Number of elements in the list
    min_val = 0  # Minimum value in the list
    max_val = 100  # Maximum value in the list

    # Generate a starting list of random integers
    lst = generating_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)  # Initialize the DrawInformation object with window size and list
    sorting = False  # Flag to check if sorting is ongoing
    ascending = True  # Sorting order (ascending by default)
    sorting_algorithm = bubble_sort  # Set the initial sorting algorithm
    sorting_algo_name = "Bubble Sort"  # Name of the current sorting algorithm
    sorting_algorithm_generator = None  # Generator object to yield steps in sorting algorithm

    # Main event loop
    while run:
        clock.tick(24)  # Set the frame rate to 24 frames per second

        if sorting:
            try:
                next(sorting_algorithm_generator)  # Execute the next step in the sorting algorithm
            except StopIteration:
                sorting = False  # Stop sorting when the algorithm is complete
        else:
            draw(draw_info, sorting_algo_name, ascending)  # Draw the window

        # Handle events such as key presses and window close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user closes the window
                run = False  # Exit the main loop

            if event.type != pygame.KEYDOWN:  # If the event is not a key press
                continue  # Skip to the next event

            # Handle key press events
            if event.key == pygame.K_r:  # Reset the list
                lst = generating_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False  # Stop sorting

            elif event.key == pygame.K_SPACE and sorting == False:  # Start sorting
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)

            elif event.key == pygame.K_a and not sorting:  # Set sorting order to ascending
                ascending = True

            elif event.key == pygame.K_d and not sorting:  # Set sorting order to descending
                ascending = False

            elif event.key == pygame.K_i and not sorting:  # Set algorithm to Insertion Sort
                sorting_algorithm = insertion_sort
                sorting_algo_name = "Insertion Sort"

            elif event.key == pygame.K_b and not sorting:  # Set algorithm to Bubble Sort
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"

            elif event.key == pygame.K_h and not sorting:  # Set algorithm to Heap Sort
                sorting_algorithm = heap_sort
                sorting_algo_name = "Heap Sort"

            elif event.key == pygame.K_s and not sorting:  # Set algorithm to Selection Sort
                sorting_algorithm = selection_sort
                sorting_algo_name = "Selection Sort"

    pygame.quit()  # Quit the Pygame application

# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Call the main function
