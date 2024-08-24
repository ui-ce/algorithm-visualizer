"""
    <Python library for visualizing data structure algorithms by generating latex output.>
    Copyright (C) 2024  Yasamin Akbari and Mahroo Noohi

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
# BubbleSort/latex_generator.py
def generate_latex_code(array, primary_color, secondary_color, steps_per_page=5, vertical_spacing=2):
    steps = []
    n = len(array)
    latex_code = r"""
\documentclass[a4paper]{article}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage{listings}
\usepackage{amsmath}
\usepackage{geometry}

\geometry{a4paper, margin=1in}

\title{Bubble Sort Visualization}
\author{Author Name}
\date{\today}

\begin{document}
\maketitle

\section*{Bubble Sort Algorithm}
Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

\section*{Python Implementation}

\begin{lstlisting}[language=Python]
def bubble_sort(arr):
    n = len(arr)
    steps = []
    for i in range(n):
        for j in range(0, n-i-1):
            step = list(arr)
            steps.append((step, j, j+1, False))
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                step = list(arr)
                steps.append((step, j, j+1, True))
    return arr, steps

arr = [7, 4, 5, 2]
sorted_arr = [2, 4, 5, 7]
\end{lstlisting}

\section*{Visualization}

The following pages provide a visual representation of the Bubble Sort algorithm. Each page contains a series of snapshots taken during the sorting process. Here's how to interpret the visualizations:

\begin{itemize}
    \item \textbf{Array Elements}: Each element of the array is represented by a rectangle. The value of the element is displayed inside the rectangle.
    \item \textbf{Primary and Secondary Colors}: During each step of the sorting process, two elements are compared. The primary color highlights the first element being compared, and the secondary color highlights the second element being compared. If a swap occurs, these colors help indicate which elements were involved in the swap.
    \item \textbf{Rectangles and Spacing}: The rectangles are positioned along the horizontal axis, with each rectangle representing an array element. The vertical position of the rectangles changes with each step to show the progress of the algorithm.
    \item \textbf{Swapping Indication}: If a swap occurs between the elements highlighted by the primary and secondary colors, the rectangles will be updated to reflect this change in the subsequent snapshots.
\end{itemize}

"""

    array_copy = list(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            step = list(array_copy)
            steps.append((step, j, j + 1, False))
            if array_copy[j] > array_copy[j + 1]:
                array_copy[j], array_copy[j + 1] = array_copy[j + 1], array_copy[j]
                step = list(array_copy)
                steps.append((step, j, j + 1, True))

    step_num = 0
    total_steps = len(steps)
    for i in range(0, total_steps, steps_per_page):
        latex_code += r"""
        
\newpage
\begin{center}
\begin{tikzpicture}[scale=0.8, every node/.style={scale=0.8}]
"""
        for j in range(i, min(i + steps_per_page, total_steps)):
            step, idx1, idx2, swapped = steps[j]
            y_pos = -j + i
            latex_code += f"\\fill[{primary_color}] ({idx1 * 1.5}, {y_pos * vertical_spacing}) rectangle ({(idx1 + 1) * 1.5}, {y_pos * vertical_spacing + 1});\n"
            latex_code += f"\\fill[{secondary_color}] ({idx2 * 1.5}, {y_pos * vertical_spacing}) rectangle ({(idx2 + 1) * 1.5}, {y_pos * vertical_spacing + 1});\n"
            for k, val in enumerate(step):
                latex_code += f"\\node at ({k * 1.5 + 0.75}, {y_pos * vertical_spacing + 0.5}) {{{val}}};\n"
                latex_code += f"\\draw ({k * 1.5}, {y_pos * vertical_spacing}) rectangle ({(k + 1) * 1.5}, {y_pos * vertical_spacing + 1});\n"
            step_num += 1

        latex_code += r"""
\end{tikzpicture}
\end{center}
"""

    latex_code += r"""
\end{document}
"""
    return latex_code
