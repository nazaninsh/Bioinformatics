k=4
seq='ACGGGGGACGGTCT'
mydict=dict() #empty dictionary
for i in range(len(seq)-k+1):
    print(seq[i:k+i])
    kmer = seq[i:i+k]
    if kmer in mydict:
        mydict[kmer]+=1
    else:
        mydict[kmer]=1


myoutfile = open("kmer_count.txt","w")
for kmer in mydict:
    myoutfile.write(kmer + " " + str(mydict[kmer])+"\n")
