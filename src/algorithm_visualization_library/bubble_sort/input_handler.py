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
# BubbleSort/input_handler.py
def get_user_input():
    array = list(map(int, input("Enter the array elements separated by space: ").split()))
    primary_color = input("Enter the primary color for the first element being compared (e.g., blue!30): ")
    secondary_color = input("Enter the secondary color for the second element being compared (e.g., red!30): ")
    steps_per_page = int(input("Enter how many arrays should be shown on one page:"))
    return array, primary_color, secondary_color, steps_per_page
