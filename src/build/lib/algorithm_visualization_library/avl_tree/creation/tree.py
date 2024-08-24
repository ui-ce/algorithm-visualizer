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


def get_height(node):
    if not node:
        return 0
    return node.height


def update_height(node):
    if node:
        node.height = 1 + max(get_height(node.left), get_height(node.right))


def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    update_height(y)
    update_height(x)

    return x


def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    update_height(x)
    update_height(y)

    return y


def insert_into_avl(root, value):
    if not root:
        return BinaryTreeNode(value), None, None

    if value < root.name:
        root.left, highlight_red, pre_rotation = insert_into_avl(root.left, value)
    else:
        root.right, highlight_red, pre_rotation = insert_into_avl(root.right, value)

    update_height(root)

    balance = get_balance(root)

    if balance > 1 or balance < -1:
        highlight_red = root.name

    pre_rotation = ""
    if balance > 1 and value < root.left.name:
        pre_rotation = generate_latex_binary_tree(root, highlight_red, is_root=True)
        root = rotate_right(root)
    elif balance < -1 and value > root.right.name:
        pre_rotation = generate_latex_binary_tree(root, highlight_red, is_root=True)
        root = rotate_left(root)
    elif balance > 1 and value > root.left.name:
        pre_rotation = generate_latex_binary_tree(root, highlight_red, is_root=True)
        root.left = rotate_left(root.left)
        root = rotate_right(root)
    elif balance < -1 and value < root.right.name:
        pre_rotation = generate_latex_binary_tree(root, highlight_red, is_root=True)
        root.right = rotate_right(root.right)
        root = rotate_left(root)

    return root, highlight_red, pre_rotation


def generate_latex_binary_tree(node, highlight_red=None, is_root=False):
    if not node:
        return ""

    balance = get_balance(node)
    color = "green!80"
    node_prefix = "\\" if is_root else ""
    latex_code = f"{node_prefix}node [fill={color}] {{{node.name}}} node [below=3pt] {{\\tiny {balance}}}"

    children = []
    if node.left or node.right:
        if node.left:
            children.append(f"child {{{generate_latex_binary_tree(node.left, highlight_red)}}}")
        else:
            children.append(f"child[fill=none] {{edge from parent[draw=none]}}")
        if node.right:
            children.append(f"child {{{generate_latex_binary_tree(node.right, highlight_red)}}}")
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
\section*{AVL Tree Algorithm Overview}

An AVL tree is a self-balancing binary search tree where the height difference between the left and right subtrees of any node is at most one. This balance ensures that the tree remains approximately balanced, leading to $O(\log n)$ time complexity for search, insertion, and deletion operations.

\subsection*{Key Concepts}
\begin{itemize}
    \item \textbf{Height}: The height of a node in an AVL tree is the length of the longest path from the node to a leaf. This height is used to determine the balance of the node.
    \item \textbf{Balance Factor}: For any node in the AVL tree, the balance factor is calculated as the height of the left subtree minus the height of the right subtree. It helps in determining if the node is balanced, left-heavy, or right-heavy.
    \item \textbf{Rotations}: To maintain balance in the AVL tree after insertions and deletions, rotations are performed. There are four types of rotations:
    \begin{itemize}
        \item \textbf{Right Rotation (Single Rotation)}: Applied when a left-heavy subtree needs balancing.
        \item \textbf{Left Rotation (Single Rotation)}: Applied when a right-heavy subtree needs balancing.
        \item \textbf{Left-Right Rotation (Double Rotation)}: Applied when a left subtree has a right-heavy child.
        \item \textbf{Right-Left Rotation (Double Rotation)}: Applied when a right subtree has a left-heavy child.
    \end{itemize}
\end{itemize}

\subsection*{Operations}
\begin{itemize}
    \item \textbf{Insertion}:
    \begin{itemize}
        \item Insert the new node following the standard binary search tree (BST) insertion rules.
        \item Update the height of each ancestor node.
        \item Calculate the balance factor of each node.
        \item Perform rotations if any node becomes unbalanced (balance factor is greater than 1 or less than -1).
    \end{itemize}
    \item \textbf{Rotations}:
    \begin{itemize}
        \item \textbf{Right Rotation}: Used when a left-heavy subtree (balance factor > 1) is unbalanced.
        \item \textbf{Left Rotation}: Used when a right-heavy subtree (balance factor < -1) is unbalanced.
        \item \textbf{Left-Right Rotation}: First perform a left rotation on the left child, then a right rotation on the current node.
        \item \textbf{Right-Left Rotation}: First perform a right rotation on the right child, then a left rotation on the current node.
    \end{itemize}
\end{itemize}
\begin{center}
\begin{tikzpicture}[level distance=15mm, sibling distance=20mm]
    \tikzstyle{every node}=[circle,inner sep=1pt, minimum size=8mm]
    \tikzstyle{level 1}=[sibling distance=60mm]
    \tikzstyle{level 2}=[sibling distance=30mm]
    \tikzstyle{level 3}=[sibling distance=15mm]
    \tikzstyle{level 4}=[sibling distance=10mm]

"""
    latex_code += "    " + generate_latex_binary_tree(root, is_root=True) + ";\n"
    latex_code += r"""
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
\subsection*{Introduction}
The AVL tree is a self-balancing binary search tree where the difference in heights between the left and right subtrees of any node (known as the balance factor) is at most 1. When an imbalance occurs due to insertion or deletion, rotations are performed to restore balance.

\subsection*{Step-by-Step Process}
\begin{itemize}
    \item \textbf{Insertion}: Nodes are inserted following the binary search tree rules. After insertion, the height of each node is updated, and the balance factor is checked. If the balance factor of any node becomes greater than 1 or less than -1, rotations are performed to restore balance.
    \item \textbf{Rotations}: Depending on the type of imbalance (left-heavy or right-heavy), one or more rotations are performed. The types of rotations include:
    \begin{itemize}
        \item \textbf{Right Rotation}: Applied when a left-heavy subtree needs balancing.
        \item \textbf{Left Rotation}: Applied when a right-heavy subtree needs balancing.
        \item \textbf{Left-Right Rotation}: Applied when a left subtree has a right-heavy child.
        \item \textbf{Right-Left Rotation}: Applied when a right subtree has a left-heavy child.
    \end{itemize}
\end{itemize}

\subsection*{Steps Visualization}
The following figures illustrate the AVL tree at various stages of the insertion and balancing process:

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
