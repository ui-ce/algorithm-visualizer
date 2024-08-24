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

    method = input("Do you want to see the final tree or the step-by-step representation? (final/steps): ").strip().lower()

    print("Enter numbers to insert into the BST. Type 'done' to finish.")

    while True:
        input_value = input("Enter a number (or type 'done' to finish): ").strip()
        if input_value.lower() == 'done':
            break

        try:
            value = int(input_value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        root = add_node(root, value)
        print(f"Node {value} added to the BST.")

        if method == 'steps':
            latex_code = generate_latex_binary_tree(root, is_root=True)
            steps.append(latex_code)

    if method == 'final':
        latex_document = generate_latex_document(root)
        filename = "binary_search_tree_final.tex"
    elif method == 'steps':
        latex_document = generate_latex_document_steps(steps)
        filename = "binary_search_tree_steps.tex"
    else:
        print("Invalid method selected.")
        return

    with open(filename, "w") as file:
        file.write(latex_document)

    print(f"LaTeX code has been generated and saved to {filename}")

if __name__ == "__main__":
    main()
"""