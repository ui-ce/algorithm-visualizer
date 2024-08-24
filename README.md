# **'Algorithm_Visualization_Library'**

### **Overview**
The algorithm_visualization_library is a Python library designed to help developers and educators visualize algorithms and data structures in a clear and intuitive manner. The library leverages LaTeX and TikZ to generate high-quality visual representations, making it easier to understand complex concepts like linked lists, binary trees, AVL trees, and Red-Black trees.

Today, the performance of algorithms plays a very important role in various fields, including computer science, engineering, basic sciences, and even our daily lives. However, understanding the concepts related to algorithms can be challenging for many people. The purpose of this research is to provide an innovative solution to facilitate the learning process of algorithms through visual visualization and user interaction. Additionally, users can understand how an algorithm works by observing its performance and viewing a step-by-step implementation. The use of visual and interactive methods in this tool makes learning algorithms more engaging, especially for those who may not have an inherent interest in abstract concepts.

In this research, users can provide basic information about their desired algorithm, which is in the list of implemented algorithms. Then, the system will illustrate the algorithm's steps visually, step by step, using LaTeX.

### **Applications** 
The applications of this project span:
- teaching 
- learning 
- research 
- reference

In education and teaching, this tool can be used in classrooms, textbooks, online courses, or self-study to teach computer algorithms. In learning, students can use this tool to grasp algorithm concepts visually. In research, researchers can utilize this tool to analyze the performance of different algorithms. Additionally, in the reference section, this tool can serve as a valuable resource for individuals working on articles or research.

## **How to use this libary**
First, if you need to use this library, you should install these two dependencies (as listed in requirements.txt):

- setuptools~=72.1.0
- PyLaTeX~=1.4.2


As you can see, in the algorithm_visualization_library, the data structure algorithms are organized within individual folders. Some algorithms have internal folders, which indicates they contain sub-algorithms. For example, in the tree folder, there are five main operations: creating a tree, deleting a given node, inserting a given node, searching for a given node, and traversing the tree.
In each folder, there are two key files that are accessible to all algorithms:



+ __init__.py: The __init__.py file is a crucial part of Python packages. It is executed when the package is imported and serves multiple purposes, such as initializing the package, defining what is available to users, and managing package-level configuration.


Example: BubbleSort/__init__.py 

Consider the BubbleSort folder in your algorithm_visualization_library. Inside the BubbleSort folder, you have an __init__.py file that might look like this:


```python
# BubbleSort/__init__.py
from .input_handler import get_user_input
from .latex_generator import generate_latex_code

__all__ = ['get_user_input', 'generate_latex_code']
```

```python
from .input_handler import get_user_input: #This line imports the get_user_input function from the input_handler.py file within the BubbleSort package. This allows users to access the get_user_input function directly from the BubbleSort package.

from .latex_generator import generate_latex_code: #Similar to the previous line, this imports the generate_latex_code function from the latex_generator.py file within the same package.

__all__: This special variable is a list of public objects of that module, as interpreted by the import * statement. When from BubbleSort import * is used, only the names included in __all__ will be imported. This ensures that only the specified functions (get_user_input and generate_latex_code) are available to users, keeping the package's interface clean and controlled.
```



Each folder in the library contains its own __init__.py file, and each of these files is responsible for managing the lower-level module or package beneath it. This setup creates a layered structure where each __init__.py file defines the functionalities of the modules within its respective directory. As you move up the directory tree, these __init__.py files collaborate, progressively assembling the complete functionality of the library. At the top level, the main __init__.py file consolidates and exposes the full set of capabilities provided by the entire library.


```python
# For our main folder __init__.py  for bubble_sort might look like this:

# algorithm_visualization_library/__init__.py

# bubble_sort
from .bubble_sort.latex_generator import generate_latex_code
from .bubble_sort.input_handler import get_user_input
```



Each __init__.py file within a folder reveals the contents of that specific module, organizing and exposing the functionalities available within it. The main __init__.py file at the top level of the algorithm_visualization_library then consolidates all these individual modules, providing an overview of all the algorithms and data structures that the library supports. This structure ensures that each folder’s __init__.py file focuses on its own components, while the main __init__.py file presents a unified interface for the entire library.

+ usage_example.py: The usage_example.py file is typically a script provided within a library's repository to demonstrate how the library can be used. It serves as a practical guide for users who want to see the library in action without having to read through the entire documentation. Below is an example structure for a usage_example.py file in your algorithm_visualization_library:

for all algorithms you should first import and then use usage_example.py file. for importing write like this:

```
1- write: from algorithm_visualization_library.algorithm_name_file/algorithm_name_folder two examples:
```

```python
- from algorithm_visualization_library.merge_sort import *
- from algorithm_visualization_library.avl_tree.creation import *
```

```
2- after that write . to see what files does that algorithm have.import all files. don't use usage_example(this file will be used after). 
```

```
3- write import *
```

```
4- importing is done, now use go to .algorithm_name_folder/useage_example and copy all to your file and this file is how to use functions and classes you can change but you should use this file beacuse it gives you a template.
```

```python
* example:
if we want to use mergesort algorithm after installation liabry in another main.py we have we can wirte:

from algorithm_visualization_library.merge_sort.merge_sort_visualization import *

now here just copy usage_example.py here like this and run:
input_array = input("Enter a list of numbers separated by spaces: ")
width = float(input("Enter the width of each array cell: "))
height = float(input("Enter the height of each array cell: "))
color_left = input("Enter the color code for the left half of the array (e.g., #FF0000): ")
color_right = input("Enter the color code for the right half of the array (e.g., #0000FF): ")
color_merge = input("Enter the color code for the merged array (e.g., #00FF00): ")

arr = list(map(int, input_array.split()))

color_map = {
    'leftcolor': color_left,
    'rightcolor': color_right,
    'mergecolor': color_merge
}

create_visualization(arr, width, height, color_map)
```








## installation:

To install the algorithm_visualization_library, you can use one of the following methods:

1. Install via pip (if published on PyPI)
If your library is published on PyPI (Python Package Index), users can install it easily using pip:
open your terminal write:
```
 pip install -i https://test.pypi.org/simple/ algorithm-visualization-library
```
2. Install from Source
```
Clone the repository:

1- https://github.com/ui-ce/algorithm-visualizer

2- Navigate to the library's directory
cd algorithm_visualization_library

3- Install the library:
pip install .
This will install the algorithm_visualization_library along with all its dependencies.

4.If you want to use this libary in another path on your os copy libary address that you clone and write this to your terminal:

pip install <libary address path>

5. Install using a requirements file
If your project includes a requirements.txt file with dependencies:


pip install -r requirements.txt
This command installs all the necessary packages listed in the requirements.txt file, including your library.
```
