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
"""
n = int(input("Enter the size of the array: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

color_key = input("Enter the color code for key element (e.g., #2a9d8f): ")
color_compared = input("Enter the color code for compared element (e.g., #e63946): ")

steps = insertion_sort(arr)

latex_output = generate_latex(arr, steps, color_key, color_compared)

file_name = "insertion_sort_step_by_step.tex"
with open(file_name, "w") as f:
    f.write(latex_output)

print(f"Insertion sort step-by-step LaTeX code written to {file_name}")
"""