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

    def insert_at_index(self, index, value):
        if index < 0:
            raise IndexError("Index must be a non-negative integer.")

        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next

        if index > length:
            raise IndexError(f"Index out of range. Maximum allowable index is {length}")

        new_node = Node(value)

        if index == 0:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        current_index = 0

        while current is not None and current_index < index - 1:
            current = current.next
            current_index += 1

        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node
        current.next = new_node

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

        # No need to add Null nodes here

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
        latex_code += r"\section*{Doubly Linked List Before Insertion}" + "\n"
        latex_code += r"\begin{tikzpicture}" + "\n"
        latex_code += before_code
        latex_code += r"\end{tikzpicture}" + "\n"
        latex_code += r"\section*{Doubly Linked List After Insertion}" + "\n"
        latex_code += r"\begin{tikzpicture}" + "\n"
        latex_code += after_code
        latex_code += r"\end{tikzpicture}" + "\n"
        latex_code += r"\end{document}"

        return latex_code