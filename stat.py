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

#making inner dict and outer dict
import csv
with open("output_1.tsv", "r") as file1:
    outer_dict_1={}
    inner_dict_1={}
    csvreader_1=csv.reader(file1, delimiter='\t')
    for row in csvreader_1:
        inner_dict_1[row[2]] = [row[3], row[4]]#values for inner dict
        outer_dict_1[row[1]] = inner_dict_1

    print(outer_dict_1)

with open("output_2.tsv", "r") as file4:
    outer_dict_2={}
    inner_dict_2={}
    csvreader_2=csv.reader(file4, delimiter='\t')
    for row in csvreader_2:
        inner_dict_2[row[2]] = [row[3], row[4]]
        outer_dict_2[row[1]] = inner_dict_2

    print(outer_dict_2)
