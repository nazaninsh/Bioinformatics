#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
#print the python version
import sys
print(sys.version)

#to show if the file exist
import os
a=os.path.isfile(sys.argv[1])
print(a)

#open file and search for targeted key words, put in 2 lists
list1=[]
list2=[]
with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    for line in data:
        if line.__contains__('stats'):
            list1.append(line)
        if line.__contains__('thresholds.bbt.db'):
            list2.append(line)
#sort the lists and write them in separate text files
sorted(list1)
with open('list1.txt','w') as f:
    for line in sorted(list1):
        f.write(line)

sorted(list2)
with open('list2.txt','w') as f:
    for line in sorted(list2):
        f.write(line)
