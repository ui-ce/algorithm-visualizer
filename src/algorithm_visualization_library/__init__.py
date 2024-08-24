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
# algorithm_visualization_library/__init__.py

# bubble_sort
from .bubble_sort.latex_generator import generate_latex_code
from .bubble_sort.input_handler import get_user_input

# quick_sort
from .quick_sort import quick_sort_visualization

# insertion_sort
from .insertion_sort import insertion_sort

# linear_search
from .linear_search import linear_search

# merge_sort
from .merge_sort import merge_sort_visualization

# selection_sort
from .selection_sort import selection_sort

# binary_search
from .binary_serach import binary_search_visualization

# MLFQ
from .MLFQ import MLFQ

# round_robin
from .round_robin import round_robin

# single_linked_list
from .single_linked_list import creation
from .single_linked_list import deletion
from .single_linked_list import insertion
from .single_linked_list import Searching

# double_linked_list
from .double_linked_list import creation
from .double_linked_list import deletion
from .double_linked_list import insertion
from .double_linked_list import searching

# queue_with_two_stacks
from .queue_with_two_stacks import queue_two_stacks

# priority_scheduling
from .priority_scheduling import priority_scheduling_visualization

# shortest_remaining_time
from .shortest_remaining_time import shortest_remaining_time_visualization

# shortest_job_next
from .shortest_job_next import shortest_job_next_visualization

# stack
from .stack import stack_visualization
from .stack_implementation_with_queue import stack_implementation_with_queue_visualization

# binary_tree
from .binary_tree import creation
from .binary_tree import deletion
from .binary_tree import insertion
from .binary_tree import searching
from .binary_tree import traversing

# binary_search_tree
from .binary_search_tree import creation
from .binary_search_tree import deletion
from .binary_search_tree import insertion
from .binary_search_tree import searching
from .binary_search_tree import traversing

# avl_tree
from .avl_tree import creation
from .avl_tree import deletion
from .avl_tree import insertion

# red_black_tree
from .red_black_tree import creation
from .red_black_tree import deletion
from .red_black_tree import insertion
