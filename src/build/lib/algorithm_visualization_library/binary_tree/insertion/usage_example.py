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
    root = BinaryTreeNode("A")
    root.left = BinaryTreeNode("B")
    root.right = BinaryTreeNode("C")
    root.left.left = BinaryTreeNode("D")
    root.left.right = BinaryTreeNode("E")
    root.right.right = BinaryTreeNode("F")

    steps = [generate_latex_binary_tree(root, is_root=True)]
    print("Initial tree created.")

    while True:
        action = input("Do you want to add a node? (yes/no): ").strip().lower()
        if action == 'no':
            break

        if action == 'yes':
            new_value = input("Enter the value for the new node: ").strip()
            root = insert_level_order(root, new_value, steps)
            print(f"Node {new_value} added in level order.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    latex_document = generate_latex_document_steps(steps)
    filename = "binary_tree_insertion_steps.tex"

    with open(filename, "w") as file:
        file.write(latex_document)

    print(f"LaTeX code for binary tree insertion steps has been generated and saved to {filename}")

if __name__ == "__main__":
    main()
"""