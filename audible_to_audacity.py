import re
import math
import sys

# offset for the chapter numbers
try:
	offset = int(sys.argv[1])
except IndexError:
	offset = 0

input_with_line_breaks = open('audible_chapters.txt', 'r').read()
input_list = input_with_line_breaks.split('\n')
# chapter names even, chapter times odd (counting from 0)

num = len(input_list)//2  # number of chapters
time_strings = [input_list[2*i+1] for i in range(num)]
# array of strings like '01:23:45'

times_list = [0]
time_sum = 0
time_padding = 0.5  # approximate gap between tracks

for time_string in time_strings:
    hms = time_string.split(':')
    h = int(hms[0])
    m = int(hms[1])
    s = int(hms[2])
    time_addend = h*3600 + m*60 + s + time_padding # duration of the chapter
    time_sum += time_addend
    times_list.append(time_sum)

number_of_digits_in_name = int(math.log10(num+offset))+1

labels_file = open('audacity_labels_in.txt','w')

for i in range(len(times_list)-1):
    labels_file.write('{start}\t{end}\t{name}\n'.format(
        start=format(times_list[i], '.6f'),  # '.6f' creates 6 digits after the decimal point (instead of 1)
        end=format(times_list[i+1], '.6f'),
        name=str(i+offset).zfill(number_of_digits_in_name)
	))
