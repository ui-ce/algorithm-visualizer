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
def generate_rr_latex(processes, time_quantum):
    colors = ['red', 'blue', 'green', 'black', 'cyan']

    latex_code = r"""\documentclass{article}
\usepackage{amsmath}
\usepackage{tikz}
\usepackage{longtable}
\usepackage{xcolor}
\begin{document}

\title{RR Queue Process}
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
\subsection*{Process Execution}
"""

    sorted_processes = sorted(enumerate(processes), key=lambda x: x[1][0])

    current_time = 0
    remaining_burst_times = [burst_time for _, burst_time in processes]
    completion_times = [None] * len(processes)
    start_times = [-1] * len(processes)
    ready_queue = []
    arrival_idx = 0
    gantt_chart_steps = []

    while any(rt > 0 for rt in remaining_burst_times):
        new_arrivals = []
        while arrival_idx < len(sorted_processes) and sorted_processes[arrival_idx][1][0] <= current_time:
            process_index = sorted_processes[arrival_idx][0]
            new_arrivals.append(process_index)
            arrival_idx += 1

        ready_queue = new_arrivals + ready_queue

        if ready_queue:
            latex_code += f"At time {current_time}, the queue is:\n\n"
            latex_code += r"\begin{center}\begin{tikzpicture}"

            for j, q_process_index in enumerate(ready_queue):
                color = colors[q_process_index % len(colors)]
                latex_code += f"\\draw[thick, {color}] ({j * 1.5},0) rectangle ({(j + 1) * 1.5},1) node[pos=.5] {{P{q_process_index + 1}}};"

            latex_code += r"\end{tikzpicture}\end{center}" + "\n\n"

            process_index = ready_queue.pop(0)
            latex_code += f"Process {process_index + 1} is selected for execution.\n\n"

            if remaining_burst_times[process_index] > 0:
                if start_times[process_index] == -1:
                    start_times[process_index] = max(current_time, sorted_processes[process_index][1][
                        0])
                actual_burst = min(time_quantum, remaining_burst_times[process_index])
                start_time = current_time
                current_time += actual_burst
                remaining_burst_times[process_index] -= actual_burst

                if remaining_burst_times[process_index] == 0:
                    completion_times[process_index] = current_time
                else:
                    ready_queue.append(process_index)
                gantt_chart_steps.append((process_index + 1, start_time, current_time))
                latex_code += r"""
\subsection*{Gantt Chart after this step}
\begin{center}
\begin{tabular}{|l|l|}
\hline
Process & Execution Interval \\
\hline
"""

                for p_id, start_time, end_time in gantt_chart_steps:
                    latex_code += f"P{p_id} & [{start_time}, {end_time}) \\\\\n"
                    latex_code += r"\hline" + "\n"

                latex_code += r"""
\end{tabular}
\end{center}

"""

        else:
            current_time += 1
    latex_code += r"""
\end{document}
"""

    return latex_code
