import re
import math

chapters_str = open('audible_chapters.txt', 'r').read()
chapters = re.sub(r'Kapitel (\d+) ', r'', chapters_str)

time_strings = chapters.split()  # array of strings like '01:23:45'
number_of_chapters = len(time_strings)
number_of_digits = int(math.log10(number_of_chapters))+1

times_list = []
time_sum = 0
time_padding = 0.5  # approximate gap between tracks

for time_string in time_strings:
    hms = time_string.split(':')
    h = int(hms[0])
    m = int(hms[1])
    s = int(hms[2])
    time_addend = h*3600 + m*60 + s  # duration of the chapter
    time_sum += time_addend + time_padding
    times_list.append(time_sum)

labels_file = open('audacity_labels_in.txt','w')

for i in range(len(times_list)-1):
    labels_file.write('{t1}\t{t2}\t{i}\n'.format(
        t1=format(times_list[i  ], '.6f'),
        t2=format(times_list[i+1], '.6f'),
        i=str(i).zfill(number_of_digits)
    ))
