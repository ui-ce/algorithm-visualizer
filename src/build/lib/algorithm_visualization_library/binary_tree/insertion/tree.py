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


def insert_level_order(root, key, steps):
    """Inserts an element into the binary tree in level order."""
    if not root:
        return BinaryTreeNode(key)

    queue = [root]

    while queue:
        temp = queue.pop(0)

        if not temp.left:
            temp.left = BinaryTreeNode(key)
            steps.append(generate_latex_binary_tree(root, is_root=True))
            return root
        else:
            queue.append(temp.left)

        if not temp.right:
            temp.right = BinaryTreeNode(key)
            steps.append(generate_latex_binary_tree(root, is_root=True))
            return root
        else:
            queue.append(temp.right)

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


def generate_latex_document_steps(steps):
    latex_code = r"""
\documentclass[10pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage{tikz}
\usepackage[margin=1cm]{geometry}
\begin{document}
\section*{Binary Tree Construction Steps}
This document illustrates the step-by-step construction of a binary tree. Each step shows the tree after the insertion of a new node, demonstrating how the tree evolves over time.

\subsection*{Algorithm Description}
The binary tree is constructed using a level-order insertion method. This means that new nodes are added starting from the top level, filling in from left to right. If a node has a left and right child, the insertion continues to the next level. The process repeats until all nodes are inserted into the tree.

\subsection*{Step-by-Step Visualization}
The following figures represent the state of the binary tree after each insertion step. The captions describe the order of the steps. Nodes are represented by circles, and the connections between them indicate the parent-child relationships.
"""

    for i in range(0, len(steps), 4):
        latex_code += r"""
\begin{figure}[h!]
\centering
"""
        for j in range(i, min(i + 4, len(steps))):
            if j == 0:
                caption_text = "Initial Tree"
            else:
                caption_text = f"Step {j + 1}"

            latex_code += r"""
\begin{minipage}{0.8\textwidth}
    \centering
    \begin{tikzpicture}[level distance=10mm]
        \tikzstyle{every node}=[fill=green!75,circle,inner sep=1pt, minimum size=8mm]
        \tikzstyle{level 1}=[sibling distance=40mm, set style={{every node}+=[fill=green!60]}]
        \tikzstyle{level 2}=[sibling distance=20mm, set style={{every node}+=[fill=green!45]}]
        \tikzstyle{level 3}=[sibling distance=15mm, set style={{every node}+=[fill=green!30]}]
        \tikzstyle{level 4}=[sibling distance=10mm, set style={{every node}+=[fill=green!15]}]
        """ + steps[j] + ";" + r"""
    \end{tikzpicture}
    \caption{""" + caption_text + r"""}
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
