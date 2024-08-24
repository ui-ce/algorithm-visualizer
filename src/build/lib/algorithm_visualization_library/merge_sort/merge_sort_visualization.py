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

def draw_array(tikz, arr, title, width, height, color_map=None, show_values=True):

    title_font_size = height * 10
    tikz.append(NoEscape(r'\node at (0,%f) {\textbf{\fontsize{%f}{%f}\selectfont %s}};' % (height * 1.5, title_font_size, title_font_size * 1.2, title)))

    for i, val in enumerate(arr):
        color = color_map.get(i, 'white') if color_map else 'white'
        tikz.append(NoEscape(r'\fill[%s] (%f, 0) rectangle (%f, -%f);' % (color, width * i, width * (i + 1), height)))
        tikz.append(NoEscape(r'\draw (%f, 0) rectangle (%f, -%f);' % (width * i, width * (i + 1), height)))
        if show_values:
            tikz.append(NoEscape(r'\node at (%f, -%f) {\fontsize{%f}{%f}\selectfont %d};' % (width * (i + 0.5), height / 2, height * 8, height * 6, val)))
            tikz.append(NoEscape(r'\node at (%f, %f) {\fontsize{%f}{%f}\selectfont %d};' % (width * (i + 0.5), height / 4, height * 8, height * 6, i)))


def merge_sort_visualize(arr, width, height, doc, color_map):
    divide_steps = []
    merge_steps = []

    original_arr = arr.copy()  

    def merge_sort(arr, left, right, level):
        if left < right:
            mid = (left + right) // 2

            merge_sort(arr, left, mid, level + 1)
            merge_sort(arr, mid + 1, right, level + 1)

            color_map_step = {i: 'leftcolor' if left <= i <= mid else 'rightcolor' for i in range(left, right + 1)}
            divide_steps.append((original_arr.copy(), f'Split [{left}, {right}]', color_map_step, level))

            merge(arr, left, mid, right)

            color_map_step = {i: 'mergecolor' for i in range(left, right + 1)}
            merge_steps.append((arr.copy(), f' Merge [{left}, {right}]', color_map_step, level))

    def merge(arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        L = [0] * n1
        R = [0] * n2

        for i in range(0, n1):
            L[i] = arr[left + i]

        for j in range(0, n2):
            R[j] = arr[mid + 1 + j]

        i = 0
        j = 0
        k = left

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    merge_sort(arr, 0, len(arr) - 1, 0)

    divide_steps.sort(key=lambda x: x[3])
    merge_steps.sort(key=lambda x: x[3], reverse=True) 

    with doc.create(Section('Division Steps')):
        for arr, title, color_map_step, level in divide_steps:
            with doc.create(Figure(position='h!')) as fig:
                with fig.create(TikZ()) as tikz:
                    draw_array(tikz, arr, title, width, height, color_map=color_map_step, show_values=True)


        with doc.create(Section('Merge Steps')):
            for arr, title, color_map_step, level in merge_steps:
                with doc.create(Figure(position='h!')) as fig:
                    with fig.create(TikZ()) as tikz:
                        draw_array(tikz, arr, title, width, height, color_map=color_map_step, show_values=True)


def create_visualization(arr, width, height, color_map):
    doc = Document()
    doc.preamble.append(NoEscape(r'\usepackage{geometry}'))
    doc.preamble.append(NoEscape(r'\geometry{a4paper, left=0.5in, top=0.5in}'))
    doc.preamble.append(NoEscape(r'\usepackage{tikz}'))
    doc.preamble.append(NoEscape(r'\usepackage{xcolor}'))

    for color_name, color_code in color_map.items():
        doc.preamble.append(NoEscape(r'\definecolor{%s}{HTML}{%s}' % (color_name, color_code.lstrip('#'))))

    with doc.create(Section('Merge Sort Visualization')):
        doc.append(NoEscape(r"""
        \section*{Introduction}
        Merge sort is one of the most efficient sorting algorithms. It works on the principle of Divide and Conquer based on the idea of breaking down a list into several sub-lists until each sublist consists of a single element and merging those sublists in a manner that results into a sorted list.
        """))
        merge_sort_visualize(arr, width, height, doc, color_map)
    doc.generate_pdf('merge_sort_visualization', clean_tex=False)
