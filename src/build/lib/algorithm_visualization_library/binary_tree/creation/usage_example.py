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
    root = None
    steps = []

    method = input("Do you want the final tree or step-by-step representation? (final/steps): ").strip().lower()

    while True:
        action = input("Do you want to add a node? (yes/no): ").strip().lower()
        if action == 'no':
            break

        if action == 'yes':
            new_value = input("Enter the value for the new node: ").strip()
            if root is None:
                root = BinaryTreeNode(new_value)
                print(f"Root node {new_value} created.")
            else:
                parent_value = input("Enter the value of the parent node: ").strip()
                position = input("Enter the position (left/right): ").strip().lower()
                root = add_node(root, parent_value, new_value, position)
                print(f"Node {new_value} added as {position} child of {parent_value}.")

            latex_code = generate_latex_binary_tree(root, is_root=True)
            steps.append(latex_code)
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if method == 'final':
        latex_document = generate_latex_document(root)
        filename = "binary_tree_final.tex"
    elif method == 'steps':
        latex_document = generate_latex_document_steps(steps)
        filename = "binary_tree_creation_steps.tex"
    else:
        print("Invalid method selected.")
        return

    with open(filename, "w") as file:
        file.write(latex_document)

    print(f"LaTeX code for binary tree has been generated and saved to {filename}")

if __name__ == "__main__":
    main()
"""