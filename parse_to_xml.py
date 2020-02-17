#!/usr/bin/python3
# - * - encode: utf-8  - * -
import sys
import re

file_path = sys.argv[1]
wrapper = file_path.split('/')[-1]
ofile = wrapper + '.xml'

with open(file_path, 'r') as f:
     lines = f.readlines()
     f.close()

new_line = []
new_line.append(f'<{wrapper}>\n')
for line in lines:
    #guardian
    line = line.rstrip()
    if len(line) <= 0 or re.findall('^#', line):
        continue
    new_line.append(f'\t<{line[:line.index("=")].lower()} {line}>\n')
new_line.append(f'</{wrapper}>\n')

with open(ofile, 'w') as f: 
    for line in new_line:
        f.write(line)
    f.close()
