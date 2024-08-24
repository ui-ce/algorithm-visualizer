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
def generate_fcfs_latex(processes):
    colors = ['red', 'blue', 'green', 'black', 'cyan']

    latex_code = r"""\documentclass{article}
\usepackage{amsmath}
\usepackage{tikz}
\usepackage{longtable}
\usepackage{xcolor}
\begin{document}

\title{FCFS Queue Process}
\author{}
\date{}
\maketitle

\section*{Process Arrival}
\begin{itemize}
"""

    for i, (arrival_time, burst_time) in enumerate(processes):
        latex_code += f"    \\item Process {i + 1} arrives at time {arrival_time} with burst time {burst_time}\n"

    latex_code += r"""
\end{itemize}

\section*{Queue States}
\subsection*{Arrival of Processes}
"""

    sorted_processes = sorted(enumerate(processes), key=lambda x: x[1][0])

    queue = []
    current_time = 0
    for i, (arrival_time, burst_time) in sorted_processes:
        current_time = max(current_time, arrival_time)
        queue.append((i, burst_time))

        latex_code += f"Process {i + 1} arrives at time {arrival_time}:\n\n"
        latex_code += r"\begin{center}\begin{tikzpicture}"

        color = colors[i % len(colors)]
        latex_code += f"\\draw[thick, {color}] (-2.5,0) rectangle (-1.25,0.5) node[pos=.5, scale=0.8] {{P{i + 1}}};"

        for j, (process_index, _) in enumerate(queue):
            color = colors[process_index % len(colors)]
            latex_code += f"\\draw[thick, {color}] ({(j + 1) * 1.5},0) rectangle ({(j + 2) * 1.5},1) node[pos=.5] {{P{process_index + 1}}};"

        latex_code += r"\end{tikzpicture}\end{center}" + "\n\n"

    latex_code += r"""
\subsection*{Exit of Processes}
"""

    completion_times = []
    current_time = 0
    for i, (process_index, burst_time) in enumerate(queue):
        arrival_time = processes[process_index][0]
        start_time = max(current_time, arrival_time)
        current_time = start_time + burst_time
        completion_times.append(current_time)

        latex_code += f"Process {process_index + 1} exits at time {current_time}:\n\n"
        latex_code += r"\begin{center}\begin{tikzpicture}"

        for j, (remaining_process_index, _) in enumerate(queue[i + 1:]):
            color = colors[remaining_process_index % len(colors)]
            latex_code += f"\\draw[thick, {color}] ({(j + 1) * 1.5},0) rectangle ({(j + 2) * 1.5},1) node[pos=.5] {{P{remaining_process_index + 1}}};"

        color = colors[process_index % len(colors)]
        latex_code += f"\\draw[thick, {color}] ({(len(queue) - i) * 1.5 + 2.5},0) rectangle ({(len(queue) - i + 1) * 1.5 + 2.5},0.5) node[pos=.5, scale=0.8] {{P{process_index + 1}}};"

        if i == len(queue) - 1:
            latex_code += r"\node at (0,0.5) {Empty};"

        latex_code += r"\end{tikzpicture}\end{center}" + "\n\n"

    latex_code += r"""
\end{document}
"""

    return latex_code
