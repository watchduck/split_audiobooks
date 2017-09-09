import re

chapters_str = open('audible_chapters.txt', 'r').read()
chapters = re.sub(r'Kapitel (\d+) / ', r'', chapters_str)

times_str = chapters.split()
times_list = []

for time_str in times_str:
    hms_strs = time_str.split(':')
    h = int(hms_strs[0])
    m = int(hms_strs[1])
    s = int(hms_strs[2])
    times_list.append(h*3600 + m*60 + s)

labels_file = open('audacity_labels_in.txt','w')

for i in range(len(times_list)-1):
    labels_file.write('{t1}.000000\t{t2}.000000\tc{i}\n'.format(
        t1=times_list[i],
        t2=times_list[i+1],
        i=i
    ))
