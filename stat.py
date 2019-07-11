#filtering the data to the ones start with 'dataline' and so making 'tsv' file out of it
file = open("output_1.tsv","w")
with open("stats-simple.q2.txt", "r") as f:
    for line in f:
        if line.startswith("dataline"):
            file.write(line)
file.close()

file2= open("output_2.tsv","w")
with open("stats-simple.q3.txt", "r") as f2:
    for line2 in f2:
        if line2.startswith("dataline"):
            file2.write(line2)
file2.close()

#making dictionary. row number 1 and 2 are keys all together and
#row number 3 nd 4 are the values all together
import csv
with open("output_1.tsv", "r") as file1:
    dict_1={}
    csvreader_1=csv.reader(file1, delimiter='\t')
    for row in csvreader_1:
        dict_1[row[1], row[2]] = [row[3], row[4]]
    # print(dict_1)

with open("output_2.tsv", "r") as file4:
    dict_2={}
    csvreader_2=csv.reader(file4, delimiter='\t')
    for row in csvreader_2:
        dict_2[row[1], row[2]] = [row[3], row[4]]
    # print(dict_2)

set_dict_1=set(dict_1)#print only keys
set_dict_2=set(dict_2)
for common_keys in set_dict_1.intersection(set_dict_2):#print common keys
    (common_keys, dict_1[common_keys], dict_2[common_keys])#common keys and common values
    a = dict_1[common_keys]# common values
    b = dict_2[common_keys]#common values

    a2= (map(float, a))#str to float
    b2= (map(float, b))


    for i in range(len(b2)):
        diff=b2[i]-a2[i]
        round= ("%0.2f"%diff)
        increase_percent=0
        if a2[i]!=0:
            increase_percent= diff/a2[i]*100
        if i==0 and (increase_percent > 10 or increase_percent < -10):
            print("diff="+str(common_keys)+":"+" 95%ile:"+str(diff)+" round="+str(round)+ " percent="+str("%0.2f"%increase_percent))

        if i==1 and (increase_percent > 10 or increase_percent < -10):
            print("diff="+str(common_keys)+":"+" 5%ile:"+str(diff)+" round="+str(round)+ " percent="+str("%0.2f"%increase_percent))


