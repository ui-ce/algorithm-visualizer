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
def selection_sort(arr):
    steps = []
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            steps.append((list(arr), i, min_idx, j))
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append((list(arr), i, min_idx, -1))  
    return steps


def generate_latex(arr, steps, color_key, color_min, color_compared):
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
\\Large\\textbf{Selection Sort Step-by-Step}
\\end{center}
\\vspace{1cm}
Sorting array:\\\\
\\begin{center}
"""

    total_width = len(arr) * 1.2

    latex_code += f"\\definecolor{{keycolor}}{{HTML}}{{{color_key.lstrip('#')}}}\n"
    latex_code += f"\\definecolor{{mincolor}}{{HTML}}{{{color_min.lstrip('#')}}}\n"
    latex_code += f"\\definecolor{{compared}}{{HTML}}{{{color_compared.lstrip('#')}}}\n"

    for step, (current_arr, key_idx, min_idx, comp_idx) in enumerate(steps):
        latex_code += "\\begin{tikzpicture}[scale=0.8, every node/.style={font=\\normalsize}]\n"
        latex_code += "\\node[above] at (0, 1.5) {\\textbf{Step %d}};\n" % (step + 1)
        for i, val in enumerate(current_arr):
            if i == key_idx:
                latex_code += f"\\node[draw, fill=keycolor, rectangle, minimum size=1cm, anchor=north] at ({i*1.2 - total_width/2 + 0.6}, 0) {{\\textbf{{{val}}}}};\n"
            elif i == min_idx:
                latex_code += f"\\node[draw, fill=mincolor, rectangle, minimum size=1cm, anchor=north] at ({i*1.2 - total_width/2 + 0.6}, 0) {{\\textbf{{{val}}}}};\n"
            elif i == comp_idx:
                latex_code += f"\\node[draw, fill=compared, rectangle, minimum size=1cm, anchor=north] at ({i*1.2 - total_width/2 + 0.6}, 0) {{\\textbf{{{val}}}}};\n"
            else:
                latex_code += f"\\node[draw, fill=gray!10, rectangle, minimum size=1cm, anchor=north] at ({i*1.2 - total_width/2 + 0.6}, 0) {{\\textbf{{{val}}}}};\n"
        latex_code += "\\end{tikzpicture}\n"
        latex_code += "\\\\[0.5cm]\n"  

    latex_code += """
\\end{center}
\\end{document}
"""
    return latex_code
