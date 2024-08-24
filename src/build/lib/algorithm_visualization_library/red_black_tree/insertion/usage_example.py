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
def main_red_black():
    rb_tree = RedBlackTree()

    predefined_values = [20, 15, 25, 10, 5]
    for value in predefined_values:
        rb_tree.insert(value)

    steps = [generate_latex_red_black_tree(rb_tree.root, rb_tree, is_root=True)]

    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        if user_input.lower() == 'done':
            break

        try:
            value = int(user_input)
            step_result = rb_tree.insert(value)
            steps.extend(step_result)
            print(f"Node {value} added to the Red-Black tree.")

            with open("red_black_tree_steps.tex", "w") as f:
                f.write(generate_latex_document_steps_red_black(steps))
            print("LaTeX file 'red_black_tree_steps.tex' has been generated.")

        except ValueError:
            print("Please enter a valid number or 'done' to finish.")

if __name__ == "__main__":
    main_red_black()
"""