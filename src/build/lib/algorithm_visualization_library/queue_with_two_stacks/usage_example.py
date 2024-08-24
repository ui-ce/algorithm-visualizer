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
custom_color = input("Please enter the color code for the filled stack cells ( #a9fc8d ): ")

queue = QueueWithStacks(custom_color)

cell_width = float(input("Please enter the width of each stack cell (in cm): "))
cell_height = float(input("Please enter the height of each stack cell (in cm): "))
queue.set_cell_dimensions(cell_width, cell_height)

enqueue_values = input("Please enter the values to enqueue (separated by spaces): ")
values = list(map(int, enqueue_values.split()))
for value in values:
    queue.enqueue(value)

num_dequeue = int(input("Please enter the number of items to dequeue: "))
for _ in range(num_dequeue):
    queue.dequeue()

queue.generate_latex("queue_with_stacks")
"""