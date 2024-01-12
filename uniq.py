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
        if input_array[i] == last_input:
            pass
        else:
            output_array.append(input_array[i])
            last_input = input_array[i]

    return output_array


if len(sys.argv) == 2:
    file_to_read = sys.argv[1]
    f = open(file_to_read)
    l = f.read().splitlines()
    o = findUnique(l)
    for i in o:
        print(i)
else:
    pass
