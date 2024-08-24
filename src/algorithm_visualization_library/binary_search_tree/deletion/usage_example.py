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
    root = BinaryTreeNode(50)
    root = add_node(root, 30)
    root = add_node(root, 70)
    root = add_node(root, 20)
    root = add_node(root, 40)
    root = add_node(root, 60)
    root = add_node(root, 80)

    steps = []

    method = input("Do you want to see the final tree or the step-by-step representation? (final/steps): ").strip().lower()

    while True:
        operation = input("Enter operation (delete) or type 'done' to finish: ").strip().lower()
        if operation == 'done':
            break

        if operation != 'delete':
            print("Invalid operation. Please enter 'delete' or 'done'.")
            continue

        input_value = input("Enter a number: ").strip()

        try:
            value = int(input_value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if operation == 'delete':
            before_state = generate_latex_binary_tree(root, new_node=value, is_step=True, is_root=True)

            root = delete_node(root, value)
            print(f"Node {value} deleted from the BST.")

            after_state = generate_latex_binary_tree(root, is_step=False, is_root=True)
            steps.append((before_state, after_state))

    if method == 'final':
        latex_document = generate_latex_document(root)
        filename = "binary_search_tree_final.tex"
    elif method == 'steps':
        latex_document = generate_latex_document_steps(steps)
        filename = "binary_search_tree_deletion_steps.tex"
    else:
        print("Invalid method selected.")
        return

    with open(filename, "w") as file:
        file.write(latex_document)

    print(f"LaTeX code has been generated and saved to {filename}")

if __name__ == "__main__":
    main()
"""