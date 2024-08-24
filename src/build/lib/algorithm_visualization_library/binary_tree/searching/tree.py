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
def search_binary_tree(node, target, steps):
    if not node:
        return False
    steps.append(generate_latex_binary_tree(node, target=target, is_root=True))

    if node.value == target:
        return True
    if search_binary_tree(node.left, target, steps):
        return True
    if search_binary_tree(node.right, target, steps):
        return True

    return False


def generate_latex_binary_tree(node, target=None, is_root=False):
    if not node:
        return ""

    node_prefix = "\\" if is_root else ""

    if node.value == target:
        latex_code = f"{node_prefix}node[fill=purple!60] {{{node.value}}}"
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

% Explanation about the algorithm
\section*{Binary Tree Search Algorithm}
In this document, we illustrate the process of searching for a value in a binary tree. The search algorithm is a depth-first search (DFS) using recursion, and it operates as follows:

\begin{enumerate}
    \item \textbf{Start at the Root:}
    Begin the search at the root of the binary tree.

    \item \textbf{Check Current Node:}
    Compare the value of the current node with the target value. If they match, the search is successful.

    \item \textbf{Recursive Search:}
    If the current node's value does not match the target, recursively search the left and right subtrees. This is done by calling the search function on the left child and then on the right child.

    \item \textbf{Highlighting Nodes:}
    During the search process, nodes being visited are highlighted to show their role in the search. If the target node is found, it is highlighted in purple.

    \item \textbf{End of Search:}
    The search concludes when the target value is found or all nodes have been visited. If the target is not found after traversing the entire tree, the search concludes with a failure.
\end{enumerate}

% Detailed Steps
\section*{Detailed Steps}
The following figures illustrate the binary tree at various stages of the search process. Each figure shows the state of the tree at different points during the search operation.

"""

    for i in range(0, len(steps), 6):
        latex_code += r"""
\begin{figure}[h!]
\centering
"""
        for j in range(i, min(i + 6, len(steps))):
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
