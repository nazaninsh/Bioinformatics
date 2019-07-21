#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
#print the python version
import sys
print(sys.version)

#to show if the file exist
import os
a=os.path.isfile(sys.argv[1])
print(a)

import re
import csv
seqout = open(sys.argv[2], 'w')
with open(sys.argv[1],'r') as f:
    reader = csv.reader(f, delimiter='\t')
    count_line = 0
    count_yes = 0
    for row in reader:
        match = re.match(r'[atcg]*([atcg])\1{7}[atcg]*', row[1], re.I)
        if match:
            count_line += 1
            if row[2] == 'yes':
                count_yes += 1
            seqout.write(','.join(row) + "\n")
seqout.close()
print('sequences that contain mnr:', count_line)
print('mnr sequences that has a yes in the third column:', count_yes)
