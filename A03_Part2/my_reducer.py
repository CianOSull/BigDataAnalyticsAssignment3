#!/usr/bin/python
# --------------------------------------------------------
#
# PYTHON PROGRAM DEFINITION
#
# The knowledge a computer has of Python can be specified in 3 levels:
# (1) Prelude knowledge --> The computer has it by default.
# (2) Borrowed knowledge --> The computer gets this knowledge from 3rd party libraries defined by others
#                            (but imported by us in this program).
# (3) Generated knowledge --> The computer gets this knowledge from the new functions defined by us in this program.
#
# When launching in a terminal the command:
# user:~$ python3 this_file.py
# our computer first processes this PYTHON PROGRAM DEFINITION section of the file.
# On it, our computer enhances its Python knowledge from levels (2) and (3) with the imports and new functions
# defined in the program. However, it still does not execute anything.
#
# --------------------------------------------------------

# ------------------------------------------
# IMPORTS
# ------------------------------------------
import sys
import codecs

# ------------------------------------------
# FUNCTION process_line
# ------------------------------------------
def process_line(line):
    # The return tuple
    res = ()



    # Split the line
    line = line.strip().split("\t")



    return res

# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters):
    res = ""

    birth_dict = {}
    time_list = [(i - i) for i in range(24)]

    for line in my_input_stream:
        # Set the values here
        # Split the line
        line = line.strip().split("\t")

        birth_year = line[0]

        # The station name
        # print(lines)
        # print(birth_year)
        time_values = line[1].strip("()").split(" ")
        start_time = int(time_values[0].strip(","))
        start_time_count = int(time_values[1])

        if birth_year in birth_dict:
            birth_dict[birth_year][start_time] += start_time_count
        else:
            birth_dict[birth_year] = time_list.copy()
            birth_dict[birth_year][start_time] = start_time_count

    # Sort hte years
    birth_years = birth_dict.keys()
    birth_years = sorted(birth_years)

    # 1990	(18, 1765)
    for byear in birth_years:
        max_time = max(birth_dict[byear])

        time_value = str(birth_dict[byear].index(max_time) + 1)
        if len(time_value) < 2:
            time_value = "0" + time_value

        res = str(byear) + "\t(" + time_value + ", " + str(max_time) + ")\n"
        # print(res)

        # Output to file
        my_output_stream.write(res)


# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. We collect the input values
    my_input_stream = sys.stdin
    my_output_stream = sys.stdout
    my_reducer_input_parameters = []

    # 5. We call to my_reduce
    my_reduce(my_input_stream,
              my_output_stream,
              my_reducer_input_parameters
             )
