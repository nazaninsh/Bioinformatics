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
    dict_q2={}
    csvreader_1=csv.reader(file1, delimiter='\t')
    for row in csvreader_1:
        dict_q2[row[1], row[2]] = [row[3], row[4]]
    # print(dict_q2)

with open("output_q3.tsv", "r") as file4:
    dict_q3={}
    csvreader_2=csv.reader(file4, delimiter='\t')
    for row in csvreader_2:
        dict_q3[row[1], row[2]] = [row[3], row[4]]
    # print(dict_q3)

set_dict_q2=set(dict_q2)#print only keys
set_dict_q3=set(dict_q3)
for common_keys in set_dict_q2.intersection(set_dict_q3):#print common keys
    (common_keys, dict_q2[common_keys], dict_q3[common_keys])#common keys and common values
    
    common_val_q2= (map(float, dict_q2[common_keys]))# common values and also turning str to float
	common_val_q3= (map(float, dict_q3[common_keys]))#common values and also turning str to float
	#print(common_val_q2)
	#print(common_val_q3)


    for i in range(len(common_val_q3)):
        diff=common_val_q3[i]-common_val_q2[i]
        round= ("%0.2f"%diff)
        increase_percent=0
        if common_val_q2[i]!=0:
            increase_percent= diff/common_val_q2[i]*100
        if i==0 and (increase_percent > 10 or increase_percent < -10):
            print("diff=\t" + "95%ile:" + str(diff) + "\tround=" + str(round) + "\tpercent=" + str("%0.2f"%increase_percent) + "\t" + str(common_keys)+"\n")

        if i==1 and (increase_percent > 10 or increase_percent < -10):
            print("diff=\t" + "5%ile:" + str(diff) + "\tround=" + str(round) + "\tpercent=" + str("%0.2f"%increase_percent) + "\t" + str(common_keys)+"\n")


