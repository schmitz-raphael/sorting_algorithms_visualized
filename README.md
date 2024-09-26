# Sorting Algorithm Visualizer

## Overview

This Python project visualizes various sorting algorithms using Pygame. The program generates a random array of integers and animates the sorting process, providing a graphical representation of how each algorithm operates. It's an interactive tool designed for learning and exploring sorting algorithms.

## Features

- **Sorting Algorithms Included:**
  - Bubble Sort
  - Selection Sort
  - Insertion Sort
  - Quick Sort
  - Heap Sort
  - Bogo Sort (for fun!)
  - Stalin sort (also for fun!)

- **Visual Interactivity:**
  - Select any sorting algorithm by hovering over and clicking the buttons.
  - Real-time visualization of the array being sorted.
  - Displays the number of comparisons made during sorting.
  
## Installation

1. Clone the repository or download the ZIP file.
   
   ```bash
   git clone https://github.com/your-username/sorting-visualizer.git

2. Install the required dependencies:
   ```bash
   pip install pygame

3. Run the program:
   ```bash
    python sorting_visualizer.py

## How to use

1. Run the program, and a window will open with 6 buttons, each corresponding to a different sorting algorithm.

2. Move your mouse over the buttons to highlight them, then click to start the sorting visualization.

3. Watch the algorithm sort the array and keep track of the number of comparisons in the window title bar.
    Bubble Sort: Classic bubble sort with adjacent element swaps.
    Selection Sort: Selection of the smallest element in each pass.
    Insertion Sort: Sorting by shifting and inserting elements in order.
    Quick Sort: Divide-and-conquer using a pivot for partitioning.
    Heap Sort: Builds a heap and sorts by extracting max/min values.
    (Bogo Sort: Randomly shuffles the array until sorted, Stalin Sort: Replaces all values with the value of the first element)
   
4. To exit, simply close the window.

##Requirements
  Python 3.x
  Pygame (install via pip)

##Future Improvements
  - clean up the code
  - improve UX by making the length of the array variable (it's hard-coded atm)
  - fix some bugs
