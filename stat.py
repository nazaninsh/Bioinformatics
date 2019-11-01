file = open("output_1.tsv","w+")
with open("stats.q2.txt", "r") as f:
    # read=f.readlines()
    for line in f:
        if line.startswith("dataline"):
            file.write(line)


file = open("output_2.tsv","w+")
with open("stats.q3.txt", "r") as f:
    # read=f.readlines()
    for line in f:
        if line.startswith("dataline"):
            file.write(line)


import csv
with open("output_1.tsv", "r") as file1:
    outer_dict_1={}
    inner_dict_1={}
    csvreader_1=csv.reader(file1, delimiter='\t')
    for row in csvreader_1:
        inner_dict_1[row[2]] = [row[3], row[4]]
        outer_dict_1[row[1]] = inner_dict_1

    print outer_dict_1

with open("output_2.tsv", "r") as file2:
    outer_dict_2={}
    inner_dict_2={}
    csvreader_2=csv.reader(file2, delimiter='\t')
    for row in csvreader_2:
        inner_dict_2[row[2]] = [row[3], row[4]]
        outer_dict_2[row[1]] = inner_dict_2

    print outer_dict_2

#
#
# # outer_dict_1 = {
# # "top_unexpected_count" :
# #     {
# #         "cycle.1236": [100,34],
# #         "cycle.32644": [43,90]
# #     },
# # "chastity_passed":
# #     {
# #         "cycle.1236": [80,76],
# #         "cycle.32644": [65,56]
# #     },
# #     "matched_host_genome": {
# #         "sdglpod.1236": [80,76],
# #         "rlkt.32644": [65,56]
# #     }
# #
# # }
# #
# # outer_dict_2 = {
# # "top_unexpected_count" :
# #     {
# #         "cycle.1236": [32,43],
# #         "cycle.9606": [78,59]
# #     },
# # "chastity_passed":
# #     {
# #         "cycle.1236": [86,66],
# #         "cycle.9606": [91,76]
# #     }
# # }
# # Iterate through dict
# common_set = nil  #nil means empty of anything
for outer_key in outer_dict_1:
    file_1_inner_dict_1 = outer_dict_1[outer_key] #outer key example : chastity_passed
    file_1_set_1 = set(file_1_inner_dict_1)

    if outer_key in outer_dict_2:
        file_2_inner_dict_2 = outer_dict_2[outer_key]
        file_2_set_2 = set(file_2_inner_dict_2)
        common_set = file_1_set_1.intersection(file_2_set_2)  #intersection gives you common inner keys
        print (outer_key)

    # inner_dict_1 = outer_dict_1[k]
    # ===========
# myRDP = { 'Actinobacter': 'GATCGA...TCA', 'subtilus sp.': 'ATCGATT...ACT' }
# myNames = { 'Actinobacter': '8924342' }
#
# rdpSet = set(myRDP)
# namesSet = set(myNames)
# for name in rdpSet.intersection(namesSet):
#     print name, myNames[name]
# =================

#
# val = dict["naz"]
# val["name"]

# dict =	{
# "naz":
#     {
#         "name": "Nazanin",
#         "location": "Vancouver",
#         "likes": 346,
#         "previous_location": ["London", "Sydney"]
#     },
# "sel":
#     {
#         "name": "Selva",
#         "location": "New West",
#         "previous_location": ["Spain", "France"]
#     }
# }
# print dict
# print "========================"
