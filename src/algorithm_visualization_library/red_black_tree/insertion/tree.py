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
from .node import RedBlackNode


class RedBlackTree:
    def __init__(self):
        self.NIL = RedBlackNode(value=None, color='black')
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.NIL:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, value):
        new_node = RedBlackNode(value, color='red', left=self.NIL, right=self.NIL)
        y = self.NIL
        x = self.root

        while x != self.NIL:
            y = x
            if new_node.value < x.value:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y == self.NIL:
            self.root = new_node
        elif new_node.value < y.value:
            y.left = new_node
        else:
            y.right = new_node

        steps = self.fix_insert(new_node)
        return steps

    def fix_insert(self, z):
        steps = []
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.left_rotate(z.parent.parent)
            steps.append(generate_latex_red_black_tree(self.root, self, is_root=True))
        self.root.color = 'black'
        steps.append(generate_latex_red_black_tree(self.root, self, is_root=True))
        return steps


def generate_latex_red_black_tree(node, rb_tree, is_root=False):
    if node == rb_tree.NIL:
        return ""

    color = node.color.lower()
    text_color = 'white'  # Color of the text
    node_prefix = "\\" if is_root else ""
    latex_code = f"{node_prefix}node [fill={color}, text={text_color}] {{{node.value}}}"

    children = []
    if node.left != rb_tree.NIL or node.right != rb_tree.NIL:
        if node.left != rb_tree.NIL:
            children.append(f"child {{{generate_latex_red_black_tree(node.left, rb_tree)}}}")
        else:
            children.append(f"child[fill=none] {{edge from parent[draw=none]}}")
        if node.right != rb_tree.NIL:
            children.append(f"child {{{generate_latex_red_black_tree(node.right, rb_tree)}}}")
        else:
            children.append(f"child[fill=none] {{edge from parent[draw=none]}}")

    return f"{latex_code} {' '.join(children)}"



def generate_latex_document_steps_red_black(steps):
    latex_code = r"""
\documentclass[10pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage{tikz}
\usepackage[margin=1cm]{geometry}
\begin{document}
\section*{Introduction}
The Red-Black tree is a self-balancing binary search tree where each node is either red or black. The tree maintains balance through several properties that ensure it remains approximately balanced.

\subsection*{Step-by-Step Process}
The following figures illustrate the Red-Black tree at various stages of the insertion and balancing process:

"""
    num_steps = len(steps)
    for i in range(0, num_steps, 4):
        latex_code += r"""
\begin{figure}[h!]
\centering
"""
        for j in range(i, min(i + 4, num_steps)):
            latex_code += r"""
\begin{minipage}{0.8\textwidth}
    \centering
    \begin{tikzpicture}[level distance=15mm, sibling distance=20mm]
        \tikzstyle{every node}=[circle,inner sep=1pt, minimum size=8mm]
        \tikzstyle{level 1}=[sibling distance=60mm]
        \tikzstyle{level 2}=[sibling distance=30mm]
        \tikzstyle{level 3}=[sibling distance=15mm]
        \tikzstyle{level 4}=[sibling distance=10mm]
        """ + steps[j] + ";" + r"""
    \end{tikzpicture}
    \caption{Step """ + str(j + 1) + r"""}
\end{minipage}
\vspace{1cm}
"""

        latex_code += r"""
\end{figure}
\newpage
"""

    latex_code += r"""
\end{document}
"""
    return latex_code
