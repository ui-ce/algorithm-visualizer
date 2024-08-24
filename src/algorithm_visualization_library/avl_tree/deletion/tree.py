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


def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete_from_avl(root, value):
    if not root:
        return root, None, None

    if value < root.name:
        root.left, highlight_red, pre_rotation = delete_from_avl(root.left, value)
    elif value > root.name:
        root.right, highlight_red, pre_rotation = delete_from_avl(root.right, value)
    else:
        if not root.left:
            return root.right, None, None
        elif not root.right:
            return root.left, None, None

        temp = min_value_node(root.right)
        root.name = temp.name
        root.right, highlight_red, pre_rotation = delete_from_avl(root.right, temp.name)

    update_height(root)

    balance = get_balance(root)

    pre_rotation = ""
    if balance > 1 and get_balance(root.left) >= 0:
        pre_rotation = generate_latex_binary_tree(root, is_root=True)
        root = rotate_right(root)
    elif balance < -1 and get_balance(root.right) <= 0:
        pre_rotation = generate_latex_binary_tree(root, is_root=True)
        root = rotate_left(root)
    elif balance > 1 and get_balance(root.left) < 0:
        pre_rotation = generate_latex_binary_tree(root, is_root=True)
        root.left = rotate_left(root.left)
        root = rotate_right(root)
    elif balance < -1 and get_balance(root.right) > 0:
        pre_rotation = generate_latex_binary_tree(root, is_root=True)
        root.right = rotate_right(root.right)
        root = rotate_left(root)

    return root, highlight_red, pre_rotation


def update_heights_from_node(root):
    if not root:
        return
    update_heights_from_node(root.left)
    update_heights_from_node(root.right)
    update_height(root)


def generate_latex_binary_tree(node, is_root=False):
    if not node:
        return ""

    balance = get_balance(node)
    color = "green!80"
    node_prefix = "\\" if is_root else ""
    latex_code = f"{node_prefix}node [fill={color}] {{{node.name}}} node [below=3pt] {{\\tiny {balance}}}"

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


def generate_latex_document_steps(steps, initial_tree=None):
    latex_code = r"""
\documentclass[10pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage{tikz}
\usepackage[margin=1cm]{geometry}
\begin{document}
\subsection*{Introduction}
The AVL tree is a self-balancing binary search tree where the difference in heights between the left and right subtrees of any node (known as the balance factor) is at most 1. When an imbalance occurs due to insertion or deletion, rotations are performed to restore balance.

\subsection*{Initial AVL Tree}
\begin{center}
\begin{tikzpicture}[level distance=15mm, sibling distance=20mm]
    \tikzstyle{every node}=[circle,inner sep=1pt, minimum size=8mm]
    \tikzstyle{level 1}=[sibling distance=60mm]
    \tikzstyle{level 2}=[sibling distance=30mm]
    \tikzstyle{level 3}=[sibling distance=15mm]
    \tikzstyle{level 4}=[sibling distance=10mm]
    """ + (generate_latex_binary_tree(initial_tree, is_root=True) if initial_tree else '') + ";" + r"""
\end{tikzpicture}
\end{center}

\subsection*{Step-by-Step Process}
The following figures illustrate the AVL tree at various stages of the deletion and balancing process:

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