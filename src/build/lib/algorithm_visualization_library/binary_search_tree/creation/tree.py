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

from .node import BinaryTreeNode

def insert_into_bst(root, value):
    if root is None:
        return BinaryTreeNode(value)
    if value < root.name:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root


def add_node(root, value):
    if root is None:
        return BinaryTreeNode(value)

    if value < root.name:
        root.left = add_node(root.left, value)
    else:
        root.right = add_node(root.right, value)

    return root


def generate_latex_binary_tree(node, is_root=False):
    if not node:
        return ""

    node_prefix = "\\" if is_root else ""
    latex_code = f"{node_prefix}node {{{node.name}}}"

    children = []
    if node.left or node.right:
        if node.left:
            children.append(f"child {{{generate_latex_binary_tree(node.left)}}}")
        else:
            children.append(f"child[fill=none] {{edge from parent[draw=none]}}")
        if node.right:
            children.append(f"child {{{generate_latex_binary_tree(node.right)}}}")
        else:
            children.append(f"child[fill=none] {{edge from parent[draw=none]}}")

    return f"{latex_code} {' '.join(children)}"


def generate_latex_document(root):
    latex_code = r"""
\documentclass[10pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage{tikz}
\usepackage[margin=1cm]{geometry}
\begin{document}

\section*{Final Binary Search Tree}
This document presents the final binary search tree generated through the user-driven node insertion process. The binary tree structure is designed to start from a root node and grows as new nodes are inserted based on user input. The following sections detail the algorithm and the visualization of the tree.

\subsection*{Tree Construction Process}
The binary tree was constructed using the following steps:
\begin{enumerate}
    \item \textbf{Insertion of Root Node:} The process begins by inserting the root node, which serves as the starting point of the tree.
    \item \textbf{Adding Child Nodes:} Subsequent nodes are added by comparing them with existing nodes. If the new node’s value is less than the current node's value, it is placed in the left subtree; otherwise, it goes to the right subtree.
    \item \textbf{Recursive Structure:} The tree maintains a recursive structure, where each node can have up to two children (left and right). Each insertion involves traversing the tree recursively until the appropriate position for the new node is found.
\end{enumerate}

\subsection*{Final Tree Visualization}
The final binary tree is visualized below:

\begin{center}
\begin{tikzpicture}[level distance=15mm, sibling distance=20mm]
    \tikzstyle{every node}=[fill=green!30,circle,inner sep=1pt, minimum size=8mm]
    \tikzstyle{level 1}=[sibling distance=40mm, set style={{every node}+=[fill=green!30]}]
    \tikzstyle{level 2}=[sibling distance=20mm, set style={{every node}+=[fill=green!30]}]
    \tikzstyle{level 3}=[sibling distance=15mm, set style={{every node}+=[fill=green!30]}]
    \tikzstyle{level 4}=[sibling distance=10mm, set style={{every node}+=[fill=green!30]}]

% The following code generates the final binary search tree (BST) after all insertions.

""" + "    " + generate_latex_binary_tree(root, is_root=True) + ";\n" + r"""
\end{tikzpicture}
\end{center}

\end{document}
"""
    return latex_code


def generate_latex_document_steps(steps):
    latex_code = r"""
\documentclass[10pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage{tikz}
\usepackage[margin=1cm]{geometry}
\begin{document}

% This document presents the step-by-step process of constructing the binary search tree (BST) through user-driven node insertions.

\section*{Step-by-Step Tree Construction}
The following figures illustrate the construction of the binary search tree (BST) at each step of node insertion. 

\subsection*{Algorithm for Tree Construction}
The binary tree was built according to these steps:
\begin{enumerate}
    \item \textbf{Starting with an Empty Tree:} The tree starts empty. Nodes are inserted based on user input, and each insertion follows the BST properties.
    \item \textbf{Inserting Nodes:} Each new node is inserted by comparing its value with the current nodes. If it is smaller, it goes to the left child; if larger, it goes to the right child. This process is repeated recursively until the correct position is found.
    \item \textbf{Recursive Insertion:} The insertion process is recursive. The tree is traversed starting from the root, and the node is inserted in the correct position by comparing it with existing nodes.
\end{enumerate}

% The following figures show the BST after each insertion step.

"""

    for i in range(0, len(steps), 3):
        latex_code += r"""
\begin{figure}[h!]
\centering
"""
        for j in range(i, min(i + 3, len(steps))):
            latex_code += r"""
\begin{minipage}{0.8\textwidth}
    \centering
    \begin{tikzpicture}[level distance=15mm, sibling distance=20mm]
        \tikzstyle{every node}=[fill=green!30,circle,inner sep=1pt, minimum size=8mm]
        \tikzstyle{level 1}=[sibling distance=20mm, set style={{every node}+=[fill=green!30]}]
        \tikzstyle{level 2}=[sibling distance=15mm, set style={{every node}+=[fill=green!30]}]
        \tikzstyle{level 3}=[sibling distance=10mm, set style={{every node}+=[fill=green!30]}]
        \tikzstyle{level 4}=[sibling distance=10mm, set style={{every node}+=[fill=green!30]}]

% This figure represents the BST after step """ + str(j + 1) + r""". 

""" + "        " + steps[j] + ";\n" + r"""
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
