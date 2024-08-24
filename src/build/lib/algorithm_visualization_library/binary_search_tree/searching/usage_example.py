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
"""
def main():
    root = BinarySearchTreeNode(10)
    root.left = BinarySearchTreeNode(5)
    root.right = BinarySearchTreeNode(20)
    root.left.left = BinarySearchTreeNode(3)
    root.left.right = BinarySearchTreeNode(7)
    root.right.left = BinarySearchTreeNode(15)
    root.right.right = BinarySearchTreeNode(25)

    target = int(input("Enter the value to search for: ").strip())
    steps = []
    found = search_bst(root, target, steps)

    if found:
        print(f"Node {target} found in the tree.")
    else:
        print(f"Node {target} not found in the tree.")

    latex_document = generate_latex_document_steps(steps)
    filename = "bst_search_steps.tex"

    with open(filename, "w") as file:
        file.write(latex_document)

    print(f"LaTeX code for binary search tree steps has been generated and saved to {filename}")

if __name__ == "__main__":
    main()
"""