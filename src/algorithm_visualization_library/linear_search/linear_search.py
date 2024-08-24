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
def linear_search(arr, target):
    steps = []
    for i in range(len(arr)):
        if arr[i] == target:
            steps.append((i, True))
            return i, steps
        else:
            steps.append((i, False))
    return -1, steps

def generate_latex(arr, steps, target, color_found, color_not_found):
    latex_code = """
\\documentclass{article}
\\usepackage[margin=0.5in]{geometry}
\\usepackage{xcolor}
\\usepackage{tikz}
\\usepackage{amsmath}
\\usepackage{ifthen}
\\usetikzlibrary{shapes, arrows.meta, positioning}
\\begin{document}
\\begin{center}
\\Large\\textbf{Linear Search Step-by-Step}
\\end{center}
\\vspace{1cm}
Searching for \\textbf{""" + str(target) + """} in array:\\\\
\\begin{center}
"""

    total_width = len(arr) * 1.2

    latex_code += f"\\definecolor{{found}}{{HTML}}{{{color_found.lstrip('#')}}}\n"
    latex_code += f"\\definecolor{{notfound}}{{HTML}}{{{color_not_found.lstrip('#')}}}\n"

    for step, (index, found) in enumerate(steps):
        latex_code += "\\begin{tikzpicture}[scale=0.8, every node/.style={font=\\normalsize}]\n"
        latex_code += "\\node[above] at (0, 1.5) {\\textbf{Step %d}};\n" % (step + 1)
        for i, val in enumerate(arr):
            if i == index:
                color = 'found' if found else 'notfound'
                latex_code += f"\\node[draw, fill={color}, rectangle, minimum size=1cm, anchor=north] at ({i*1.2 - total_width/2 + 0.6}, 0) {{\\textbf{{{val}}}}};\n"
            else:
                latex_code += f"\\node[draw, fill=gray!10, rectangle, minimum size=1cm, anchor=north] at ({i*1.2 - total_width/2 + 0.6}, 0) {{\\textbf{{{val}}}}};\n"
        latex_code += "\\end{tikzpicture}\n"
        latex_code += "\\\\[0.5cm]\n" 

    latex_code += """
\\end{center}
\\end{document}
"""
    return latex_code