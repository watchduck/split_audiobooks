import re
from os import system

"""
audacity: seconds.000000
mp3splt: minutes.seconds.00
"""

def time_format(seconds_str):
    seconds = int(seconds_str)
    m, s = divmod(seconds, 60)
    return str(m) + '.' + str(s)


chapters_file = open('audacity_labels_out.txt', 'r')

while True:
    chapter_line = chapters_file.readline()
    if chapter_line == '':
        break
    strs = chapter_line.split('\t')
    t1_old = strs[0][0:-5]  # time in seconds with one digit after the point
    t2_old = strs[1][0:-5]
    name = strs[2][0:-1].replace(' ', '_')
    [t1_s, t1_ds] = t1_old.split('.')
    [t2_s, t2_ds] = t2_old.split('.')
    t1 = time_format(t1_s) + '.' + t1_ds + '0'
    t2 = time_format(t2_s) + '.' + t2_ds + '0'
    system('mp3splt uncut.mp3 {t1} {t2} -o chapters/{name}'.format(t1=t1, t2=t2, name=name))
