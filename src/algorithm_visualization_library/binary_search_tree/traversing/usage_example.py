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
1--Level_Order
def main():
    # Define a Binary Search Tree (BST)
    root = BinaryTreeNode(10)
    root.left = BinaryTreeNode(5)
    root.right = BinaryTreeNode(20)
    root.left.left = BinaryTreeNode(3)
    root.left.right = BinaryTreeNode(7)
    root.right.left = BinaryTreeNode(15)
    root.right.right = BinaryTreeNode(25)

    steps = []
    breadth_first_traversal(root, steps)

    latex_document = generate_latex_document_steps(steps)
    filename = "bst_bfs_steps.tex"

    with open(filename, "w") as file:
        file.write(latex_document)

    print(f"LaTeX code for binary search tree BFS steps has been generated and saved to {filename}")

if __name__ == "__main__":
    main()

"""

"""
2--depth_Order
def main():
    root = BinaryTreeNode(10)
    root.left = BinaryTreeNode(5)
    root.right = BinaryTreeNode(20)
    root.left.left = BinaryTreeNode(3)
    root.left.right = BinaryTreeNode(7)
    root.right.left = BinaryTreeNode(15)
    root.right.right = BinaryTreeNode(25)

    steps = [generate_latex_binary_tree(root, is_root=True)]

    print("Choose the type of traversal:")
    print("1. Pre-order")
    print("2. In-order")
    print("3. Post-order")
    
    choice = int(input("Enter your choice (1/2/3): ").strip())

    if choice == 1:
        pre_order_traversal(root, steps)
    elif choice == 2:
        in_order_traversal(root, steps)
    elif choice == 3:
        post_order_traversal(root, steps)
    else:
        print("Invalid choice.")
        return

    latex_document = generate_latex_document_steps(steps)
    filename = "bst_dfs_steps.tex"

    with open(filename, "w") as file:
        file.write(latex_document)

    print(f"LaTeX code for binary search tree traversal steps has been generated and saved to {filename}")

if __name__ == "__main__":
    main()
"""