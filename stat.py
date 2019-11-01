#filtering the data to the ones start with 'dataline' and so making 'tsv' file out of it
#do not display if metric is , total_reads , chastity_passed and chastity_passed_no_reagent
count_threshold= 200
file = open("output_q2.tsv","w")
with open("stats.q2.txt", "r") as f:
    for line in f:
        if line.startswith("dataline"):
            if "total_reads" not in line and "chastity_passed" not in line and "chastity_passed_no_reagent" not in line:
                file.write(line)

file.close()

file2= open("output_q3.tsv","w")
with open("stats.q3.txt", "r") as f2:
    for line2 in f2:
        if line2.startswith("dataline"):
            if "total_reads" not in line2 and "chastity_passed" not in line2 and "chastity_passed_no_reagent" not in line2:
                file2.write(line2)

file2.close()

#making dictionary. row number 1 and 2 are keys all together and
#row number 3 and 4 and sub of 5 and 6 are the values all together(3 values)
import csv
with open("output_q2.tsv", "r") as file1:
    dict_q2={}
    csvreader_q2=csv.reader(file1, delimiter='\t')
    for row in csvreader_q2:
        dict_q2[row[1], row[2]] = [row[3], row[4], float(row[5]) + float(row[6])]

    # print(dict_q2)
print("***********************")
with open("output_q3.tsv", "r") as file4:
    dict_q3={}
    csvreader_q3=csv.reader(file4, delimiter='\t')
    for row in csvreader_q3:
        dict_q3[row[1], row[2]] = [row[3], row[4], float(row[5]) + float(row[6])]
    # print(dict_q3)

# x=set(dict_1)
    # print(x) #just printing the keys
result= open("result.tsv", "w")
set_dict_q2=set(dict_q2)#print only keys
set_dict_q3=set(dict_q3)
for common_keys in set_dict_q2.intersection(set_dict_q3):#print common keys
    (common_keys, dict_q2[common_keys], dict_q3[common_keys])#common keys and common values for each quarter

    common_val_q2= (map(float, dict_q2[common_keys]))# common values and also turning str to float
    common_val_q3= (map(float, dict_q3[common_keys]))#common values and also turning str to float
    print(common_val_q2)
    print(common_val_q3)


    for i in range(len(common_val_q3)):
        diff=common_val_q3[i]-common_val_q2[i]
        round= ("%0.2f"%diff)
        increase_percent=0
        if common_val_q2[i]!=0:
            increase_percent= diff/common_val_q2[i]*100

        if (common_val_q2[2] > count_threshold and common_val_q3[2] > count_threshold):
            if i==0  and (increase_percent > 10 or increase_percent < -10):
                # result.write("lib_q2=" + str(common_val_q2[2]) + "\t" +"lib_q3=" + str(common_val_q3[2]) + "\n")
                result.write("diff=\t" + "\t5%ile_round:" + str(round) +"\t"+ "\tpercent=" + str("%0.2f"%increase_percent) + "\t\t" + "lib_q2=" + str(common_val_q2[2]) + "\t" +"lib_q3=" + str(common_val_q3[2]) + str(common_keys)+ "\n")
            if i==1 and (increase_percent > 10 or increase_percent < -10):
                # result.write("lib_q2=" + str(common_val_q2[2]) + "\t" + "lib_q3=" +  str(common_val_q3[2]) + "\n")
                result.write("diff=\t" + "\t95%ile_round:" + str(round) +"\t"+ "\tpercent=" + str("%0.2f"%increase_percent) + "\t\t" + "lib_q2=" + str(common_val_q2[2]) + "\t" +"lib_q3=" + str(common_val_q3[2]) + str(common_keys)+ "\n")
result.close()

        # if common_val_q2[2] > 10 and common_val_q3[2] > 10:
        #     if i==0  and (increase_percent > 10 or increase_percent < -10) or (i==1 and (increase_percent > 10 or increase_percent < -10)):
        #         result.write("lib_q2=" + str(common_val_q2[2]) + "\t" +"lib_q3=" + str(common_val_q3[2]) + "\n")
        #         result.write("diff=\t" + "\t5%ile_round:" + str(round) +"\t"+ "\tpercent=" + str("%0.2f"%increase_percent) + "\t\t" + str(common_keys)+ "\n")
        #         result.write("diff=\t" + "\t95%ile_round:" + str(round) +"\t"+ "\tpercent=" + str("%0.2f"%increase_percent) + "\t\t" + str(common_keys)+ "\n")



        # if (common_val_q2[2] > 10 and common_val_q3[2] > 10):
        #     if i==0  and (increase_percent > 10 or increase_percent < -10):
        #         result.write("lib_q2=" + str(common_val_q2[2]) + "\t" +"lib_q3=" + str(common_val_q3[2]) + "\n")
        #         result.write("diff=\t" + "\t5%ile_round:" + str(round) +"\t"+ "\tpercent=" + str("%0.2f"%increase_percent) + "\t\t" + str(common_keys)+ "\n")
        #     if i==1 and (increase_percent > 10 or increase_percent < -10):
        #         result.write("lib_q2=" + str(common_val_q2[2]) + "\t" + "lib_q3=" +  str(common_val_q3[2]) + "\n")
        #         result.write("diff=\t" + "\t95%ile_round:" + str(round) +"\t"+ "\tpercent=" + str("%0.2f"%increase_percent) + "\t\t" + str(common_keys)+ "\n")

        # if common_val_q2[2] > 10 and common_val_q3[2] > 10 and i==0 and (increase_percent > 10 or increase_percent < -10):
        #     result.write("lib_q2=" + str(common_val_q2[2]) + "\t" +"lib_q3=" + str(common_val_q3[2]) + "\n")
        #     result.write("diff=\t" + "\t5%ile_round:" + str(round) +"\t"+ "\tpercent=" + str("%0.2f"%increase_percent) + "\t\t" + str(common_keys)+ "\n")
        # if common_val_q2[2] > 10 and common_val_q3[2] > 10 and i==1 and (increase_percent > 10 or increase_percent < -10):
        #     result.write("lib_q2=" + str(common_val_q2[2]) + "\t" + "lib_q3=" +  str(common_val_q3[2]) + "\n")
        #     result.write("diff=\t" + "\t95%ile_round:" + str(round) +"\t"+ "\tpercent=" + str("%0.2f"%increase_percent) + "\t\t" + str(common_keys)+ "\n")
# result.close()


#print the percentage that are bigger than 3% on small file and then use it on the big file- and 10% on the big file..
# calculate the number of libraries by adding 5% count and 95% count
#print the number of lib at the end of the line with count=
#change the print out order: the numbers first, then the metrics name, then the combination string
#change it to tab delimited file
#filter out all the differences that have lib count of more than that 10
# how the numbers are changing over time between diff quarters..

#use CSV writer to create a tab delimited file instead of manually!!
#Git Toturial

#add the 5%ile count to the 95%ile count to get the total number of lib in that quarter for each line
#calculate the percent diff in the metrics- ( already done)
# only print out the diff if both total number of lib( in 2 quarters) is greatre than 10

#for Aug21:
#1. the count of lib in each quarter in the result file
#2. remove 5%ile and 95%ile
#3. do not display if metric is , total_reads , chastity_passed and chastity_passed_no_reagent
#4. rename round to 5%ile_round and 95%ile_round

#for sep
#making a test file by myself to confirm the calculation
#1. chnage number of lib to variable
#2. change percent diff to a variable as well
#3. make the above variable into a command line argument using argv
