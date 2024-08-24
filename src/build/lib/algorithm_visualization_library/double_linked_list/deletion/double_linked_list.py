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

from .node import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def delete_at_index(self, index):
        if index < 0:
            raise IndexError("Index must be a non-negative integer.")

        if self.head is None:
            raise IndexError("Deletion from an empty list is not allowed.")

        current = self.head

        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        current_index = 0

        while current is not None and current_index < index:
            current = current.next
            current_index += 1

        if current is None:
            raise IndexError(f"Index out of range. Maximum allowable index is {current_index - 1}")

        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

    def delete_by_value(self, value):
        if self.head is None:
            raise ValueError("Deletion from an empty list is not allowed.")

        current = self.head

        # Handle deletion if the value is in the head node
        if current.value == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        # Traverse the list to find the node with the given value
        while current is not None and current.value != value:
            current = current.next

        if current is None:
            raise ValueError(f"Value {value} not found in the list.")

        # Update the links to remove the node
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

    def generate_latex_for_state(self):
        if not self.head:
            return ""

        latex_code = ""
        current = self.head
        node_counter = 1

        # Generate nodes
        while current:
            latex_code += f"    \\node[list,on chain] (N{node_counter}) {{\\nodepart{{second}} {current.value}}};\n"
            current = current.next
            node_counter += 1

        # Generate edges
        for i in range(node_counter - 2):
            latex_code += f"    \\path[*->] let \\p1 = (N{i + 1}.three), \\p2 = (N{i + 1}.center) in (\\x1,\\y2) edge [bend left] ($(N{i + 2}.one)+(0,0.2)$);\n"
            latex_code += f"    \\path[*->] ($(N{i + 2}.one)+(0.1,0.1)$) edge [bend left] ($(N{i + 1}.three)+(0,-0.05)$);\n"

        return latex_code

    def generate_combined_latex(self, before_code, after_code):
        latex_code = r"\documentclass[10pt,a4paper]{article}" + "\n"
        latex_code += r"\usepackage[T1]{fontenc}" + "\n"
        latex_code += r"\usepackage{tikz}" + "\n"
        latex_code += r"\usepackage[margin=1cm]{geometry}" + "\n"
        latex_code += r"\usetikzlibrary{calc,shapes.multipart,chains,arrows,positioning}" + "\n"
        latex_code += r"\tikzset{list/.style={very thick, rectangle split, rectangle split parts=3, draw, rectangle split horizontal, minimum size=18pt, inner sep=5pt, text=black, rectangle split part fill={blue!20, red!20, blue!20}}, ->, start chain=going right, very thick}" + "\n"
        latex_code += r"\begin{document}" + "\n"
        latex_code += r"\section*{Doubly Linked List Before Operation}" + "\n"
        latex_code += r"\begin{tikzpicture}" + "\n"
        latex_code += before_code
        latex_code += r"\end{tikzpicture}" + "\n"
        latex_code += r"\section*{Doubly Linked List After Operation}" + "\n"
        latex_code += r"\begin{tikzpicture}" + "\n"
        latex_code += after_code
        latex_code += r"\end{tikzpicture}" + "\n"
        latex_code += r"\end{document}"

        return latex_code