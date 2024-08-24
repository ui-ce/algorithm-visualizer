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
def pre_order_traversal(node, steps):
    if not node:
        return

    steps.append(generate_latex_binary_tree(node, target=node.value, is_root=True))

    pre_order_traversal(node.left, steps)
    pre_order_traversal(node.right, steps)


def in_order_traversal(node, steps):
    if not node:
        return

    in_order_traversal(node.left, steps)

    steps.append(generate_latex_binary_tree(node, target=node.value, is_root=True))

    in_order_traversal(node.right, steps)


def post_order_traversal(node, steps):
    if not node:
        return

    post_order_traversal(node.left, steps)
    post_order_traversal(node.right, steps)

    steps.append(generate_latex_binary_tree(node, target=node.value, is_root=True))


def generate_latex_binary_tree(node, target=None, is_root=False):
    if not node:
        return ""

    node_prefix = "\\" if is_root else ""

    if node.value == target:
        latex_code = f"{node_prefix}node[fill=blue!30] {{{node.value}}}"
    else:
        latex_code = f"{node_prefix}node {{{node.value}}}"

    children = []
    if node.left or node.right:
        if node.left:
            children.append(f"child {{{generate_latex_binary_tree(node.left, target=target)}}}")
        else:
            children.append(f"child[fill=none] {{edge from parent[draw=none]}}")
        if node.right:
            children.append(f"child {{{generate_latex_binary_tree(node.right, target=target)}}}")
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

\title{Binary Tree Traversal Algorithms}
\author{}
\date{}
\maketitle

\section*{Introduction}
This document provides a visual representation of binary tree traversal algorithms. We will explore three different traversal methods: pre-order, in-order, and post-order. Each method is demonstrated through a series of figures that show the binary tree at various stages of traversal.

\section*{Traversal Algorithms}
\begin{itemize}
    \item \textbf{Pre-order Traversal:}
    In pre-order traversal, the nodes are recursively visited in the following order: root, left subtree, right subtree. This traversal method is useful for creating a prefix expression of the tree.

    \item \textbf{In-order Traversal:}
    In in-order traversal, the nodes are recursively visited in this order: left subtree, root, right subtree. This method is particularly useful for binary search trees (BSTs) as it retrieves the nodes in ascending order.

    \item \textbf{Post-order Traversal:}
    In post-order traversal, the nodes are recursively visited in the order: left subtree, right subtree, root. This traversal method is useful for deleting nodes or evaluating postfix expressions.
\end{itemize}

\section*{Initial Tree State}
The following figure shows the initial state of the binary tree before any traversal has occurred. This provides a baseline for understanding how the tree changes during traversal.

\begin{figure}[h!]
\centering
\begin{minipage}{0.8\textwidth}
    \centering
    \begin{tikzpicture}[level distance=10mm]
        \tikzstyle{every node}=[fill=green!75,circle,inner sep=1pt, minimum size=8mm]
        \tikzstyle{level 1}=[sibling distance=25mm, set style={{every node}+=[fill=green!60]}]
        \tikzstyle{level 2}=[sibling distance=20mm, set style={{every node}+=[fill=green!45]}]
        \tikzstyle{level 3}=[sibling distance=15mm, set style={{every node}+=[fill=green!30]}]
        \tikzstyle{level 4}=[sibling distance=10mm, set style={{every node}+=[fill=green!15]}]
        """ + steps[0] + ";" + r"""
    \end{tikzpicture}
    \caption{Initial Tree State}
\end{minipage}
\vspace{1cm}
\end{figure}

% Traversal Steps
\section*{Traversal Steps}
The following figures illustrate the binary tree at different stages of traversal, depending on the chosen traversal method. Each step shows the tree with the current node being processed highlighted.

"""

    for i in range(1, len(steps), 4):
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
        \tikzstyle{level 1}=[sibling distance=25mm, set style={{every node}+=[fill=green!60]}]
        \tikzstyle{level 2}=[sibling distance=20mm, set style={{every node}+=[fill=green!45]}]
        \tikzstyle{level 3}=[sibling distance=15mm, set style={{every node}+=[fill=green!30]}]
        \tikzstyle{level 4}=[sibling distance=10mm, set style={{every node}+=[fill=green!15]}]
        """ + steps[j] + ";" + r"""
    \end{tikzpicture}
    \caption{Traversal Step """ + str(j + 1) + r"""}
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


