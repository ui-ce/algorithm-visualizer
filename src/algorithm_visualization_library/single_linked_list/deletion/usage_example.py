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
    dll = SingleLinkedList()
    dll.append(12)
    dll.append(99)
    dll.append(100)
    dll.append(250)
    dll.append(120)
    dll.append(1)
    dll.append(-10)

    latex_code_before = dll.generate_latex_for_state()

    try:
        operation = input("Enter 'delete_index' to delete a node by index or 'delete_value' to delete a node by value: ").strip().lower()

        if operation == 'delete_index':
            index = int(input("Enter the index of the node to delete: "))
            dll.delete_at_index(index)
        elif operation == 'delete_value':
            value = int(input("Enter the value of the node to delete: "))
            dll.delete_by_value(value)
        else:
            raise ValueError("Invalid operation. Please enter 'delete_index' or 'delete_value'.")

        latex_code_after = dll.generate_latex_for_state()
        combined_latex_code = dll.generate_combined_latex(latex_code_before, latex_code_after)

        with open("Single_linked_list_combined.tex", "w") as file:
            file.write(combined_latex_code)

        print("Combined LaTeX code generated and saved to Single_linked_list_combined.tex")
    except (IndexError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()
"""