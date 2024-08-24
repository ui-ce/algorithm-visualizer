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

target = int(input("Enter the target number to search for: "))
color_found = input("Enter the color code for found element (e.g., green or #2a9d8f): ")
color_not_found = input("Enter the color code for not found element (e.g., red or #e63946): ")

index, steps = linear_search(arr, target)

latex_output = generate_latex(arr, steps, target, color_found, color_not_found)

file_name = "linear_search_step_by_step.tex"
with open(file_name, "w") as f:
    f.write(latex_output)

print(f"Linear search step-by-step LaTeX code written to {file_name}")
"""