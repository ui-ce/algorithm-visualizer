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
    root = BinaryTreeNode(30)
    root.left = BinaryTreeNode(20)
    root.right = BinaryTreeNode(40)
    root.left.left = BinaryTreeNode(10)
    root.left.right = BinaryTreeNode(25)
    root.right.right = BinaryTreeNode(50)

    steps = []

    print("Enter numbers to delete from the AVL tree. Type 'done' to finish.")
    highlight_red = None

    while True:
        input_value = input("Enter a number to delete (or type 'done' to finish): ").strip()
        if input_value.lower() == 'done':
            break

        try:
            value = int(input_value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        root, highlight_red, pre_rotation = delete_from_avl(root, value)
        print(f"Node {value} deleted from the AVL tree.")

        if pre_rotation:
            steps.append(pre_rotation)
        update_heights_from_node(root)
        latex_code = generate_latex_binary_tree(root, is_root=True)
        steps.append(latex_code)
        highlight_red = None

    latex_document = generate_latex_document_steps(steps, initial_tree=BinaryTreeNode(30, BinaryTreeNode(20, BinaryTreeNode(10), BinaryTreeNode(25)), BinaryTreeNode(40, None, BinaryTreeNode(50))))
    filename = "avl_tree_deletion_steps.tex"

    with open(filename, "w") as file:
        file.write(latex_document)

    print(f"LaTeX code has been generated and saved to {filename}")

if __name__ == "__main__":
    main()
"""