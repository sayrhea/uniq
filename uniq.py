### The uniq utility reads the specified input_file comparing adjacent lines, and
### writes a copy of each unique input line to the output_file.  If input_file is a
### single dash (‘-’) or absent, the standard input is read.  If output_file is
### absent, standard output is used for output.  The second and succeeding copies
### of identical adjacent input lines are not written.  Repeated lines in the input
### will not be detected if they are not adjacent, so it may be necessary to sort
### the files first.

import sys


def findUnique(input_array):
    output_array = []

    last_input = None

    for i in range(0, len(input_array)):
        if input_array[i] != last_input:
            output_array.append({"value": input_array[i], "count": 1})
            last_input = input_array[i]
        else:
            output_array[-1]["count"] += 1

    return output_array


if __name__ == "__main__":
    command_line_args = sys.argv.copy()
    supported_flags = ["-c", "-d", "-u"]
    command_line_args = list(
        filter(lambda x: x not in supported_flags, command_line_args)
    )
    count_flag = "-c" in sys.argv
    repeated_flag = "-d" in sys.argv
    unique_flag = "-u" in sys.argv

    input_file = sys.stdin
    if len(command_line_args) > 1:
        filename = command_line_args[1]
        if filename != "-":
            input_file = open(filename)

    input_lines = input_file.read().splitlines()

    output_lines = findUnique(input_lines)

    output_file = sys.stdout
    if len(command_line_args) > 2:
        filename = command_line_args[2]
        output_file = open(command_line_args[2], "w")

    for i in output_lines:
        if repeated_flag and i["count"] < 2:
            continue
        if unique_flag and i["count"] > 1:
            continue

        val = i["value"]
        if count_flag:
            val = f"{i['count']} {i['value']}"
        print(val, file=output_file)
