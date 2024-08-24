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
"""
processes = []
is_invalid = False
while not is_invalid:
    processes_count = int(input("Enter number of processes(between 1 and 8): "))
    if 8 >= processes_count >= 1:
        is_invalid = True
    else:
        print("Please enter a valid number of processes.")

for i in range(processes_count):
    arrival_time = int(input(f"Enter arrival time for process {i + 1} (>=0): "))
    while arrival_time < 0:
        print("Please enter a valid arrival time.")
        arrival_time = int(input(f"Enter arrival time for process {i + 1} (>=0): "))

    burst_time = int(input(f"Enter burst time for process {i + 1} (>=1): "))
    while burst_time < 1:
        print("Please enter a valid burst time.")
        burst_time = int(input(f"Enter burst time for process {i + 1} (>=1): "))

    processes.append((arrival_time, burst_time))

num_queues = int(input("Enter number of priority queues: "))
time_quantums = []
for i in range(num_queues):
    time_quantum = int(input(f"Enter time quantum for queue {i + 1}: "))
    time_quantums.append(time_quantum)

latex_code = generate_mlfq_latex(processes, time_quantums)

with open("mlfq_queue.tex", "w") as f:
    f.write(latex_code)

print("LaTeX code generated and saved to mlfq_queue.tex")
"""