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


def add_node(root, parent_value, new_value, position):
    if root is None:
        return None

    if root.name == parent_value:
        if position == 'left':
            root.left = BinaryTreeNode(new_value)
        elif position == 'right':
            root.right = BinaryTreeNode(new_value)
        return root

    if root.left:
        add_node(root.left, parent_value, new_value, position)
    if root.right:
        add_node(root.right, parent_value, new_value, position)

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

\section*{Final Binary Tree:}
This document presents the final binary tree generated through the user-driven node insertion process. The binary tree structure is designed to start from a root node and grows as new nodes are inserted based on user input. The following sections detail the algorithm and the visualization of the tree.

\subsection*{Tree Construction Process:}
The binary tree was constructed using the following steps:
\begin{enumerate}
    \item \textbf{Insertion of Root Node:} The process began by inserting the root node, which is the starting point of the tree.
    \item \textbf{Adding Child Nodes:} For each subsequent node, the user was prompted to specify the parent node and whether the new node should be placed on the left or right.
    \item \textbf{Recursive Structure:} The tree maintains a recursive structure, where each node can have up to two children (left and right). The final tree reflects all user inputs.
\end{enumerate}

\vspace{1cm}

\begin{center}
\begin{tikzpicture}[level distance=20mm]
    \tikzstyle{every node}=[fill=green!75,circle,inner sep=10pt, minimum size=8mm]
    \tikzstyle{level 1}=[sibling distance=40mm, set style={{every node}+=[fill=green!75]}]
    \tikzstyle{level 2}=[sibling distance=20mm, set style={{every node}+=[fill=green!75]}]
    \tikzstyle{level 3}=[sibling distance=10mm, set style={{every node}+=[fill=green!75]}]
    \tikzstyle{level 4}=[sibling distance=5mm, set style={{every node}+=[fill=green!75]}]
"""
    latex_code += "    " + generate_latex_binary_tree(root, is_root=True) + ";\n"
    latex_code += r"""
\end{tikzpicture}
\end{center}

\subsection*{Understanding the Visualization:}
The tree diagram above visually represents the binary tree. Each circle represents a node, and the connections between them represent the parent-child relationships. The root node is the topmost circle, and all other nodes are connected below it. The position of each node (left or right) corresponds to its relation to the parent node, as determined by the user's input during the tree construction process.

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

\section*{Step-by-Step Binary Tree Construction:}
This document illustrates the step-by-step construction of a binary tree. Each step corresponds to the insertion of a new node, which modifies the tree structure as shown in the corresponding diagrams.

\subsection*{Explanation of Steps:}
The binary tree evolves with each insertion based on the user's input. Below, each step shows the state of the tree after a new node has been added. The nodes are placed according to the specified parent node and whether the new node is a left or right child.
"""

    for i in range(0, len(steps), 4):
        latex_code += r"""
\begin{figure}[h!]
\centering
"""
        for j in range(i, min(i + 4, len(steps))):
            latex_code += r"""
\begin{minipage}{0.8\textwidth}
    \centering
    \begin{tikzpicture}[level distance=10mm]
        \tikzstyle{every node}=[fill=green!75,circle,inner sep=1pt, minimum size=8mm]
        \tikzstyle{level 1}=[sibling distance=30mm, set style={{every node}+=[fill=green!60]}]
        \tikzstyle{level 2}=[sibling distance=15mm, set style={{every node}+=[fill=green!45]}]
        \tikzstyle{level 3}=[sibling distance=10mm, set style={{every node}+=[fill=green!30]}]
        \tikzstyle{level 4}=[sibling distance=5mm, set style={{every node}+=[fill=green!15]}]
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