#filtering the data to the ones start with 'dataline' and so making 'tsv' file out of it
file = open("output_q2.tsv","w")
with open("stats.q2.txt", "r") as f:
    for line in f:
        if line.startswith("dataline"):
            file.write(line)
file.close()


file2= open("output_q3.tsv","w")
with open("stats.q3.txt", "r") as f2:
    for line2 in f2:
        if line2.startswith("dataline"):
            file2.write(line2)
file2.close()

#making dictionary. row number 1 and 2 are keys all together and
#row number 3 nd 4 are the values all together
import csv
with open("output_q2.tsv", "r") as file1:
    dict_1={}
    csvreader_1=csv.reader(file1, delimiter='\t')
    for row in csvreader_1:
        dict_1[row[1], row[2]] = [row[3], row[4]]

    # print(dict_1)
print("***********************")
with open("output_q3.tsv", "r") as file4:
    dict_2={}
    csvreader_2=csv.reader(file4, delimiter='\t')
    for row in csvreader_2:
        dict_2[row[1], row[2]] = [row[3], row[4]]
    # print(dict_2)

# x=set(dict_1)
# print(x) #just printing the keys

set_dict_1=set(dict_1)#print only keys
set_dict_2=set(dict_2)
for common_keys in set_dict_1.intersection(set_dict_2):#print common keys
    print(common_keys, dict_1[common_keys], dict_2[common_keys])#common keys and common values
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



    #the original value is diff=0.034
    #The target value is matched_target_genome::cycle.151~protocol.SLX-Genome_Shotgun_HiSeqX~taxon_id.9606::95%ile::diff=0.034
    #print the percentage that are bigger than 3% on small file and then use it on the big file- and 10% on the big file..

# calculate the number of libraries by adding 5% count and 95% count
#print the number of lib at the end of the line with count=
#change the print out order: the numers first, then the metrics name, then the combination string
#change it to tab delimited file
#filter out all the differences that have lib count of more than that 10
