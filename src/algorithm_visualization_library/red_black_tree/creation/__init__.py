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
from .node import RedBlackNode
from .tree import RedBlackTree
from .tree import generate_latex_red_black_tree
from .tree import generate_latex_document_steps_red_black

__all__ = {'RedBlackNode',
           'RedBlackTree',
           'generate_latex_red_black_tree',
           'generate_latex_document_steps_red_black'},
