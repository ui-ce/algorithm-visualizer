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
from pylatex import Document, Section, Subsection, Tabular, Figure, NoEscape, Package

processes = []

class Process:
    def __init__(self, name, burst_time, arrival_time, color):
        self.name = name
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.service_start_time = 0
        self.color = color


def srt_scheduling_latex(processes, cell_width, cell_height):
    doc = Document()
    doc.packages.append(Package('xcolor'))
    doc.packages.append(Package('tikz'))
    doc.packages.append(Package('geometry', options='left=0.5in, right=0.5in, top=1in, bottom=1in'))

    for process in processes:
        color_code = process.color.lstrip('#')
        doc.preamble.append(NoEscape(r'\definecolor{%s}{HTML}{%s}' % (process.name, color_code)))

    font_scale = min(cell_width, cell_height)

    with doc.create(Section('SRT Scheduling')):
        doc.append(NoEscape(r"""
        \section*{Introduction}
        Shortest Remaining Time (SRT) scheduling is one of the scheduling algorithms in operating systems that is used to manage processes. This algorithm is an advanced version of the Shortest Job Next (SJN) algorithm. In SRT, the process with the shortest remaining time is executed, and if a new process with a shorter remaining time enters the system, the algorithm switches to that new process.
        """))

        time = 0
        completed_processes = []
        execution_order = []
        process_queue = []

        while len(completed_processes) < len(processes):
            for process in processes:
                if process.arrival_time == time:
                    process_queue.append(process)

            if process_queue:
                current_process = min(process_queue, key=lambda x: x.remaining_time)
                if current_process.service_start_time == 0:
                    current_process.service_start_time = time
                execution_order.append((current_process.name, time, time + 1))
                current_process.remaining_time -= 1

                if current_process.remaining_time == 0:
                    current_process.completion_time = time + 1
                    process_queue.remove(current_process)
                    completed_processes.append(current_process)

                with doc.create(Subsection(f'Time {time}: Process {current_process.name}')):
                    draw_process(doc, processes, execution_order, current_process, time, cell_width, cell_height,
                                 font_scale)

            time += 1

        with doc.create(Subsection('Final Process Table')):
            with doc.create(Tabular('|c|c|c|c|')) as table:
                table.add_hline()
                table.add_row((NoEscape(r'\textbf{Process}'), NoEscape(r'\textbf{Arrival Time}'),
                               NoEscape(r'\textbf{Burst Time}'), NoEscape(r'\textbf{Completion Time}')))
                table.add_hline()
                for process in processes:
                    table.add_row((process.name, process.arrival_time, process.burst_time, process.completion_time))
                    table.add_hline()

        with doc.create(Subsection('Execution Order')):
            draw_execution_order(doc, execution_order, len(processes), cell_width, cell_height, font_scale)

    doc.generate_pdf('srt_scheduling', clean_tex=False)


def draw_process(doc, processes, execution_order, current_process, time, cell_width, cell_height, font_scale,
                 completed=False):
    with doc.create(Figure(position='h!')) as fig:
        fig.append(NoEscape(r'\centering'))
        fig.append(NoEscape(r'\begin{tikzpicture}'))
        width = cell_width * len(processes)
        fig.append(NoEscape(r'\draw[thick] (0,0) rectangle (%f, %f);' % (width, cell_height)))
        x = 0
        for name, start_time, end_time in execution_order:
            process = next(p for p in processes if p.name == name)
            fig.append(NoEscape(
                r'\node[draw, minimum width=%fcm, minimum height=%fcm, text centered, fill=%s, font=\fontsize{%d}{%d}\selectfont] at (%f, %f) {%s};' % (
                    cell_width, cell_height, process.name, int(10 * font_scale), int(12 * font_scale),
                    x + cell_width / 2, cell_height / 2, name)))
            fig.append(NoEscape(r'\node[font=\fontsize{%d}{%d}\selectfont] at (%f, -0.3) {%d};' % (
            int(8 * font_scale), int(10 * font_scale), x, start_time)))
            x += cell_width
            fig.append(NoEscape(r'\node[font=\fontsize{%d}{%d}\selectfont] at (%f, -0.3) {%d};' % (
            int(8 * font_scale), int(10 * font_scale), x, end_time)))
        fig.append(NoEscape(r'\end{tikzpicture}'))


def draw_execution_order(doc, execution_order, num_processes, cell_width, cell_height, font_scale):
    with doc.create(Figure(position='h!')) as fig:
        fig.append(NoEscape(r'\centering'))
        fig.append(NoEscape(r'\begin{tikzpicture}'))
        width = cell_width * num_processes
        fig.append(NoEscape(r'\draw[thick] (0,0) rectangle (%f, %f);' % (width, cell_height)))
        x = 0
        for name, start_time, end_time in execution_order:
            process = next(p for p in processes if p.name == name)
            fig.append(NoEscape(
                r'\node[draw, minimum width=%fcm, minimum height=%fcm, text centered, font=\fontsize{%d}{%d}\selectfont, fill=%s] at (%f, %f) {%s};' % (
                    cell_width, cell_height, int(10 * font_scale), int(12 * font_scale), process.name,
                    x + cell_width / 2, cell_height / 2, name)))
            fig.append(NoEscape(r'\node[font=\fontsize{%d}{%d}\selectfont] at (%f, -0.3) {%d};' % (
            int(8 * font_scale), int(10 * font_scale), x, start_time)))
            x += cell_width
            fig.append(NoEscape(r'\node[font=\fontsize{%d}{%d}\selectfont] at (%f, -0.3) {%d};' % (
            int(8 * font_scale), int(10 * font_scale), x, end_time)))
        fig.append(NoEscape(r'\end{tikzpicture}'))

