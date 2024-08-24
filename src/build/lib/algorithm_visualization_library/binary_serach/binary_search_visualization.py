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
from pylatex import Document, Section, TikZ, Figure, NoEscape


def create_visualization(arr, target, width, height, left_color, right_color, mid_color, bg_color, target_color):

    doc = Document()

    doc.preamble.append(NoEscape(r'\usepackage[a4paper, left=0.5in, top=0.5in]{geometry}'))

    with doc.create(Section('Binary Search Visualization')):
        doc.append(NoEscape(r"""
        \section*{Introduction}
        Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one. 
        """))
        doc.preamble.append(NoEscape(r'\usepackage{xcolor}'))
        doc.preamble.append(NoEscape(r'\definecolor{leftcolor}{HTML}{%s}' % left_color.lstrip('#')))
        doc.preamble.append(NoEscape(r'\definecolor{rightcolor}{HTML}{%s}' % right_color.lstrip('#')))
        doc.preamble.append(NoEscape(r'\definecolor{midcolor}{HTML}{%s}' % mid_color.lstrip('#')))
        doc.preamble.append(NoEscape(r'\definecolor{bgcolor}{HTML}{%s}' % bg_color.lstrip('#')))
        doc.preamble.append(NoEscape(r'\definecolor{targetcolor}{HTML}{%s}' % target_color.lstrip('#')))

        with doc.create(Figure(position='h!')) as initial_fig:
            with initial_fig.create(TikZ()) as tikz:
                draw_array(tikz, arr, 'Initial Array', width, height, None, None, None, False, None)

        arr.sort()
        with doc.create(Figure(position='h!')) as sorted_fig:
            with sorted_fig.create(TikZ()) as tikz:
                draw_array(tikz, arr, 'Sorted Array', width, height, None, None, None, False, None)

        left, right = 0, len(arr) - 1
        step = 1
        target_index = None
        while left <= right:
            mid = left + (right - left) // 2

            with doc.create(Figure(position='h!')) as step_fig:
                with step_fig.create(TikZ()) as tikz:
                    draw_array(tikz, arr, f'Step {step}', width, height, left, right, mid, False, None)
                

            if arr[mid] == target:
                target_index = mid
                break
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

            step += 1

        if target_index is not None:
            with doc.create(Figure(position='h!')) as final_fig:
                with final_fig.create(TikZ()) as tikz:
                    draw_array(tikz, arr, 'Final Step', width, height, None, None, None, True, target_index)

    doc.generate_pdf('binary_search_visualization', clean_tex=False)


def draw_array(tikz, arr, title, width, height, left=None, right=None, mid=None, target_found=False, target_index=None):
 
    value_font_size = height * 8
    index_font_size = height * 8
    label_font_size = height * 8
    title_font_size = height * 10

    tikz.append(NoEscape(r'\node at (0,%f) {\textbf{\fontsize{%f}{%f}\selectfont %s}};' % (
    height * 1.5, title_font_size, title_font_size * 1.2, title)))

    for i, val in enumerate(arr):
        if target_found and target_index == i:
            tikz.append(
                NoEscape(r'\fill[targetcolor] (%f, 0) rectangle (%f, -%f);' % (width * i, width * (i + 1), height)))
        else:
            tikz.append(NoEscape(r'\fill[bgcolor] (%f, 0) rectangle (%f, -%f);' % (width * i, width * (i + 1), height)))

        tikz.append(NoEscape(r'\draw (%f, 0) rectangle (%f, -%f);' % (width * i, width * (i + 1), height)))
        tikz.append(NoEscape(r'\node at (%f, -%f) {\fontsize{%f}{%f}\selectfont %d};' % (
        width * (i + 0.5), height / 2, value_font_size, value_font_size * 0.8, val)))
        index_vertical_offset = height / 5
        tikz.append(NoEscape(r'\node at (%f, %f) {\fontsize{%f}{%f}\selectfont %d};' % (
        width * (i + 0.5), height / 5 + index_vertical_offset, index_font_size, index_font_size * 0.8, i)))

    if left is not None and right is not None and mid is not None and not target_found:
        radius = height / 2  

        tikz.append(NoEscape(
            r'\draw[leftcolor, very thick] (%f, %f) circle (%f);' % (width * (left + 0.5), -height / 2, radius)))
        tikz.append(NoEscape(
            r'\draw[rightcolor, very thick] (%f, %f) circle (%f);' % (width * (right + 0.5), -height / 2, radius)))
        tikz.append(
            NoEscape(r'\draw[midcolor, very thick] (%f, %f) circle (%f);' % (width * (mid + 0.5), -height / 2, radius)))

        positions = {}
        for idx, color, label in [(left, 'leftcolor', 'Left'), (right, 'rightcolor', 'Right'),
                                  (mid, 'midcolor', 'Mid')]:
            if idx is not None:
                pos = width * (idx + 0.5)
                if pos in positions:
                    positions[pos].append(label)
                else:
                    positions[pos] = [label]

        vertical_spacing = radius  

        for pos, labels in positions.items():
            for i, label in enumerate(labels):
                tikz.append(NoEscape(r'\node[below] at (%f, %f) {\fontsize{%f}{%f}\selectfont %s};' % (
                pos, -height * 1 - i * vertical_spacing, label_font_size, label_font_size * 0.8, label)))

