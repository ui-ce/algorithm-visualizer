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
    steps = []
    try:
        while True:
            value = int(input("Enter a value to append to the single linked list (or type 'done' to finish): "))
            dll.append(value)
            steps.append(dll.generate_latex_for_state())
    except ValueError:
        pass

    combined_latex_code = dll.generate_combined_latex(steps)

    with open("doubly_linked_list_steps.tex", "w") as file:
        file.write(combined_latex_code)

    print("Step-by-step LaTeX code generated and saved to single_linked_list_steps.tex")

if __name__ == "__main__":
    main()
"""
