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
from .quick_sort_visualization import partition
from .quick_sort_visualization import quickSort
from .quick_sort_visualization import update_steps
from .quick_sort_visualization import get_square_size
from .quick_sort_visualization import get_colors
from .quick_sort_visualization import save_steps_as_tikz


__all__ = ['partition',
           'quickSort',
           'update_steps',
           'get_square_size',
           'get_colors',
           'save_steps_as_tikz']
