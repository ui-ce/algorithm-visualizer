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
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    steps = [generate_latex_binary_tree(root, is_root=True)]
    print("Initial tree created.")

    while True:
        user_input = input("Enter the value of the node to delete (or 'stop' to end): ").strip()
        if user_input.lower() == 'stop':
            break

        try:
            value_to_delete = int(user_input)
            root = deletion(root, value_to_delete, steps)
            print(f"Node {value_to_delete} deleted.")
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'stop'.")

    latex_document = generate_latex_document_steps(steps)
    filename = "binary_tree_deletion_steps.tex"

    with open(filename, "w") as file:
        file.write(latex_document)

    print(f"LaTeX code for binary tree operations steps has been generated and saved to {filename}")

if __name__ == "__main__":
    main()
"""